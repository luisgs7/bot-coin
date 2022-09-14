"""Test Filet"""


def sum_value(value_a: int, value_b: int) -> int:
    """Func Sum"""
    return value_a + value_b


def test_sum():
    """Test Sum"""
    assert sum_value(2, 3) == 5
