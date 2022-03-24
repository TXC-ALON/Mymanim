from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class testtoedge(Scene):

    def construct(self):
# object
        t2c = {"def": PURPLE_B, "anim": TEAL, "Square": BLUE, "UpdateFromAlphaFunc": BLUE,
               "set_value": BLUE_D, "save_state": BLUE_D, "self": RED, "run_time": ORANGE,
               "lambda": PURPLE_A, "TextMobject": BLUE, "add_updater": BLUE_D, '"': TEAL,
               ".": GREY, ",": GREY, "=": "#fa8763", "ValueTracker": BLUE}
        cir = Circle().set_color(BLUE)
        t1 = CodeLine('manim中通过点的位置来确定多边形的形状与位置', font='思源黑体').to_edge(UP)
# position
        cir.to_edge(UP)
        codet = CodeLine("t = ValueTracker()").scale(2.5)
        codet.set_color_by_t2c(t2c)
        codet.to_edge(UP)
        #codet = CodeLine("t = ValueTracker()").to_edge(UP)
        #codet.scale(2.5).set_color_by_t2c(t2c)
        #texta = TexMobject(r"add\_updater")
        texta = TexMobject(r"add_updater", plot_depth=2).scale(1.5).shift(UP * 2.5).add_background_rectangle(opacity=0.5)
        self.play(Write(texta))
        self.play(Write(codet))
        self.play(ShowCreation(cir))
        self.play(ShowCreation(t1))

class VTExample(DarkScene):
    def construct(self):
        t2c = {"def": PURPLE_B, "anim": TEAL, "Square": BLUE, "UpdateFromAlphaFunc": BLUE,
               "set_value": BLUE_D, "save_state": BLUE_D, "self": RED, "run_time": ORANGE,
               "lambda": PURPLE_A, "TextMobject": BLUE, "add_updater": BLUE_D, '"': TEAL,
               ".": GREY, ",": GREY, "=": "#fa8763", "ValueTracker": BLUE}
        codet = CodeLine("t = ValueTracker()").to_edge(UP)
        codet.scale(2.5).set_color_by_t2c(t2c)
        self.play(Write(codet))
        t = ValueTracker(-TAU)
        dec = DecimalNumber(0).shift(UP * 1 + LEFT * 5) \
            .add_updater(lambda a: a.set_value(t.get_value()))
        path = ParametricFunction(lambda t: np.array([t, np.sin(t) - 1, 0]),
                                  t_min=-8, t_max=8)
        cir = VGroup(Circle(radius=1), Dot(color=ORANGE))
        cir.add_updater(lambda a: a.move_to(np.array([
            t.get_value(), np.sin(t.get_value()) - 1, 0
        ])))
        vec = Vector()
        vec.add_updater(lambda a: a.become(
            Vector(RIGHT, color=YELLOW).rotate(
                np.arctan(np.cos(t.get_value())), about_point=ORIGIN)
            .shift(cir[0].get_center())
        ))
        vec1 = Vector()
        vec1.add_updater(lambda a: a.become(
            Vector(RIGHT, color=YELLOW).rotate(
                np.arctan(np.cos(t.get_value())), about_point=ORIGIN)
            .shift(UP * 1 + RIGHT * 4)
        ))
        self.play(ShowCreation(path), Write(dec),
                  ShowCreation(cir), ShowCreation(vec), ShowCreation(vec1))
        ve1 = Arrow(codet[0].get_center(), dec.get_center(),
                    buff=0.7, color=GREEN)
        ve2 = Arrow(codet[-1].get_center(),
                    vec1.get_start(), buff=0.7, color=GREEN)
        ve3 = Arrow().add_updater(lambda a: a.become(
            Arrow(codet.get_center(), cir.get_center(), color=GREEN, buff=1)
        ))
        #texta = TextMobject(r"add_updater", plot_depth=2) \
        #    .scale(1.5).shift(UP * 2.5).add_background_rectangle(opacity=0.5)
        self.play(ShowCreation(ve1), ShowCreation(
            ve2), ShowCreation(ve3))#, Write(texta))
        self.wait(0.5)
        self.play(t.set_value, TAU, run_time=6, rate_func=sine)
        self.wait(2)
class Testt2c(Scene):
    def construct(self):
        text = Text("abc").set_color_by_t2c({"a": BLUE})
        print(text)
        self.add(text)

class RollingWheel(DarkScene):
    def construct(self):
        t2c = {"def": PURPLE_B, "anim": TEAL, "VGroup": BLUE, "UpdateFromAlphaFunc": BLUE,
               "set_value": BLUE_D, "save_state": BLUE_D, "self": RED, "run_time": ORANGE,
               ".": GREY, ",": GREY, "=": "#fa8763"}
        ap = TexMobject("\\alpha=").shift(DOWN * 3 + LEFT * 0.7)
        dec = DecimalNumber(0).next_to(ap, RIGHT)
        l = Line(LEFT * 7, RIGHT * 7).shift(DOWN * 2)
        cir = Circle(radius=1).shift(LEFT * PI + DOWN)
        vec = Vector(DOWN, color=YELLOW).shift(LEFT * PI + DOWN)
        gup = VGroup(cir, vec)
        self.play(ShowCreation(l))
        self.play(ShowCreation(gup))

        code = CodeLine(r"""gup = VGroup(cir,vec)
gup.save_state()
def anim(obj, alpha):
    obj.restore()
    obj.shift(RIGHT*TAU*alpha)
    obj.rotate(-TAU*alpha)
    dec.set_value(alpha)
self.play(UpdateFromAlphaFunc(gup, anim),
    run_time=4)""", t2s={"def": ITALIC})
        code.scale(1.5).to_corner(UL)
        code.set_color_by_t2c(t2c)
        self.play(Write(code))
        self.play(Write(ap), Write(dec))
        gup.save_state()

        def anim(obj, alpha):
            obj.restore()
            obj.shift(RIGHT * TAU * alpha)
            obj.rotate(-TAU * alpha)
            dec.set_value(alpha)

        path = TracedPath(vec.get_end, stroke_width=4, stroke_color=ORANGE)
        self.add(path)
        self.play(UpdateFromAlphaFunc(gup, anim), run_time=4, rate_func=sine)
        self.wait()