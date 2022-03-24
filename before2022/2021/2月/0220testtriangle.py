from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class testtriangle(Scene):

    def construct(self):
# object
        tri = Triangle().scale(2.5)
        dot = Dot().move_to(tri.points[0])

        cir = Circle().scale(1).set_color(GOLD).move_to(dot)#.set_fill(color = average_color(GOLD,PINK),opacity = 1)

        cir2 = Circle().scale(0.5).set_color(GREEN).move_to(cir.points[8])
        dot2 = Dot().move_to(cir.points[8])
        def anim(obj1, alpha):
            obj1.move_to(tri.point_from_proportion(alpha))
            cir.add_updater(lambda a: a.move_to(obj1))
            cir2.add_updater(lambda a: a.next_to(cir))

        def anim2(obj2, alpha):
            obj2.move_to(cir.point_from_proportion(alpha))
            cir2.add_updater(lambda a: a.move_to(obj2))
# position

# show
        self.play(ShowCreation(tri))
        self.add(dot,cir,cir2)
        self.wait(1)
        cir.rotate(PI/2)#小细节，不然anim alpha就从右边开始
        self.play(UpdateFromAlphaFunc(dot,anim),
                  UpdateFromAlphaFunc(dot2,anim2),
                  run_time=5, rate_func=linear)
        self.wait(1)

class debugPointsScene(DarkScene):
    def construct(self):
        obj = Triangle().scale(3)
        obj2 = Circle().scale(2).set_color(GREEN)
        #obj.points[1:4] += RIGHT
        self.add(obj,obj2)
        debugPoints(self, obj)
        debugPoints(self, obj2)
class MoveAlongPathWithAlphaScene(DarkScene):
    def construct(self):
        line = Line(LEFT * 4, RIGHT * 4, color=BLUE).shift(UP * 2.5)
        cir = Circle().shift(LEFT * 3 + DOWN).scale(2)
        sinfunc = ParametricFunction(
            lambda t: np.array([t, np.sin(t), 0]), t_min=-PI / 2, t_max=PI / 2) \
            .shift(RIGHT * 2 + DOWN).set_color(YELLOW)
        dot0 = Dot()
        dot1 = Dot()
        dot2 = Dot()

        def anim0(obj, alpha):
            obj.move_to(line.point_from_proportion(alpha))

        def anim1(obj, alpha):
            obj.move_to(cir.point_from_proportion(alpha))

        def anim2(obj, alpha):
            obj.move_to(sinfunc.point_from_proportion(alpha))

        self.play(ShowCreation(line),
                  ShowCreation(cir),
                  ShowCreation(sinfunc))

        self.add(dot0, dot1, dot2)
        debugPoints(self, line)
        debugPoints(self, cir)

        self.play(UpdateFromAlphaFunc(dot0, anim0),
                  UpdateFromAlphaFunc(dot1, anim1),
                  UpdateFromAlphaFunc(dot2, anim2),
                  run_time=5, rate_func=linear)