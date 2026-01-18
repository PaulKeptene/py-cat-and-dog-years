import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "All zeroes",
        "All less than 15",
        "All 15",
        "All 24",
        "All 28",
        "All 100",
    ]
)
def test_calculation_with_diff_val(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert (get_human_age(cat_age, dog_age) == result), \
        f"Age values from {cat_age} and {dog_age} should be equal to {result}"
