from manim import *
import numpy as np

class test(Scene) :
    def construct(self):

        box = Rectangle(stroke_color = GREEN_C, stroke_opacity = 0.7,
                        fill_color = RED_B, fill_opacity = 0.5,
                        height = 2, width = 1)

        self.add(box)
        self.wait(2)
        self.play(box.animate(run_time = 2).shift(2 * UP + 3 * LEFT))
        self.wait(2)

class oxy(Scene) :
    def construct(self):

        axes = Axes(x_range = [-3, 3, 1], y_range = [-3, 3, 1],
                    x_length = 6, y_length = 6).to_edge(LEFT, buff = 0.5)
        square = Square(stroke_color = RED_C, stroke_width = 3).to_edge(RIGHT, buff = 3)
        text_in_square = MathTex("\\dfrac{1}{x}").set_color_by_gradient(BLUE, GREEN).set_height(1.5)

        text_in_square.add_updater(lambda x : x.move_to(square.get_center()))

        self.wait(1)
        self.play(Write(axes), Create(square), run_time = 1)
        self.wait(1)
        self.play(Write(text_in_square))
        self.wait(1)
        self.play(Swap(axes, square))
        self.wait(1)

class UnwrappingCircle(Scene) :
    def construct(self):
        r = ValueTracker(0.5)
        r_value = always_redraw(lambda : DecimalNumber(r.get_value(), 2))
        circle = always_redraw(lambda :
            Circle(radius = r.get_value(), stroke_color = YELLOW, stroke_width = 2)
        )

        self.wait(0.5)
        self.play(Create(circle), Write(r_value), run_time = 1)
        self.wait(0.5)
        self.play(r.animate().set_value(3), run_time = 1)
        self.wait(0.5)
        self.play(r.animate().set_value(1), run_time = 1)
        self.wait(1)

        half_left_circ = ImplicitFunction(
            lambda x, y: (x * x + y * y - 1),
            x_range=[-2, 0],
            color=YELLOW
        )
        half_right_circ = ImplicitFunction(
            lambda x, y: (x * x + y * y - 1),
            x_range=[0, 2],
            color=YELLOW
        )
        self.add(half_left_circ, half_right_circ)
        self.remove(circle)

        half_left_line = (Line(color = YELLOW, stroke_width = 2)
            .set_length(r.get_value() * PI)
            .shift(r.get_value() * PI / 2 * LEFT + 1.5 * DOWN))
        half_right_line = (Line(color=YELLOW, stroke_width=2)
            .set_length(r.get_value() * PI)
            .shift(r.get_value() * PI / 2 * RIGHT + 1.5 * DOWN))

        self.play(Transform(half_left_circ, half_left_line), Transform(half_right_circ, half_right_line))

        self.wait(1)

class WigglingSinWave(Scene) :
    def construct(self):
        # self.add(NumberPlane())
        self.wait(1)

        ax = Axes(
            x_range = [0, 6, 1],
            y_range = [-1.5, 1.5, 1],
            tips = True,
            axis_config = {"include_numbers": True}
        )
        ax.scale(0.5).shift((ORIGIN - ax.c2p(0, 0, 0)) * RIGHT)
        # self.play(Write(ax), run_time = 1.5)

        alpha = ValueTracker(0)
        sin_func = always_redraw(
            lambda : ax.plot(
                lambda t : np.sin(t + alpha.get_value()),
                x_range = [-0.01, 6],
                color = YELLOW
            ),
        )

        circle = Circle(radius = 1, stroke_width = 1.5, color = WHITE).shift(LEFT * 3.5)
        circ_cent = Dot(circle.get_center(), color = RED, radius = 0.05)
        circ_dot = always_redraw(
            lambda : Dot(point = circle.point_at_angle(alpha.get_value()),
                         radius = 0.05,
                         color = RED
            )
        )
        fixed_circ_dot = Dot(point = circle.get_center(), color = RED, radius = 0.05).shift(RIGHT)
        circ_radius = Line(circ_cent, circ_dot, color = RED)

        rotating_radius = always_redraw(
            lambda : Line(start = [0, 0, 0], end = [1, 0, 0],
                          color = TEAL, stroke_width = 2).set_angle(alpha.get_value())
                        .shift(3.5 * LEFT)
        )

        dashed_line = always_redraw(
            lambda : DashedLine(
                start = circ_dot,
                end = ax.c2p(0, np.sin(alpha.get_value())),
                stroke_width = 1.5
            )
        )

        angle_curve = always_redraw (
            lambda : Angle(
                circ_radius,
                rotating_radius,
                quadrant = (1, 1),
                color = WHITE
            )
        )

        # graph_dot = always_redraw(
        #     lambda : Dot(dashed_line.get_end(), color = RED, radius = 0.08)
        # )

        def move_dot(dot) :
            dot.move_to(dashed_line.get_end())

        graph_dot = Dot(color = RED, radius = 0.08).move_to(sin_func.get_start())
        graph_dot.add_updater(move_dot)

        radian_text = VGroup()
        alpha_str = MathTex(r"\alpha = ")
        alpha_value = always_redraw(
            lambda : DecimalNumber(alpha.get_value() % TAU, 2).next_to(alpha_str, RIGHT)
        )

        radian_text.add(alpha_str, alpha_value)
        radian_text.next_to(circle, DOWN * 1.5)

        self.play(Write(ax), run_time = 3)
        self.wait(0.5)
        self.play(Create(circle), Create(circ_cent), run_time = 3, lag_ratio = 0)
        self.wait(0.5)
        self.play(Create(rotating_radius), Create(circ_radius), Create(circ_dot), run_time = 1.5)
        self.add(angle_curve, fixed_circ_dot)
        self.wait(0.5)
        self.play(Create(dashed_line), Create(graph_dot), Write(sin_func), Write(radian_text), run_time = 1.5, rate_func = smooth)
        self.wait(1)
        self.play(alpha.animate.set_value(2.5 * PI), run_time = 6.5, rate_func = smoothstep, lag_ratio = 0)
        self.wait(2)

class test(Scene) :
    def construct(self):
        plane = NumberPlane()
        plane.get_graph()