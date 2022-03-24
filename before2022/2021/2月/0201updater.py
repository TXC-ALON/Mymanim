from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class Rotate(Scene):

    def construct(self):
        # object
        axes = Axes().set_opacity(0.5)
        sq1 = Square(side_length=1, color=BLUE).shift(UP * 2.5)
        sq2 = Square(side_length=1, color=PINK).shift(UP * 2.5)
        # position

        # show
        self.add(axes, sq1, sq2)
        self.wait()
        self.play(
            Rotating(sq1, radians=TAU / 3, about_point=ORIGIN),
            sq2.rotate, {"about_point": ORIGIN, "angle": TAU / 3},
            run_time=4
        )
        self.wait()


class RotatingExample(Scene):
    def construct(self):
        square = Square().scale(2)
        self.add(square)

        self.play(
            Rotating(
                square,
                radians=PI / 4,
                run_time=2
            )
        )
        self.wait(0.3)
        self.play(
            Rotating(
                square,
                radians=PI,
                run_time=2,
                axis=[1,1,1]
            )
        )
        self.wait(0.3)

class ValueTrackerScene2(DarkScene):
    def construct(self):
        t = ValueTracker(0)
        cir = Circle(radius=2).shift(LEFT * 5)
        dot_o = Dot(LEFT * 5).set_color(RED)
        dot_a = Dot(LEFT * 3).set_color(YELLOW)
        l_oa = Line(LEFT * 5, LEFT * 3)
        dot_p = Dot().add_updater(lambda a: a.move_to(
            np.array([-5 + 2 * np.cos(t.get_value()), 2 * np.sin(t.get_value()), 0])))
        l_op = Line().add_updater(lambda a: a.put_start_and_end_on(
            dot_o.get_center(), dot_p.get_center()))
        arc = Arc(angle=0).add_updater(lambda a: a.become(
            Arc(start_angle=0, angle=t.get_value() % TAU, color=ORANGE).shift(LEFT * 5)))
        self.add(cir, dot_o, dot_a, dot_p, l_oa, l_op, arc)
        self.play(t.set_value, 2 * TAU, run_time=8, rate_func=linear)
class ValueTrackerScene3(DarkScene):
    def construct(self):
        t = ValueTracker(0)
        cir = Circle(radius=2).shift(LEFT * 5)
        dot_p = Dot().add_updater(lambda a: a.move_to(
            np.array([-5 + 2 * np.cos(t.get_value()), 2 * np.sin(t.get_value()), 0])))
        dot_q = Dot().add_updater(lambda a: a.move_to(
            np.array([-2, 2 * np.sin(t.get_value()), 0])))
        l_pq = DashedLine().add_updater(lambda a: a.put_start_and_end_on(
            dot_p.get_center(), dot_q.get_center()))
        dot_m = Dot().add_updater(lambda a: a.move_to(
            np.array([-2, 2 * np.cos(t.get_value()), 0])))
        l_pm = DashedLine().add_updater(lambda a: a.put_start_and_end_on(
            dot_p.get_center(), dot_m.get_center()))
        path = TracedPath(dot_q.get_center, stroke_width=6,
                          stroke_color=YELLOW)
        path.add_updater(lambda a: a.shift(RIGHT * 0.04))
        path2 = TracedPath(dot_m.get_center, stroke_width=6,
                          stroke_color=BLUE)
        path2.add_updater(lambda a: a.shift(RIGHT * 0.04))
        self.add(cir, dot_p, dot_q,dot_m, l_pq, l_pm,path,path2)
        self.play(t.set_value, 2 * TAU, run_time=8, rate_func=linear)

