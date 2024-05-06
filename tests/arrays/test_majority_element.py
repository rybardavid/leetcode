import pytest
from src.arrays.majority_element import run

@pytest.mark.parametrize(
        "numbers, expected",
        [
            [[3,2,3], 3]
            ]
)
def test_run(numbers: list[int], expected: int) -> None:
    assert run(numbers) == expected