from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L
class Part_4(SpecialThreeDScene):

    CONFIG = {
    # "background_image": 'my_projects\\resource\\png_files\\screen_test.png',
    "default_angled_camera_position": {
        "phi": 66 * DEGREES,
        "theta": -60 * DEGREES,
        'gamma': 0.0 * DEGREES,
        "distance": 50,
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

        axes_origin = ORIGIN
        axes_scale = 1.2
        axes = self.get_axes().scale(axes_scale, about_point=ORIGIN).shift(axes_origin)

        self.set_camera_to_default_position()

        cp_scale = 2
        cp = ComplexPlane(axis_config=axis_config).scale(cp_scale*axes_scale, about_point=ORIGIN).shift(axes_origin)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6)
        cp.add_coordinates(1j, 2j, 3j, 4j, -1j, -2j, -3j, -4j)

        ##
        l = axes_scale

        r = cp.n2p(1)[0]/2  #实际上就是半格
        dot2 = Dot3d(color=PURPLE, size=0.18).move_to(cp.n2p(1))
        self.add(axes,cp)
        self.add(dot2)
        circle = Circle(radius=r).rotate(PI/2, UP).shift(axes.c2p(-2, 0, 0))
        line_r = Line(circle.get_center(), circle.get_center() + UP * r, color=ORANGE, stroke_width=6)
        dot = Dot3d(color=RED, size=0.18).add_updater(lambda d: d.move_to(line_r.get_end()))
        #cube0 = Cube(color=PINK, fill_opacity=0.0, stroke_width=4, stroke_color=YELLOW).scale(np.array([l * 2, l/2, l/2]))
        #cube = Cube(color=BLUE, fill_opacity=0.0, stroke_width=4, stroke_color=BLUE_D).scale(np.array([l * 4, l, l]))#这样就是显示在画面中间变大
        #self.add(cube0,cube)
        w = TAU/2
        curve_3d = ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t), r * np.sin(w * t)]), t_min=-0.0001,
                                      t_max=8,
                                      color=ORANGE, stroke_width=4).shift(cp.n2p(-2)) #这是一个以t为updater的
        curve_3d.add_updater(lambda c: c.become(ParametricFunction
                                                (lambda t: np.array([t * r, r * np.cos(w * t), r * np.sin(w * t)]),
                                                 t_min=-0.00001,
                                                 t_max=(cp.p2n(circle.get_center()).real + 2) * 2,
                                                 color=PINK, stroke_width=4).shift(cp.n2p(-2))))#这是一个以circle为updater的
        line_r.add_updater(lambda l: l.become(Line(circle.get_center(), circle.get_center() +
                                                   UP * r * np.cos((cp.p2n(circle.get_center()).real + 2) * 2 * w) +
                                                   OUT * r * np.sin((cp.p2n(circle.get_center()).real + 2) * 2 * w),
                                                   color=ORANGE, stroke_width=6)))

        cos_t = ParametricFunction(lambda t: np.array([t * r, r * np.cos(w * t), 0]), t_min=-0.0001, t_max=8,
                                   color=GREEN, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(OUT * r * (1 + 1.45))
        sin_t = ParametricFunction(lambda t: np.array([t * r, 0, r * np.sin(w * t)]), t_min=-0.0001, t_max=8,
                                   color=PINK, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(DOWN * r * (1 + 2))
        self.add(curve_3d,line_r,cos_t,sin_t)
        self.play(circle.shift, axes.c2p(4, 0, 0), run_time=6)