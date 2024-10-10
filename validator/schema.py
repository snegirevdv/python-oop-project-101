from typing import Any

from validator.rule import Rule


class Schema:
    def __init__(
        self,
        *,
        types: list[type] | None = None,
        rules: dict[str, Rule] | None = None,
        required: bool = False,
    ) -> None:
        self.types: list[type] = types or []
        self.rules: dict[str, Rule] = rules or {}
        self.required: bool = required

    def add_rule(self, name: str, rule: Rule) -> None:
        self.rules[name] = rule

    def add_type(self, new_type: type) -> None:
        self.types.append(new_type)

    def check_value(self, value: Any) -> bool:
        if not value:
            return not self.required

        if not any(isinstance(value, data_type) for data_type in self.types):
            return False

        return all(rule.check(value) for rule in self.rules.values())
