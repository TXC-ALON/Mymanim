from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class testAngle(Scene):
    CONFIG = {
        'radius': 1,
        'color': RED,
        'opacity': 0.4,
        'stroke_width': 10,
        # 'below_180': True,
    }
    def construct(self):
        # object
        A = np.array([2, 3, 4])
        O = np.array([0, 0, 0])
        B = np.array([-1, 2, 8])
        OA, OB = A - O, B - O
        theta = np.angle(complex(*OA[:2]) / complex(*OB[:2]))  # angle of OB to OA 复数除法都忘了。。太菜了。
        point_O = Dot().move_to(O)
        line_OA = Line(O, A)
        line_OB = Line(O, B)
        Arc_small = Arc(start_angle=Line(O, B).get_angle(), angle=theta, radius=self.radius/2,
                        stroke_width=self.stroke_width, color=GREEN)
        Arc_large = Arc(start_angle=Line(O, B).get_angle(), angle=theta, radius=self.radius,
                        stroke_width=self.stroke_width, color=self.color)
        Arc_group = VGroup(point_O, line_OA, line_OB, Arc_small, Arc_large)
        self.add(Arc_group)
        debugPoints(self,Arc_group[3])

class Rotate_outof_screen4(SpecialThreeDScene):

    CONFIG = {
        "background_image": 'logo.png',
        "default_angled_camera_position": {
            "phi": 80 * DEGREES,
            "theta": 10 * DEGREES,
            'gamma': 0.0 * DEGREES,
            "distance": 1000,
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
        }
        # self.camera.init_background()

        image_bg = ImageMobject(self.background_image)

        image_bg.rotate(PI/2).rotate(self.default_angled_camera_position['phi'], UP).rotate(self.default_angled_camera_position['theta'], OUT)
        image_bg.scale(2)
        self.add(image_bg)
        axes_origin = OUT * 0.75 + UP * 0.5
        axes_scale = 0.35
        axes = self.get_axes().scale(axes_scale).shift(axes_origin)
        self.set_camera_to_default_position()

        cp_scale = 2
        cp = ComplexPlane(axis_config=axis_config).scale(cp_scale*axes_scale)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6)
        cp.add_coordinates(1j, 2j, 3j, -1j, -2j, -3j)
        cp.rotate(PI/2).rotate(PI/2, UP).shift(axes_origin)

        # self.add(axes)

        r_vect = Arrow(axes.c2p(0, 0, 0), axes.c2p(0, 1, 0), buff=0, color=RED).rotate(PI/2, UP)
        i_vect = Arrow(axes.c2p(0, 0, 0), axes.c2p(0, 1, 0), buff=0, color=YELLOW).rotate(PI/2, UP).rotate(PI/2, RIGHT, about_point=ORIGIN)

        r = axes.c2p(1, 0, 0)[0] - axes.c2p(0, 0, 0)[0]
        w = 2.5
        t_max = 4 / w * TAU

        # unit_circle = Circle(radius=r, color=ORANGE).rotate(PI/2, UP).shift(axes_origin)

        curve_3d = ParametricFunction(lambda t: (np.cos(w * t) * UP + np.sin(w*t) * OUT) * r + t * RIGHT, color=RED,
                                      t_min=0, t_max=t_max, stroke_width=5).set_stroke(color=ORANGE, opacity=0.8).shift(axes_origin)

        surface_func = lambda u, v: np.array([u, np.cos(w * u) * v * r, np.sin(w * u) * v * r])
        u_num = 80
        surface = ParametricSurface(surface_func, u_min=0, u_max=t_max, v_min=0.001, v_max=1., resolution=(u_num, 8),
                                    color=ORANGE, checkerboard_colors=None, stroke_color=BLACK, stroke_opacity=0.6,
                                    stroke_width=1.2, fill_color=BLUE, fill_opacity=0.4).shift(axes_origin)
        # surface.set_depth(2)
        # surface_02 = self.get_surface(axes, lambda u, v: np.array([u, np.cos(w * u) * v, np.sin(w * u) * v]),
        #                               u_min=0, u_max=t_max, v_min=0.001, v_max=1., resolution=(50, 10))
        colors = color_gradient([RED, BLUE], u_num)
        for face in surface:
            face.set_fill(colors[face.u_index], opacity=0.75)

        self.play(ShowCreation(cp))
        # self.play(ShowCreation(r_vect))
        # self.play(ShowCreation(i_vect))
        # self.play(ShowCreation(unit_circle))
        self.wait()
        self.play(ShowCreation(curve_3d))
        self.wait()
        self.play(ShowCreation(surface))

        self.wait(4)

class Dot2D(Scene):
    def construct(self):
        dot_01 = Dot(ORIGIN, color=BLUE).set_height(0.5)
        self.add(dot_01)
        num=8
        dot = VGroup()
        for i in range(1, num):
            dot_i = dot_01.copy().rotate(PI * i/num, axis=UP).shift(LEFT*3*i/num).set_color(RED)
            dot.add(dot_i)
        for i in range(1, num):
            dot_i = dot_01.copy().rotate(PI * i/num, axis=RIGHT).shift(RIGHT*3*i/num).set_color(PINK)
            dot.add(dot_i)
        self.add(dot)

