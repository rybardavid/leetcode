import pytest
from src.buy_and_sell_stock.program import run

@pytest.mark.parametrize(
        "numbers, expected",
        [
            [[7,1,5,3,6,4], 5],
            [[7,6,4,3,1], 0],
        ],
)
def test_run(numbers: list[int], expected: int) -> None:
    assert run(numbers) == expected