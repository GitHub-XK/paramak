
import os
import unittest
from pathlib import Path

import pytest

from paramak import SweepMixedShape
from paramak.utils import cut_solid, intersect_solid, union_solid


class test_object_properties(unittest.TestCase):
    def test_solid_constuction(self):
        """checks that a SweepMixedShape solid can be created"""

        test_shape = SweepMixedShape(
            points = [
                (-20, 20, "straight"),
                (0, 20, "spline"),
                (10, 10, "spline"),
                (20, 0, "straight"),
                (0, -20, "straight"),
                (-5, -20, "circle"),
                (-10, -15, "circle"),
                (-5, -10, "straight")
            ],
            path_points = [
                (50, 0),
                (20, 200),
                (50, 400)
            ],
            workplane = "XY",
            path_workplane = "XZ"
        )
        test_shape.create_solid()
        
        assert test_shape.solid is not None

    def test_azimuth_placement_angle(self):
        """creates SweepMixedShape solids with single and multiple azimuth
            placement angles and checks the relative volumes are correct"""

        test_shape_1 = SweepMixedShape(
            points = [
                (-20, 20, "straight"),
                (0, 20, "spline"),
                (10, 10, "spline"),
                (20, 0, "straight"),
                (0, -20, "straight"),
                (-5, -20, "circle"),
                (-10, -15, "circle"),
                (-5, -10, "straight")
            ],
            path_points = [
                (100, 0),
                (50, 200),
                (100, 400)
            ],
            workplane = "XY",
            path_workplane = "XZ"
        )

        test_shape_2 = SweepMixedShape(
            points = [
                (-20, 20, "straight"),
                (0, 20, "spline"),
                (10, 10, "spline"),
                (20, 0, "straight"),
                (0, -20, "straight"),
                (-5, -20, "circle"),
                (-10, -15, "circle"),
                (-5, -10, "straight")
            ],
            path_points = [
                (100, 0),
                (50, 200),
                (100, 400)
            ],
            workplane = "XY",
            path_workplane = "XZ",
            azimuth_placement_angle = [0, 90, 180, 270]
        )

        assert test_shape_2.volume == pytest.approx(test_shape_1.volume * 4)


if __name__ == "__main__":
    unittest.main()