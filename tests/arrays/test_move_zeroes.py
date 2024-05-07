import pytest
from src.arrays.move_zeroes import run

@pytest.mark.parametrize(
        "numbers, expected",
        [
            [[0,1,0,3,12], [1,3,12,0,0]],
            [[0],[0]],
            [[0,0,1],[1,0,0]],
        ]
)
def test_run(numbers: list[int], expected: list[int]) -> None:
    run(numbers)
    assert numbers == expected