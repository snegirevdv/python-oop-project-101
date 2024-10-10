from validator import Validator


def test_string_schema_valid_empty() -> None:
    v = Validator()
    schema = v.string()

    assert schema.is_valid('') is True
    assert schema.is_valid(None) is True
    assert schema.is_valid('what does the fox say') is True


def test_string_schema_required() -> None:
    v = Validator()
    schema = v.string().required()

    assert schema.is_valid('') is False
    assert schema.is_valid(None) is False
    assert schema.is_valid('hexlet') is True


def test_string_schema_independence() -> None:
    v = Validator()
    schema1 = v.string()
    schema2 = v.string()

    assert schema1 != schema2, 'Схемы равны'
    assert schema1.is_valid('') is True

    schema1.required()

    assert schema2.is_valid('') is True
    assert schema1.is_valid('') is False
    assert schema1.is_valid(None) is False
    assert schema1.is_valid('hexlet') is True


def test_string_schema_contains() -> None:
    v = Validator()
    schema = v.string().contains('what')

    assert schema.is_valid('what does the fox say') is True
    assert (
        schema.contains('whatthe').is_valid('what does the fox say') is False
    )


def test_string_schema_min_len() -> None:
    v = Validator()
    schema = v.string().min_len(10)

    assert schema.is_valid('Hexlet') is False
    assert schema.min_len(4).is_valid('Hexlet') is True


def test_last_min_len_overrides() -> None:
    v = Validator()

    schema = v.string().min_len(10).min_len(4)

    assert schema.is_valid('Hexlet') is True
    assert schema.is_valid('Hi') is False