class DtFourierScene(DarkScene):
    def construct(self):
        axes = Axes()
        vec1 = Vector(RIGHT, color=YELLOW)
        cir1 = Circle(radius=1, color=BLUE)
        gup1 = VGroup(vec1, cir1)

        vec2 = Vector(RIGHT, color=YELLOW)
        cir2 = Circle(radius=1, color=BLUE)
        gup2 = VGroup(vec2, cir2)
        gup2.save_state()

        def anim1(obj, dt):
            obj.rotate(dt, about_point=ORIGIN)

        def anim2(obj):
            obj.restore()
            obj.rotate(-vec1.get_angle())
            obj.shift(vec1.get_vector())

        gup1.add_updater(anim1)
        gup2.add_updater(anim2)

        path = TracedPath(vec2.get_end, stroke_width=6, stroke_color=ORANGE)
        path.add_updater(lambda a, dt: a.shift(DOWN * dt))
        self.add(axes, gup1, gup2, path)
        self.wait(6)

class LastSceneHelp(DarkScene):
    def construct(self):
        axes = Axes()
        vec1 = Vector(RIGHT, color=YELLOW_E)
        cir1 = Circle(radius=1, color=BLUE_E)
        gup1 = VGroup(vec1, cir1)

        vec2 = Vector(RIGHT, color=YELLOW)
        cir2 = Circle(radius=1, color=BLUE)
        gup2 = VGroup(vec2, cir2)
        gup2.save_state()

        text1 = TextMobject("Group1").add_updater(
            lambda a: a.next_to(gup1, LEFT))
        text2 = TextMobject("Group2").add_updater(
            lambda a: a.next_to(gup2, RIGHT))

        code0 = CodeLine(r"""def anim1(obj, dt):
	obj.rotate(dt, about_point=ORIGIN)""").scale(2).shift(RIGHT * 3.9 + DOWN * 2)
        code0[0:3].set_color(PURPLE_A)
        code0[10:13].set_color(YELLOW_D)
        code0[15:17].set_color(YELLOW_D)
        code0[-19:-8].set_color(YELLOW_D)

        code = CodeLine(r"""def anim2(obj):
	obj.restore()
	obj.rotate(-vec1.get_angle())
	obj.shift(vec1.get_vector())""").scale(2).next_to(code0, DOWN, aligned_edge=LEFT)
        code[0:3].set_color(PURPLE_A)
        code[10:13].set_color(YELLOW_D)

        point = TexMobject("\\blacktriangleright",
                           color=YELLOW).next_to(code0[0], LEFT)

        self.add(gup1, gup2, text1, text2, code, point, code0)
        self.play(gup2.shift, vec1.get_vector(), run_time=0.5)
        self.add(vec2.copy().set_opacity(0.2),
                 cir2.copy().set_stroke(opacity=0.2))
        self.wait(0.2)

        for i in range(10):
            self.play(point.next_to, code0[21], LEFT, run_time=0.3)
            self.play(MRotate(gup1, radians=PI / 5,
                              about_point=ORIGIN), run_time=0.7)
            self.play(point.next_to, code[17], LEFT, run_time=0.3)
            self.play(gup2.restore, run_time=0.7)
            self.play(point.next_to, code[32], LEFT, run_time=0.3)
            self.play(MRotate(gup2, radians=-vec1.get_angle(),
                              about_point=ORIGIN), run_time=0.7)
            self.play(point.next_to, code[63], LEFT, run_time=0.3)
            self.play(gup2.shift, vec1.get_vector(), run_time=0.7)
            self.add(vec2.copy().set_opacity(0.2),
                     cir2.copy().set_stroke(opacity=0.2))

        def anim1(obj, dt):
            obj.rotate(dt, about_point=ORIGIN)

        def anim2(obj):
            obj.restore()
            obj.rotate(-vec1.get_angle())
            obj.shift(vec1.get_vector())

        gup1.add_updater(anim1)
        gup2.add_updater(anim2)
        text1.clear_updaters()
        text2.clear_updaters()
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(point))
        self.wait(2 * TAU)



