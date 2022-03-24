from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class TestPS4(SpecialThreeDScene):
    CONFIG = {
        # "background_image": 'my_projects\\resource\\png_files\\screen_test.png',
        "default_angled_camera_position": {
            "phi": 56 * DEGREES,
            "theta": -56 * DEGREES,
            'gamma': 0.0 * DEGREES,
            "distance": 80,
        },
        'camera_config': {'background_color': WHITE},
        "three_d_axes_config": {
            "num_axis_pieces": 1,
            "number_line_config": {
                'color': BLACK,
                "unit_size": 2,
                "tick_frequency": 1,
                "numbers_with_elongated_ticks": [0, 1, 2],
                "stroke_width": 2,
            }
        },
    }
    def construct(self):
# object
        axis_config={
            "stroke_color": BLACK,
            "stroke_width": 2,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
            'decimal_number_config': {'color': BLACK},
        }
        # self.camera.init_background()

        # image_bg = ImageMobject(self.background_image)
        #
        # image_bg.rotate(PI/2).rotate(self.default_angled_camera_position['phi'], UP).rotate(self.default_angled_camera_position['theta'], OUT)
        # image_bg.scale(4.2)
        # self.add(image_bg)
        axes_origin = DOWN * 1.6 + RIGHT * 1.6
        axes_scale = 1
        axes = self.get_axes().scale(axes_scale, about_point=ORIGIN).shift(axes_origin)
        cp = ComplexPlane(axis_config=axis_config).scale(2*axes_scale, about_point=ORIGIN).shift(axes_origin)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6)
        cp.add_coordinates(1j, 2j, 3j, 4j, -1j, -2j, -3j, -4j)


        self.set_camera_to_default_position()

        r = axes.c2p(1, 0, 0)[0] - cp.c2p(0, 0, 0)[0]
        w = 1
        surface_func = lambda u, v: np.array([np.cos(w * u) * v * r, np.sin(w * u) * v * r, u * w / PI * 2])
        u_num = 480 / 10
        surface = ParametricSurface(surface_func, u_min=0, u_max=2 * PI, v_min=0.001, v_max=1, resolution=(144, 4),
                                    color=ORANGE, checkerboard_colors=None, stroke_color=ORANGE, stroke_opacity=0.6,
                                    stroke_width=1.5, fill_color=BLUE, fill_opacity=0.25).shift(axes_origin)
# position

# show
        self.add(axes)
        self.play(ShowCreation(surface))

