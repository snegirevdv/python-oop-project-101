from collections.abc import Callable
from typing import Generic, Self, TypeVar

Type = TypeVar('Type')


class BaseValidator(Generic[Type]):
    def __init__(self) -> None:
        self._schema = []
        self._required = False

        self.add_rule(lambda value: isinstance(value, Type))

    def add_rule(self, rule: Callable) -> None:
        self._schema.append(rule)

    def required(self) -> Self:
        self._required = True
        return self

    def is_valid(self, value: Type | None) -> bool:
        if not value:
            return not self._required

        return all(check(value) for check in self._schema)
