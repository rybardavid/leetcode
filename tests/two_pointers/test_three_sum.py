import pytest
from src.two_pointers.three_sum import run

@pytest.mark.parametrize(
        "numbers, expected",
        [
            [[-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]],
        ]
)
def test_run(numbers: list[int], expected: list[int]) -> None:
    assert run(numbers) == expected