from validator import Validator


def test_list_validator_none() -> None:
    v = Validator()
    schema = v.list()

    assert schema.is_valid(None) is True


def test_list_validator_required() -> None:
    v = Validator()
    schema = v.list().required()

    assert schema.is_valid([]) is True
    assert schema.is_valid(['hexlet']) is True


def test_list_validator_sizeof() -> None:
    v = Validator()
    schema = v.list().required().sizeof(2)

    assert schema.is_valid(['hexlet']) is False
    assert schema.is_valid(['hexlet', 'code-basics']) is True
