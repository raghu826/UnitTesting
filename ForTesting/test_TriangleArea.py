import unittest
import TriangleArea


def test_tri_area():
    area = TriangleArea.tri_area(10, 20)
    assert area == 100.0


