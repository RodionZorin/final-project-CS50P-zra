from project import is_point_in_polygon, get_polygon_square, get_triangle_square, get_test_square
import pytest

def test_is_point_in_polygon_clockwise():
    assert is_point_in_polygon([(0, 0), (0, 2), (2, 5), (4, 5), (4, 0)], 2, 4) == True
    assert is_point_in_polygon([(0, 0), (0, 2), (2, 5), (4, 5), (4, 0)], 0, 3) == False
    assert is_point_in_polygon([(0, 0), (0, 2), (2, 5), (4, 5), (4, 0)], 5, 0) == False

def test_is_point_in_polygon_counterclockwise():
    assert is_point_in_polygon([(0, 0), (4, 0), (4, 5), (2, 5), (0, 2)], 2, 4) == True
    assert is_point_in_polygon([(0, 0), (4, 0), (4, 5), (2, 5), (0, 2)], 0, 3) == False
    assert is_point_in_polygon([(0, 0), (4, 0), (4, 5), (2, 5), (0, 2)], 5, 0) == False

def test_is_point_in_polygon_float():
    assert is_point_in_polygon([(0, 0), (4, 0), (4, 5), (2, 5), (0, 2)], 1.9, 3.8) == True
    assert is_point_in_polygon([(0, 0), (4, 0), (4, 5), (2, 5), (0, 2)], 0, 2.1) == False
    assert is_point_in_polygon([(0, 0), (4, 0), (4, 5), (2, 5), (0, 2)], 4.1, 0) == False

def test_get_polygon_square():
    assert get_polygon_square([(0, 0), (0, 2), (2, 2), (2, 0)], [0, 0, 2, 2], [0, 2, 2, 0]) == 2*2

def test_get_triangle_square():
    polygon_square = get_polygon_square([(0, 0), (0, 2), (2, 2), (2, 0)], [0, 0, 2, 2], [0, 2, 2, 0])
    assert get_triangle_square([0, 0, 2], [0, 2, 0]) == polygon_square/2

def test_get_test_square():
    polygon_square = get_polygon_square([(0, 0), (0, 2), (2, 2), (2, 0)], [0, 0, 2, 2], [0, 2, 2, 0])
    assert get_test_square([(0, 0), (0, 2), (2, 2), (2, 0)], [0, 0, 2, 2], [0, 2, 2, 0], 1, 1) == polygon_square
    assert get_test_square([(0, 0), (0, 2), (2, 2), (2, 0)], [0, 0, 2, 2], [0, 2, 2, 0], 3, 3) != polygon_square
