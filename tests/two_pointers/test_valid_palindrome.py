import pytest
from src.two_pointers.valid_palindrome import run

@pytest.mark.parametrize(
        "s, expected",
        [
            ["A man, a plan, a canal: Panama", True],
            ["race a car", False],
            [" ", True],
        ],
)
def test_run(s: str, expected: bool) -> None:
    assert run(s) == expected