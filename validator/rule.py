from collections.abc import Callable

from validator.exceptions import ValidationError


class Rule:
    def __init__(self, rule_func: Callable, description: str = '') -> None:
        self.rule = rule_func
        self.description = description

    def check(self, *args, **kwargs) -> bool:
        result = bool(self.rule(*args, **kwargs))

        if not result:
            msg = f'Validation Error: {self.description}'
            raise ValidationError(msg)

        return result
