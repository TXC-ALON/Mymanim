from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L
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

        r = cp.n2p(1)[0]/2

        circle = Circle(radius=r).rotate(PI/2, UP).shift(axes.c2p(-2, 0, 0))
        line_r = Line(circle.get_center(), circle.get_center() + UP * r, color=ORANGE, stroke_width=6)
        dot = Dot3d(color=RED, size=0.18).add_updater(lambda d: d.move_to(line_r.get_end()))

        cube = Cube(color=BLUE, fill_opacity=0.0, stroke_width=4, stroke_color=BLUE_D).scale(np.array([l * 4, l, l]))
        self.add(cube)
        w = TAU/2
        curve_3d = ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t), r * np.sin(w * t)]), t_min=-0.0001,
                                      t_max=8,
                                      color=ORANGE, stroke_width=4).shift(cp.n2p(-2))

        curve_3d.add_updater(lambda c: c.become(ParametricFunction
                                     (lambda t: np.array([t*r, r * np.cos(w * t), r * np.sin(w * t)]),t_min=-0.00001,
                                      t_max=(cp.p2n(circle.get_center()).real+2)*2,
                                      color=ORANGE, stroke_width=4).shift(cp.n2p(-2))))
        # line_r.add_updater(lambda l: l.put_start_and_end_on(circle.get_center(), circle.get_center() +
        #                                                     UP * r * np.cos((cp.p2n(circle.get_center()).real+2)*2*w) +
        #                                                     OUT * (-r) * np.sin((cp.p2n(circle.get_center()).real+2)*2*w)))
        line_r.add_updater(lambda l: l.become(Line(circle.get_center(), circle.get_center() +
                                                   UP * r * np.cos((cp.p2n(circle.get_center()).real+2)*2*w) +
                                                   OUT * r * np.sin((cp.p2n(circle.get_center()).real+2)*2*w),
                                                   color=ORANGE, stroke_width=6)))

        cos_t = ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t), 0]), t_min=-0.0001, t_max=8,
                                      color=GREEN, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(OUT*r*(1+1.45))
        sin_t = ParametricFunction(lambda t: np.array([t*r, 0, r * np.sin(w * t)]), t_min=-0.0001, t_max=8,
                                      color=PINK, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(DOWN*r*(1+2))

        cube_g = VGroup()
        A = axes.c2p(-2, -0.5, 0.5)
        B = axes.c2p(-2, 0.5, 0.5)
        C = axes.c2p(-2, 0.5, -0.5)
        D = axes.c2p(-2, -0.5, -0.5)
        E = axes.c2p(2, -0.5, 0.5)
        F = axes.c2p(2, 0.5, 0.5)
        G = axes.c2p(2, 0.5, -0.5)
        H = axes.c2p(2, -0.5, -0.5)
        line_color = BLUE
        s_width = 2

        AB = Line(A, B, color=line_color, stroke_width=s_width)
        BC = DashedLine(C, B, color=line_color, stroke_width=s_width)
        CD = DashedLine(C, D, color=line_color, stroke_width=s_width)
        DA = Line(A, D, color=line_color, stroke_width=s_width)

        AE = Line(A, E, color=line_color, stroke_width=s_width)
        BF = Line(F, B, color=line_color, stroke_width=s_width)
        CG = DashedLine(C, G, color=line_color, stroke_width=s_width)
        DH = Line(H, D, color=line_color, stroke_width=s_width)

        EF = Line(E, F, color=line_color, stroke_width=s_width)
        FG = Line(F, G, color=line_color, stroke_width=s_width)
        GH = Line(G, H, color=line_color, stroke_width=s_width)
        HE = Line(H, E, color=line_color, stroke_width=s_width)

        cube_g.add(AB, BC, CD, DA, AE, BF, CG, DH, EF, FG, GH, HE)

        y_dash = VGroup(DashedLine((A+D)/2, (E+H)/2, color=line_color, stroke_width=s_width*0.75))
        for i in range(1, 16):
            y_dash.add(DashedLine(A + i * (E-A)/16, D + i * (E-A)/16, color=line_color, stroke_width=s_width*0.75))
        yt = VGroup(DA.copy(), AE.copy(), HE.copy(), DH.copy(), y_dash)

        x_dash = VGroup(DashedLine((A+B)/2, (E+F)/2, color=line_color, stroke_width=s_width*0.75))
        for i in range(1, 16):
            x_dash.add(DashedLine(A + i * (E-A)/16, B + i * (E-A)/16, color=line_color, stroke_width=s_width*0.75))
        xt = VGroup(AB.copy(), BF.copy(), EF.copy(), AE.copy(), x_dash)

        color_dict = {'e': GREEN, 'i': YELLOW_D, 't': BLUE, '\\omega': RED, '\\varphi': ORANGE, '\\sin': PINK, '\\cos': GREEN}

        text_eiwt = TexMobject('\\mathbf{e^{', 'i', '(', '\\omega', 't', '+', '\\varphi', ')}}', background_stroke_color=WHITE, color=BLACK).set_color_by_tex_to_color_map(color_dict)
        text_sint = TexMobject('\\mathbf{\\sin{', '(', '\\omega', 't', '+', '\\varphi', ')}}', background_stroke_color=WHITE, color=BLACK).set_color_by_tex_to_color_map(color_dict)
        text_cost = TexMobject('\\mathbf{\\cos{', '(', '\\omega', 't', '+', '\\varphi', ')}}', background_stroke_color=WHITE, color=BLACK).set_color_by_tex_to_color_map(color_dict)
        text_eiwt.scale(1.25).rotate(PI/2, RIGHT).shift(axes.c2p(2.75, 0, 0)).shift(OUT*0.4 + LEFT * 0.2)
        text_sint.scale(1.25).rotate(PI/2, RIGHT).shift(axes.c2p(2.75, 0, 0)).shift(DOWN*r*(1+2))
        text_cost.scale(1.2).rotate(PI/2, RIGHT).shift(axes.c2p(2.75, 0, 0)).shift(OUT*r*(1+1.45)+LEFT*0.75*r+DOWN*0.4*r)

        navi_cube = Cube(stroke_color=ORANGE, stroke_width=0.6, fill_color=ORANGE, fill_opacity=0.2).scale(0.1)
        l_cube = navi_cube.get_height()
        navi_cube.shift(l_cube/2)
        l_x = Line(ORIGIN, l_cube * UP * 4, color=GREEN)
        l_y = Line(ORIGIN, l_cube * OUT * 4, color=PINK)
        l_t = Line(ORIGIN, l_cube * RIGHT * 4, color=ORANGE)
        tex_x = TexMobject('x', background_stroke_color=WHITE, color=GREEN).rotate(PI/2, RIGHT).next_to(l_x, UP*1.25)
        tex_y = TexMobject('y', background_stroke_color=WHITE, color=PINK).rotate(PI/2, RIGHT).next_to(l_y, OUT*0.5)
        tex_t = TexMobject('t', background_stroke_color=WHITE, color=ORANGE).rotate(PI/2, RIGHT).next_to(l_t, RIGHT*0.5)
        navi_group = VGroup(l_x, l_y, l_t, tex_x, tex_y, tex_t, navi_cube).move_to(cp.n2p(-0.6-3.2j))

        ## rotate update ##
        # rotate_group_old = VGroup(curve_3d, line_r, dot)
        # rotate_group = rotate_group_old.deepcopy()
        # def rotate_all(r):
        #     r.rotate(2*DEGREES, RIGHT, about_point=ORIGIN)
        # cos_t.add_updater(lambda c: c.become(ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t + rotate_group[1].get_angle()), 0]), t_min=-0.0001, t_max=8,
        #                               color=GREEN, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(OUT*r*(1+1.45))))
        # sin_t.add_updater(lambda s: s.become(ParametricFunction(lambda t: np.array([t*r, 0, r * np.sin(w * t + rotate_group[1].get_angle())]), t_min=-0.0001, t_max=8,
        #                               color=PINK, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(DOWN*r*(1+2))))

        ## animation ##

        self.add(cp, axes)

        self.add(curve_3d, cube_g, circle, line_r, dot, navi_group)
        self.wait()

        # circle.shift(axes.c2p(4, 0, 0))
        self.play(circle.shift, axes.c2p(4, 0, 0), run_time=6)
        self.play(Write(text_eiwt), run_time=1.5)
        self.wait()
        self.play(yt.shift, DOWN*r*2, run_time=1.5)
        self.wait(0.5)
        self.play(TransformFromCopy(curve_3d, sin_t), run_time=2)
        self.wait(0.4)
        self.play(Write(text_sint), run_time=1.5)
        self.wait()
        self.play(xt.shift, OUT*r*1.45, run_time=1.5)
        self.wait(0.5)
        self.play(TransformFromCopy(curve_3d, cos_t), run_time=2)
        self.wait(0.4)
        self.play(Write(text_cost), run_time=1.5)
        self.wait(4)

