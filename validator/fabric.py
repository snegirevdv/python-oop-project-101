from validator.base import BaseValidator
from validator.string import StringValidator


class Validator:
    def __init__(self) -> None:
        pass

    def string(self) -> StringValidator:
        return StringValidator()

    def base(self) -> BaseValidator:
        return BaseValidator()
