from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class Epicycloid3(Scene_):
    def construct(self):
        cir_o = Circle(radius=2, color=GREEN)
        l_ab = Line(LEFT*2 , RIGHT*2, color=GREEN)
        dot_p = Dot(cir_o.point_from_proportion(0.0001))
        cir_p = Circle(radius=abs(dot_p.get_center()[0]), color=PURPLE).move_to(
            dot_p.get_center())
        dot_1 = dot_p.get_center()[0]
        dot_1.set_color(RED)
        envelop = VGroup()

        def anim(obj, alpha):
            dot_p.move_to(cir_o.point_from_proportion(alpha))
            #if abs(dot_p.get_center()[1]) > 0:
            cir_p.become(Circle(radius=abs(dot_p.get_center()[
                             0]), color=PURPLE).move_to(dot_p.get_center()))
            envelop.add(cir_p.copy().set_stroke(width=1.5, color=BLUE))

        self.add(cir_o, l_ab, dot_p, cir_p, dot_1,envelop)
        self.play(UpdateFromAlphaFunc(dot_p, anim),
                  run_time=8, rate_func=linear)
        self.wait()
