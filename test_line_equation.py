# test line_equation
import pytest
@pytest.mark.parametrize("a, b, c, d", [
    [(0, 2), (-3, 0), 3, 4],
    [(3, 0), (0,3), -1, 4]
    ])
def test_line_equation(a, b, c, d):
    from line_equation import line_equation
    answer = line_equation(a, b, c)
    assert answer == d
