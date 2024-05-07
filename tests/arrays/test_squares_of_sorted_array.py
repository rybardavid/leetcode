import pytest
from src.arrays.squares_of_sorted_array import run

@pytest.mark.parametrize(
        "numbers, expected",
        [
            [[-4,-1,0,3,10], [0,1,9,16,100]],
            [[-7,-3,2,3,11], [4,9,9,49,121]],
        ]
)
def test_run(numbers: list[int], expected: list[int]) -> None:
    assert run(numbers) == expected