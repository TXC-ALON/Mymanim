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
                                                 color=ORANGE, stroke_width=4).shift(cp.n2p(-2))))#这是一个以circle为updater的
        line_r.add_updater(lambda l: l.become(Line(circle.get_center(), circle.get_center() +
                                                   UP * r * np.cos((cp.p2n(circle.get_center()).real + 2) * 2 * w) +
                                                   OUT * r * np.sin((cp.p2n(circle.get_center()).real + 2) * 2 * w),
                                                   color=ORANGE, stroke_width=6)))

        cos_t = ParametricFunction(lambda t: np.array([t * r, r * np.cos(w * t), 0]), t_min=-0.0001, t_max=8,
                                   color=GREEN, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(OUT * r * (1 + 1.45))
        sin_t = ParametricFunction(lambda t: np.array([t * r, 0, r * np.sin(w * t)]), t_min=-0.0001, t_max=8,
                                   color=PINK, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(DOWN * r * (1 + 2))

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

        y_dash = VGroup(DashedLine((A + D) / 2, (E + H) / 2, color=RED, stroke_width=s_width * 0.75))
        for i in range(1, 16):
            y_dash.add(
                DashedLine(A + i * (E - A) / 16, D + i * (E - A) / 16, color=RED, stroke_width=s_width * 0.75))
        yt = VGroup(DA.copy(), AE.copy(), HE.copy(), DH.copy(), y_dash)

        x_dash = VGroup(DashedLine((A + B) / 2, (E + F) / 2, color=YELLOW, stroke_width=s_width * 0.75))
        for i in range(1, 16):
            x_dash.add(
                DashedLine(A + i * (E - A) / 16, B + i * (E - A) / 16, color=YELLOW, stroke_width=s_width * 0.75))
        xt = VGroup(AB.copy(), BF.copy(), EF.copy(), AE.copy(), x_dash)


        self.add(curve_3d,line_r,cos_t,sin_t)
        self.add(cube_g,y_dash,x_dash)
        #self.play(circle.shift, axes.c2p(4, 0, 0), run_time=6)

class Part_6(Scene):

    CONFIG = {
        'camera_config': {'background_color': WHITE},
    }

    def construct(self):

        color_dict = {'i': RED, '\\theta': BLUE, 'e': GREEN, '\\sin': PINK, '\\cos': GREEN, '\\varphi': YELLOW, 't': BLUE_D, '\\omega': RED}

        formula = TexMobject('\\mathbf{e', '^{i', '\\theta', '}=', '\\cos{', '\\theta', '}+', 'i', '\\sin', '{\\theta}}',
                             color=BLACK, background_stroke_color=BLACK, background_stroke_width=3).set_height(1.)

        formula.set_color_by_tex_to_color_map({'i': RED, '\\theta': BLUE, 'e': GREEN, '\\sin': PINK, '\\cos': GREEN}).shift(DOWN * 1.8)
        formula[2].set_color(BLUE)
        formula[5].set_color(BLUE)
        formula[-1].set_color(BLUE)

        arrow_x = Arrow(LEFT * 2.35, RIGHT * 2.6, color=GRAY, buff=0, max_tip_length_to_length_ratio=0.05)
        arrow_y = Arrow(DOWN * 2.35, UP * 2.6, color=GRAY, buff=0, max_tip_length_to_length_ratio=0.05)
        circle = Circle(color=RED_D, stroke_width=8).scale(2)
        group_1 = VGroup(arrow_x, arrow_y, circle).shift(UP * 1.2)

        dot_o = Dot(ORIGIN, color=GRAY).set_height(0.2)
        dot_p = Dot(np.sqrt(3) * RIGHT + UP, color=BLUE).set_height(0.25)
        arrow = Arrow(dot_o.get_center(), dot_p.get_center(), color=RED_D, stroke_width=8)
        line_2 = Line(dot_o.get_center(), dot_p.get_center()*RIGHT + RIGHT * 0.035, color=YELLOW_D, stroke_width=10)
        line_3 = Line(dot_p.get_center()*RIGHT + DOWN * 0.035, dot_p.get_center(), color=YELLOW_D, stroke_width=10)
        group_2 = VGroup(arrow, line_2, line_3, dot_o, dot_p).shift(UP * 1.2)

        tex_i_1 = TexMobject('\\mathbf{i}', color=ORANGE, background_stroke_color=ORANGE, background_stroke_width=1.6).scale(0.8)
        tex_i_2 = TexMobject('\\mathbf{-i}', color=ORANGE, background_stroke_color=ORANGE, background_stroke_width=1.6).scale(0.8)
        tex_i_1.shift(UP * 2.2 + RIGHT * 0.275)
        tex_i_2.shift(DOWN * 2.2 + RIGHT * 0.275)

        tex_1_1 = TexMobject('\\mathbf{1}', color=WHITE, background_stroke_color=WHITE, background_stroke_width=1.6).scale(0.8)
        tex_1_2 = TexMobject('\\mathbf{-1}', color=WHITE, background_stroke_color=WHITE, background_stroke_width=1.6).scale(0.8)
        tex_1_1.shift(RIGHT * 2.25 + DOWN * 0.275)
        tex_1_2.shift(LEFT * 2.35 + DOWN * 0.275)

        tex_cos = TexMobject('\\mathbf{\\cos{', '\\theta}}', color=GREEN_D, background_stroke_color=WHITE, background_stroke_width=1).scale(0.8)
        tex_sin = TexMobject('\\mathbf{\\sin{', '\\theta}}', color=PINK, background_stroke_color=WHITE, background_stroke_width=1).scale(0.8)
        tex_cos[1].set_color(BLUE)
        tex_sin[1].set_color(BLUE)
        tex_cos.next_to(line_2, DOWN * 0.8)
        tex_sin.next_to(line_3, RIGHT * 1.25)

        text_theta = TexMobject('\\mathbf{\\theta', '=', '\\omega', 't', '+', '\\varphi', color=BLACK,
                                background_stroke_color=BLACK, background_stroke_width=3).set_color_by_tex_to_color_map(color_dict)
        text_theta.set_height(1.).next_to(formula, DOWN * 2)
        text_theta[0].set_color(BLUE)

        tex_group = VGroup(tex_1_1, tex_1_2, tex_i_1, tex_i_2).shift(UP * 1.2)

        self.add(group_1, group_2, tex_group, tex_cos, tex_sin)
        self.wait()
        d_theta = 2.5 * DEGREES
        arrow.add_updater(lambda a, dt: a.rotate(d_theta * 0.2, about_point=ORIGIN+UP*1.2))
        self.play(Write(formula))
        self.wait()
        self.play(Write(text_theta))
        self.wait(10)
