from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class threeleaf(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 80 * DEGREES,
            "theta": -45 * DEGREES,
            "distance": 100,
        },
        'camera_config': {'background_color': WHITE},
    }

    def construct(self):
        self.set_camera_to_default_position()
        axes = ThreeDAxes()

        self.add(axes)
        R, r = 3.2, 0.2
        three_surface = ParametricSurface(lambda u, v: R * np.array([np.sin(u), np.cos(u), 0])
                                                        + v * np.array([2*np.sin(2*u), -2*np.cos(2*u), 0])
                                                        + v * -1*np.sin(3*u) * OUT,
                                           u_min=0, u_max=2 * TAU, v_min=-r, v_max=r, resolution=(80, 16),
                                           checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.6,
                                           stroke_width=1.2, fill_color=BLUE, fill_opacity=0.8)

        three_edge = ParametricFunction(lambda t: R * np.array([np.sin(t)+np.sin(2*t), np.cos(t)-2*np.cos(2*t), -1*np.sin(3*t)])
                                         ,t_min=0, t_max=2 * TAU, color=RED, stroke_width=10, stroke_opacity=0.5)

        self.play(ShowCreation(three_surface), run_time=3)
        self.play(ShowCreation(three_edge), run_time=3)
        self.wait(1)
