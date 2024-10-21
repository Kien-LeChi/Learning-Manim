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
            Circle(radius = r.get_value(), stroke_color = YELLOW, stroke_width = 2))

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

        ax = Axes(
            x_range = [-6, 6, 1],
            y_range = [-3, 3, 1],
            tips = True,
            axis_config = {"include_numbers": True}
        )
        self.add(ax)

        x = ValueTracker(0)
        sin_func = always_redraw(
            lambda : ImplicitFunction(
                lambda t, y : y - np.sin(t + x.get_value()),
                x_range = [0, 10]
            )
        )
        self.add(sin_func)
        self.play(x.animate.set_value(12 * PI), run_time = 5, rate_func = linear)