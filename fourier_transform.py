import numpy as np
from manim import *

class TwistingWaves(Scene):
    def construct(self):
        # self.add(NumberPlane(
        #     background_line_style = {
        #         'stroke_width': 0.5,
        #         'stroke_color': GREEN_A
        #     }
        # ))


        t = ValueTracker(3)

        SinWaveAxe = always_redraw (
            lambda : Axes(
                x_range = [0, 4.5, 1/3],
                x_length = 13,
                y_range = [0, 2.5, 1],
                y_length = 2,
                tips = True,
                axis_config = {
                    'tip_width' : 0.2,
                    'tip_height' : 0.25,
                    'include_ticks' : True
                },
                x_axis_config = {
                    'numbers_with_elongated_ticks' : np.arange(1, 100, 1),
                    'include_numbers' : True,
                    'numbers_to_include' : np.arange(0, 100, 1),
                    'decimal_number_config' : {
                        'num_decimal_places' : 0
                    },
                }
            ).shift(UP * 2.25)
        )

        TargetSinWave = VGroup()
        TargetSinWave += always_redraw (
                lambda : SinWaveAxe.plot(
                    lambda x : np.cos(6 * PI * x) + 1
            )
        )
        self.play(Create(SinWaveAxe), run_time = 1.5)
        self.wait(3)
        self.play(Write(TargetSinWave), run_time = 1)
        self.wait(2)
        WindingGraph = NumberPlane(
            x_range = [-2.2, 2.2, 1],
            y_range = [-2.2, 2.2, 1],
            x_length = 4,
            y_length = 4,
            background_line_style = {
                'stroke_width': 1,
                'stroke_color': GREEN_C
            },
            faded_line_ratio = 2,
            faded_line_style = {
                'stroke_width': 0.2
            }
        ).shift(LEFT * 4.5 + DOWN * 1.5)
        self.play(Create(WindingGraph), run_time = 1.5)


        self.play(t.animate.set_value(4.5), run_time = 3)

