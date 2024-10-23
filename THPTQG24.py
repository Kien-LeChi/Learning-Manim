from manim import *
import numpy as np

class Geometry(ThreeDScene) :
    def construct(self):
        self.set_camera_orientation(phi=2 * PI / 5, theta=PI / 3, gamma = PI / 5)
        ax = ThreeDAxes (
            x_range = [-6, 6, 1],
            y_range = [-6, 6, 1],
            z_range = [-6, 6, 1]
        )
        moving_line = Line(start = ORIGIN, end = [-3, -4, -5], stroke_width = 3, color = TEAL)
        self.play(Create(moving_line), Write(ax))
        self.wait(1)
        self.begin_ambient_camera_rotation(rate = 0.2, about = 'theta')
        self.wait(1)
        self.play(ax.animate.move_to([-3, -4, -5]))


class Camera_angles(ThreeDScene) :
    def construct(self):
        self.set_camera_orientation(phi=2 * PI / 5, theta=PI / 3, gamma=PI / 5)

        edges = VGroup()
        cube = Cube(side_length = 3, fill_opacity = 0.5, color = TEAL)
        edges.add(cube)

        ax = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1]
        )
        self.play(Write(ax), run_time = 2)
        self.wait(1)
        for edge in edges :
            self.play(Create(edge), run_time = 1)
        self.wait(3)