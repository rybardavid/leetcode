import pytest
from src.two_pointers.continaer_with_most_water import run

@pytest.mark.parametrize(
        "numbers, expected",
        [
            [[1,8,6,2,5,4,8,3,7], 49],
            [[1,1], 1]
        ]
)
def test_run(numbers: list[int], expected: int) -> None:
    assert run(numbers) == expected