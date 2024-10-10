from typing import Self

from validator.base import BaseValidator


class StringValidator(BaseValidator[str]):
    def min_len(self, min_length: int) -> Self:
        self.add_rule(lambda value: len(value) > min_length)
        return self

    def contains(self, chunk: str) -> Self:
        self.add_rule(lambda value: chunk in value)
        return self
