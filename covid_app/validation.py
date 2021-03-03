from typing import Any

import attr


@attr.s(auto_attribs=True, frozen=True)
class InputParams:
    area_code: str
    sample: int


def validate_input_params(data: Any) -> InputParams:
    if not isinstance(data, dict):
        raise ValueError("Expected an object")

    try:
        area_code = data["area_code"]
    except KeyError:
        raise ValueError("area_code is required")

    try:
        sample = data["sample"]
    except KeyError:
        raise ValueError("sample is required")

    return InputParams(area_code=area_code, sample=sample)
