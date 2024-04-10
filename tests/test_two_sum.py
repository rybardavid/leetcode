import pytest
from src.two_sum import twoSum

@pytest.mark.parametrize(
        "numbers, target, expected",
        [
            [[2,7,11,15], 9, [0,1]],
            [[3,2,4], 6, [1,2]],
            [[3,3], 6, [0,1]],
            [[2,1,5,3], 4, [1,3]],
        ],
)
def test_run(numbers: list[int], target: int, expected: list[int]) -> None:
    assert twoSum(numbers, target) == expected