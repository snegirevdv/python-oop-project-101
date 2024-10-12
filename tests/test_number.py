from validator import Validator


def test_number_validator_none() -> None:
    v = Validator()
    schema = v.number()

    assert schema.is_valid(None) is True


def test_number_validator_required() -> None:
    v = Validator()
    schema = v.number().required()

    assert schema.is_valid(None) is False


def test_number_validator_type_int() -> None:
    v = Validator()
    schema = v.number()

    assert schema.is_valid(7) is True
    assert schema.is_valid('7') is False


def test_number_validator_positive() -> None:
    v = Validator()
    schema = v.number().positive()

    assert schema.is_valid(10) is True
    assert schema.is_valid(-10) is False


def test_number_validator_range() -> None:
    v = Validator()
    schema = v.number().range(-5, 5)

    assert schema.is_valid(-5) is True
    assert schema.is_valid(0) is True
    assert schema.is_valid(5) is True
    assert schema.is_valid(-6) is False
    assert schema.is_valid(6) is False


def test_number_validator_positive_and_range() -> None:
    v = Validator()
    schema = v.number().positive().range(-5, 5)

    assert schema.is_valid(-5) is False
    assert schema.is_valid(0) is False
    assert schema.is_valid(5) is True
