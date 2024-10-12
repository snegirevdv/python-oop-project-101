from validator import Validator


def test_dict_validator_age_none() -> None:
    v = Validator()
    schema = v.dict().shape(
        {
            'name': v.string().required(),
            'age': v.number().positive(),
        }
    )

    assert schema.is_valid({'name': 'maya', 'age': None}) is True


def test_dict_validator_valid_data() -> None:
    v = Validator()
    schema = v.dict().shape(
        {
            'name': v.string().required(),
            'age': v.number().positive(),
        }
    )

    assert schema.is_valid({'name': 'kolya', 'age': 100}) is True


def test_dict_validator_invalid_name() -> None:
    v = Validator()
    schema = v.dict().shape(
        {
            'name': v.string().required(),
            'age': v.number().positive(),
        }
    )

    assert schema.is_valid({'name': '', 'age': None}) is False


def test_dict_validator_negative_age() -> None:
    v = Validator()
    schema = v.dict().shape(
        {
            'name': v.string().required(),
            'age': v.number().positive(),
        }
    )

    assert schema.is_valid({'name': 'ada', 'age': -5}) is False


def test_dict_validator_missing_key() -> None:
    v = Validator()
    schema = v.dict().shape(
        {
            'name': v.string().required(),
            'age': v.number().positive(),
        }
    )

    assert schema.is_valid({'name': 'maya'}) is False
