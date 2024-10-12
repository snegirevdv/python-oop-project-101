from validator import Validator


def test_string_validator_starts_with() -> None:
    v = Validator()
    fn = lambda value, start: value.startswith(start)  # noqa: E731
    v.add_validator('string', 'startWith', fn)

    schema = v.string().test('startWith', 'H')

    assert schema.is_valid('exlet') is False
    assert schema.is_valid('Hexlet') is True


def test_number_validator_min():
    v = Validator()
    fn = lambda value, min: value >= min  # noqa: E731
    v.add_validator('number', 'min', fn)

    schema = v.number().test('min', 5)

    assert schema.is_valid(4) is False
    assert schema.is_valid(6) is True
