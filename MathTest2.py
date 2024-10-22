from manim import *
import numpy as np

class CoordSys(Scene) :
    def construct(self):
        self.wait(1)
        grid = Axes (
            x_range = [-2, 6, 0.5],
            y_range = [-1, 4, 0.5],
            x_length = 9,
            y_length = 5,
            axis_config = {
                "include_numbers": True,
                "numbers_to_include": np.arange(-3, 7, 1),
                "font_size": 24
            },
            tips = True,
        )
        self.play(Create(grid), run_time = 1.5)
        self.wait(1)
        graphs = VGroup()
        for n in np.arange(1, 20 + 0.5, 0.5) :
            graphs += grid.plot(lambda x : x * n, color = YELLOW)

        self.play(Create(graphs), run_time = 1.5)

        self.wait(1)

class CoordSysExample(Scene):
    def construct(self):
        # the location of the ticks depends on the x_range and y_range.
        grid = Axes(
            x_range=[0, 1, 0.05],  # step size determines num_decimal_places.
            y_range=[0, 1, 0.05],
            x_length=9,
            y_length=5.5,
            axis_config={
                "numbers_to_include": np.arange(0, 1 + 0.1, 0.1),
                "font_size": 24,
            },
            tips=False,
        )

        # Labels for the x-axis and y-axis.
        y_label = grid.get_y_axis_label("y", edge=LEFT, direction=LEFT, buff=0.4)
        x_label = grid.get_x_axis_label("x")
        grid_labels = VGroup(x_label, y_label)

        graphs = VGroup()
        for n in np.arange(1, 20 + 0.5, 0.5):
            graphs += grid.plot(lambda x: x ** n, color=WHITE)
            graphs += grid.plot(
                lambda x: x ** (1 / n), color=WHITE, use_smoothing=False
            )

        # Extra lines and labels for point (1,1)
        graphs += grid.get_horizontal_line(grid.c2p(1, 1, 0), color=BLUE)
        graphs += grid.get_vertical_line(grid.c2p(1, 1, 0), color=BLUE)
        graphs += Dot(point=grid.c2p(1, 1, 0), color=YELLOW)
        graphs += Tex("(1,1)").scale(0.75).next_to(grid.c2p(1, 1, 0))

        title = Title(
            # spaces between braces to prevent SyntaxError
            r"Graphs of $y=x^{ {1}\over{n} }$ and $y=x^n (n=1,2,3,...,20)$",
            include_underline=False,
            font_size=40,
        )

        self.add(title, graphs, grid, grid_labels)