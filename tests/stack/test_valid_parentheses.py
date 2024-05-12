import pytest
from src.stack.valid_parentheses import run

@pytest.mark.parametrize(
        "s, expected",
        [
            ['()', True],
            ['()[]{}', True],
            ['([{()}]){}[]', True],
            ['([}]){}[]', False],
            ['(]', False],
            [']', False],
            ['[', False],
        ],
)
def test_run(s: str, expected: bool) -> None:
    assert run(s) == expected