class Dot3d(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-20 * DEGREES)
        dot_01 = Dot(ORIGIN, color=BLUE).set_height(0.5)
        self.add(dot_01)
        num=8
        dot = VGroup()
        for i in range(1, num):
            dot_i = dot_01.copy().rotate(PI * i/num, axis=UP).shift(LEFT*3*i/num).set_color(RED)
            dot.add(dot_i)
        for i in range(1, num):
            dot_i = dot_01.copy().rotate(PI * i/num, axis=RIGHT).shift(RIGHT*3*i/num).set_color(PINK)
            dot.add(dot_i)
        self.add(dot)


class Dot3d(VGroup):

    def __init__(self, loc=ORIGIN, size=0.2, color=WHITE, **kwargs):
        VGroup.__init__(self, **kwargs)
        dot_01 = Dot(loc, color=color).set_height(size)
        self.add(dot_01)
        num=8
        for i in range(1, num):
            dot_i = dot_01.copy().rotate(PI * i/num, axis=UP)
            self.add(dot_i)
        for i in range(1, num):
            dot_i = dot_01.copy().rotate(PI * i/num, axis=RIGHT)
            self.add(dot_i)

class Part_3_7(SpecialThreeDScene):

    CONFIG = {
    # "background_image": 'my_projects\\resource\\png_files\\screen_test.png',
    "default_angled_camera_position": {
        "phi": 56 * DEGREES,
        "theta": -56 * DEGREES,
        'gamma': 0.0 * DEGREES,
        "distance": 200,
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
        # self.camera.init_background()

        # image_bg = ImageMobject(self.background_image)
        #
        # image_bg.rotate(PI/2).rotate(self.default_angled_camera_position['phi'], UP).rotate(self.default_angled_camera_position['theta'], OUT)
        # image_bg.scale(4.2)
        # self.add(image_bg)
        axes_origin = DOWN * 1.6 + RIGHT * 1.6
        axes_scale = 1
        axes = self.get_axes().scale(axes_scale, about_point=ORIGIN).shift(axes_origin)

        self.set_camera_to_default_position()

        cp_scale = 2
        cp = ComplexPlane(axis_config=axis_config).scale(cp_scale*axes_scale, about_point=ORIGIN).shift(axes_origin)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6)
        cp.add_coordinates(1j, 2j, 3j, 4j, -1j, -2j, -3j, -4j)

        ##
        arrow = Line(cp.n2p(0), cp.n2p(1), buff=0, color=ORANGE, stroke_width=8)
        dot = Dot3d(color=RED, size=0.25).add_updater(lambda d: d.move_to(arrow.get_end()))
        #dot = Dot(color=RED, size=0.25).add_updater(lambda d: d.move_to(arrow.get_end()))
        self.delta_t = 0 * 1 / 60
        self.w = 0
        # arrow.add_updater(lambda a, dt: a.shift((axes.c2p(0,0,0) - a.get_start()) * np.array([1,1,0])).rotate(self.w, axis=OUT, about_point=a.get_start()).shift((axes.c2p(0, 0, 1)-axes.c2p(0,0,0)) * self.delta_t))
        arrow.add_updater(lambda a, dt: a.rotate(self.w, axis=OUT, about_point=a.get_start()).shift(
            (axes.c2p(0, 0, 1) - axes.c2p(0, 0, 0)) * self.delta_t))
        line_group = VGroup()
        self.t_num = 0

        def update_line(g):
            self.t_num += 1 * int(np.sign(self.w) % 2)
            if self.t_num % 3 == 0:
                g.add(Line(arrow.get_start(), arrow.get_end(), stroke_width=2, stroke_color=ORANGE))

        curve_3d = VGroup()
        self.p_old = dot.get_center()

        def update_curve(g):
            if not self.w == 0:
                p_new = dot.get_center()
                g.add(Line(self.p_old, p_new, stroke_width=5, stroke_color=ORANGE))
                self.p_old = p_new

        curve_3d.add_updater(update_curve)
        line_group.add_updater(update_line)

        r = axes.c2p(1, 0, 0)[0] - cp.c2p(0, 0, 0)[0]
        w = 4
        surface_func = lambda u, v: np.array([np.cos(w * u) * v * r, np.sin(w * u) * v * r, 1/4*u * w / PI * 2])
        u_num = 144
        surface = ParametricSurface(surface_func, u_min=0, u_max=2 * PI, v_min=0.001, v_max=1, resolution=(u_num, 8),
                                    color=ORANGE, checkerboard_colors=None, stroke_color=ORANGE, stroke_opacity=0.6,
                                    stroke_width=1.5, fill_color=BLUE, fill_opacity=0.25).shift(axes_origin)

        self.add(axes)
        self.play(ShowCreation(cp), run_time=1.2)
        self.wait()
        self.play(ShowCreation(arrow), FadeIn(dot))
        self.wait(2)
        self.add(line_group, curve_3d)
        self.start_rotate()
        self.wait(8)
        self.stop_rotate()
        self.wait()
        self.play(ReplacementTransform(line_group, surface), run_time=2.5)
        self.wait(4)

    def start_rotate(self, delta_t=1/120, w=TAU/60):#因为一秒30帧。所以一秒可以转30*360/60 180度
        self.delta_t = delta_t
        self.w = w

    def stop_rotate(self):
        self.delta_t = 0 * 1/60
        self.w = 0