from collections import defaultdict
from collections.abc import Callable
from numbers import Number
from typing import Any, Self


class Validator:
    def __init__(self) -> None:
        self.validators = defaultdict(dict)

    def add_validator(
        self,
        type_name: str,
        validator_name: str,
        func: Callable,
    ) -> None:
        self.validators[type_name][validator_name] = func

    def string(self) -> 'StringSchema':
        return StringSchema(self)

    def number(self) -> 'NumberSchema':
        return NumberSchema(self)

    def list(self) -> 'ListSchema':
        return ListSchema(self)

    def dict(self) -> 'DictSchema':
        return DictSchema(self)


class BaseSchema:
    def __init__(self, validator: Validator) -> None:
        self.validator: Validator = validator
        self.checks: dict[str, Callable] = {}
        self.type_name: str = 'all'
        self.is_required: bool = False
        self.type_check: Callable | None = lambda _: True
        self.required_check: Callable | None = lambda value: value is not None

    def is_valid(self, value: Any) -> bool:
        if self.is_required and not self.required_check(value):
            return False

        if not self.type_check(value):
            return False

        return all(check(value) for check in self.checks.values())

    def required(self) -> Self:
        self.is_required = True
        return self

    def test(self, validator_name: str, *args) -> Self:
        def check(value: Any) -> bool:
            func = self.validator.validators[self.type_name].get(
                validator_name
            )
            return func(value, *args) if func else True

        self.checks[validator_name] = check
        return self


class StringSchema(BaseSchema):
    def __init__(self, validator: Validator) -> None:
        super().__init__(validator)
        self.type_name = 'string'
        self.type_check = lambda value: isinstance(value, str | None)
        self.required_check = lambda value: value

    def min_len(self, min_length: int) -> Self:
        self.checks['min_len'] = lambda value: len(value) >= min_length
        return self

    def contains(self, substring: str) -> Self:
        self.checks['contains'] = lambda value: substring in value
        return self


class NumberSchema(BaseSchema):
    def __init__(self, validator: Validator) -> None:
        super().__init__(validator)
        self.type_name = 'number'
        self.type_check = lambda value: isinstance(value, Number | None)

    def positive(self) -> Self:
        self.checks['positive'] = lambda value: value > 0
        return self

    def range(self, min_value: Number, max_value: Number) -> Self:
        self.checks['range'] = lambda value: min_value <= value <= max_value
        return self


class ListSchema(BaseSchema):
    def __init__(self, validator: Validator) -> None:
        super().__init__(validator)
        self.type_name = 'list'
        self.type_check = lambda value: isinstance(value, list | None)

    def sizeof(self, size: int) -> Self:
        self.checks['sizeof'] = lambda value: len(value) == size
        return self


class DictSchema(BaseSchema):
    def __init__(self, validator: Validator) -> None:
        super().__init__(validator)
        self.type_name = 'dict'
        self.type_check = lambda value: isinstance(value, dict | None)
        self.shape_validators = {}

    def shape(self, structure: dict[str, BaseSchema]) -> Self:
        self.shape_validators = structure
        self.checks['shape'] = self._validate_shape
        return self

    def _validate_shape(self, value: Any) -> bool:
        return all(
            schema.is_valid(value[key])
            for key, schema in self.shape_validators.items()
        )