class EnvelopFunc(DarkScene):
    def construct(self):
        sq1 = Square(color=RED, side_length=2).shift(UP * 2 + LEFT * 5)
        sq2 = Square(color=RED, side_length=2).shift(UP * 2 + LEFT * 5) \
            .set_stroke(width=0.5, opacity=0.5)
        dt = 1 / self.camera.frame_rate
        en = VGroup()
        self.add(sq1, sq2, en, sq2.copy())

        def anim(obj):
            obj.shift(RIGHT * dt * 2)
            obj.rotate(0.4 * TAU * dt)
            en.add(obj.copy())

        def anim2(obj):
            obj.shift(RIGHT * dt)
            obj.rotate(0.2 * TAU * dt)

        sq4 = Square(color=GREEN, side_length=2).shift(LEFT * 5 + DOWN * 2)
        dot0 = Dot(sq4.get_vertices()[0], color=BLUE).scale(2)
        dot1 = Dot(sq4.get_vertices()[1], color=YELLOW).scale(2)
        dot2 = Dot(sq4.get_vertices()[2], color=ORANGE).scale(2)
        dot3 = Dot(sq4.get_vertices()[3], color=PURPLE_A).scale(2)
        vg1 = VGroup(sq4, dot0, dot1, dot2, dot3)
        self.add(vg1)

        self.wait()
        self.play(UpdateFromFunc(sq2, anim),
                  FadeIn(vg1.copy().shift(
                      RIGHT * 10).rotate(PI).set_stroke(opacity=0.3)),
                  run_time=5 - 2 * dt, rate_func=linear)
        self.wait()
        self.play(UpdateFromFunc(sq1, anim2),

                  vg1.shift, RIGHT * 10,
                  vg1.rotate, PI,

                  run_time=10 - 2 * dt, rate_func=linear)
        self.wait()


class ExplainExample1(DarkScene):

    def construct(self):
        t2c_dic = {"def": PURPLE_B,
                   "anim": TEAL_D,
                   "restore": BLUE_D,
                   "shift": BLUE_D,
                   "rotate": BLUE_D,
                   "save_state": BLUE_D}
        code = CodeLine(r"""sq.save_state()

def anim(obj, alpha):
    obj.restore()
    obj.shift(RIGHT*alpha*10)
    obj.rotate(PI*3*alpha)""", t2s={"def": ITALIC}).scale(2).to_corner(DR, buff=1)
        code.set_color_by_t2c(t2c_dic)
        code[26:29].set_color(ORANGE)
        self.add(code)
        text = TexMobject("\\blacktriangleright",
                          color=YELLOW).next_to(code[0], LEFT)
        self.add(text)
        line = Line(LEFT * 5, RIGHT * 5).set_color(GREY)
        sq = Square(side_length=1, color=BLUE).shift(LEFT * 5)
        sq.save_state()

        def anim(obj, alpha):
            obj.restore()
            obj.shift(RIGHT * alpha * 10)
            obj.rotate(PI * 3 * alpha)

        self.add(line, sq)

        verticalL = VGroup(*[DashedLine(UP, DOWN, color=GREY).move_to(
            line.point_from_proportion(i / 10)) for i in range(11)])
        numG = VGroup(*[DecimalNumber(i / 10, num_decimal_places=1).scale(0.6).next_to(verticalL[i], UP)
                        for i in range(11)])
        self.add(verticalL, numG)

        self.wait()
        self.add(sq.copy().set_stroke(opacity=0.35, color=WHITE))
        for i in range(1, 11):
            self.play(text.next_to, code[43], LEFT, run_time=0.3)
            self.play(sq.restore, run_time=0.7)
            self.play(text.next_to, code[61], LEFT, run_time=0.3)
            self.play(sq.shift, RIGHT * i, run_time=0.7)
            self.play(text.next_to, code[91], LEFT, run_time=0.3)
            self.play(Rotating(sq, radians=PI * 3 * i / 10), run_time=0.7)
            self.add(sq.copy().set_stroke(opacity=0.35, color=WHITE))

        self.play(sq.restore)
        self.play(UpdateFromAlphaFunc(sq, anim),
                  run_time=10, rate_func=linear)
        self.wait()

