import pytest
import geometry


def test_circle_area():
    result = geometry.Circle(1).area()
    assert pytest.approx(result, 0.01) == 3.1415


def test_triangle_area():
    result = geometry.Triangle(3, 4, 5).area()
    assert pytest.approx(result, 0.01) == 6.0


def test_triangle_right_angle():
    result = geometry.Triangle(3, 4, 5).is_right_angled()
    assert result is True


def test_invalid_circle():
    with pytest.raises(ValueError):
        geometry.Circle(0).area()


def test_invalid_triangle():
    with pytest.raises(ValueError):
        geometry.Triangle(1, 2, 10).area()
