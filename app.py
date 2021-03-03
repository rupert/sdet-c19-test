from datetime import date
from pathlib import Path

from flask import Flask, request
from covid_app.dataset import read_dataset
from covid_app.model import compute_probability
from covid_app.validation import validate_input_params

app = Flask(__name__)

dataset = read_dataset(Path(__file__).parent / "data.json")


@app.route("/compute", methods=["POST"])
def compute():
    """
    Compute the probability of at least one COVID-19 positive
    individual being present at an event of a given size.
    """

    body = request.get_json(force=True)

    try:
        input_params = validate_input_params(body)
    except ValueError as exc:
        return {"message": str(exc)}, 400

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
            {
                "code": "E92000001",
                "name": "England",
            },
            {
                "code": "N92000002",
                "name": "Northern Ireland",
            },
            {
                "code": "S92000003",
                "name": "Scotland",
            },
            {
                "code": "W92000004",
                "name": "Wales",
            },
        ]
    }
