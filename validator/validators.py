from typing import Any, Self

from validator.exceptions import ValidationError
from validator.rule import Rule
from validator.schema import Schema


class BaseValidator:
    def __init__(self, schema: Schema | None = None) -> None:
        self.schema = schema or Schema()

    def string(self) -> 'StringValidator':
        self.schema.add_type(str)
        return StringValidator(self.schema)

    def required(self) -> Self:
        self.schema.required = True
        return self

    def is_valid(self, value: Any, *, raise_exceptions: bool = False) -> bool:
        try:
            return self.schema.check_value(value)

        except ValidationError:
            if raise_exceptions:
                raise

            return False


class StringValidator(BaseValidator):
    def min_len(self, min_length: int) -> Self:
        rule = Rule(rule_func=lambda value: len(value) >= min_length)
        self.schema.add_rule('min_len', rule)
        return self

    def contains(self, chunk: str) -> Self:
        rule = Rule(rule_func=lambda value: chunk in value)
        self.schema.add_rule('contains', rule)
        return self
