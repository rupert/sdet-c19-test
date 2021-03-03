from datetime import date, timedelta

from covid_app.dataset import Dataset

POPULATIONS = {
    "E92000001": 56_286_961,  # England
    "S92000003": 5_463_300,  # Scotland
    "W92000004": 3_152_879,  # Wales
    "N92000002": 1_893_667,  # Northern Ireland
}


def compute_probability(
    *, dataset: Dataset, area_code: str, date: date, sample: int
) -> float:
    """
    Given a group of people gather on a particular date and area of the country, compute
    the probability that at least one of them currently has coronavirus.

    Args:
        dataset: the dataset used to compute the probability.
        area_code: the area where the gathering took place.
        date: the date the gathering took place.
        sample: the number of people that attended the gathering.
    """

    start_date = date - timedelta(days=10)

    # Count the number of active cases with a positive test
    # in the last n days
    active_cases = sum(
        row.newCasesByPublishDate
        for row in dataset.body
        if row.date >= start_date
        if row.areaCode == area_code
    )

    # Multiply the number of cases to account for people with
    # coronavirus who haven't had a positive test
    active_cases *= 5

    # Get the population of the specified area
    population = POPULATIONS[area_code]

    # Probability of someone in the population currently having coronavirus
    population_p = active_cases / population

    # Probability of someone in the sample currently having coronavirus
    #
    # sample_p = 1 - x
    #   Where x = probability of nobody in the sample having coronavirus
    sample_p = 1 - (1 - population_p) ** sample

    return sample_p
