from datetime import date
from pathlib import Path

import attr
from flask import Flask, request
from cattr import structure
from covid_app.dataset import read_dataset
from covid_app.model import compute_probability

app = Flask(__name__)

dataset = read_dataset(Path(__file__).parent / "data.json")


@attr.s(auto_attribs=True, frozen=True)
class InputParams:
    area_code: str
    sample: int


@app.route("/compute", methods=["POST"])
def compute():
    body = request.get_json(force=True)

    input_params = structure(body, InputParams)

    probability = compute_probability(
        dataset=dataset,
        area_code=input_params.area_code,
        sample=input_params.sample,
        date=date(2021, 3, 2),
    )

    return {"probability": probability}


@app.route("/areas")
def list_areas():
    """
    List the areas supported by the API.
    """

    return {
        "items": [
            {"code": "E92000001", "name": "England",},
            {"code": "N92000002", "name": "Northern Ireland",},
            {"code": "S92000003", "name": "Scotland",},
            {"code": "W92000004", "name": "Wales",},
        ]
    }
