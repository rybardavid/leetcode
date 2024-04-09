import pytest
from src.contains_duplicates import run

@pytest.mark.parametrize(
        "numbers, expected",
        [
            [[1,2,3,1], True],
            [[1,2,3,4], False],
            [[1,1,1,3,3,4,3,2,4,2], True],
            [[3,3], True],
            [[], False],
            [[1, -1], False],
        ],
)
def test_run(numbers: list[int], expected: bool) -> None:
    assert run(numbers) == expected