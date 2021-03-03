# SDET COVID-19 Coding Test 🦠

The app estimates the chance that at least one COVID-19 positive
individual will be present at a event of a given size. For example:

> At a concert in England with 2000 people in the audience, what is the
> probability that at least one of them currently has COVID-19?

The dataset in `data.json` contains the daily number of new Coronavirus cases
for each United Kingdom nation (England, Scotland, Wales, Northern Ireland)
[published by the UK government](https://coronavirus.data.gov.uk/).

```javascript
{
    "length": 1700,
    "body": [
        {
            "date": "2021-03-02",
            "areaType": "nation",
            "areaCode": "N92000002",
            "areaName": "Northern Ireland",
            "newCasesByPublishDate": 149
        },
        // etc.
    ]
}
```

The API exposes two endpoints:

* `GET /areas` - returns a list of areas where events can take place.
* `POST /compute` - given an area and event size, returns the probability
  of at least one person at the event having Coronavirus.

The user chooses an area from the list returned by the `GET /areas` API:

```bash
curl http://localhost:5000/areas
```

```json
{
  "items": [
    {
      "code": "E92000001",
      "name": "England"
    },
    {
      "code": "N92000002",
      "name": "Northern Ireland"
    },
    {
      "code": "S92000003",
      "name": "Scotland"
    },
    {
      "code": "W92000004",
      "name": "Wales"
    }
  ]
}
```

Then uses the `POST /compute` API to calculate the probability:

```bash
curl -X POST http://localhost:5000/compute --data '{"sample": 2000, "area_code": "E92000001"}'
```

```json
{
  "probability": 0.9999994281491117
}
```

Note: the probabilities it produces are "just for fun", don't take them too seriously!

## Overview 🔭

The app is written in Python using the Flask framework.

```
covid_app/
  model.py       ← module to compute probabilities
  dataset.py     ← module to read the dataset from the filesystem
  validation.py  ← module to validate incoming requests

tests/
  unit/          ← unit tests
  integration/   ← integration tests
  e2e/           ← end to end tests

app.py           ← API views
data.json        ← number of new cases per day and nation
requirements.txt ← Python dependencies
```

## Goals 🎯

As you will discover, the app is not ready for production quite yet! The goals of this exercise are to:

1. Talk through the code and explain what it does.
2. Run the application, and make a request with `curl`.
3. Write some tests to give us confidence the app is working (hint: edge cases!).
   Use your judgement to decide what types of test to focus on: unit, integration, and E2E.

## Running the app

In Repl.it, you can simply click the green _Run_ button, the output will be shown in the _Console_ tab.

Create a virtualenv and install the requirements:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip3 install -r requirements.txt
```

Run the app:

```bash
flask run
```

Note: this will run the `app.py`.

Make an API request using `curl`:

```bash
curl -X POST http://localhost:5000/compute --data '{"sample": 2000, "area_code": "E92000001"}'
```

## Running the tests

In Repl.it, you can run commands from the _Shell_ tab.

You can run all the tests with:

```bash
pytest tests
```

Or just the unit tests (for example) with:

```bash
pytest tests/unit
```

Note: the E2E tests expect the app to be running and listening on `localhost:5000`.
