import pytest

from covid_app.validation import validate_input_params


def test_sample_is_required():
    body = {"area_code": "N92000002"}

    with pytest.raises(ValueError) as e:
        validate_input_params(body)

    assert str(e.value) == "sample is required"
