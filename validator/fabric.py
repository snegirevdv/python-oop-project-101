from validator.schema import Schema
from validator.validators import StringValidator


class ValidatorFabric:
    def string(self) -> StringValidator:
        schema = Schema()
        schema.add_type(str)
        return StringValidator(schema)
