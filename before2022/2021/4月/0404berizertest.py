from manim_sandbox.utils.imports import *
import sys
sys.setrecursionlimit(1000000)

# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L
def bezier(self, olddot, newdot):
    listlen = len(olddot)
    if listlen == 1:
        t = ValueTracker(0)
        path = TracedPath(olddot[0].get_center, stroke_width=7, stroke_color=RED)
        self.add(path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
    else:
        linegroup = VGroup()
        newdotgroup = VGroup()
        for i in range(1, listlen):
            t = ValueTracker(0)
            # linegroup.add(Line(olddot[i], olddot[i - 1], color=YELLOW_E)).set_stroke(width=0.8))
            newdotgroup.add(Dot(color=BLUE).add_updater(lambda m: m.move_to(
                (olddot[i].get_center() - olddot[i - 1].get_center()) * t.get_value() + olddot[
                    i - 1].get_center())))
        listlen -= 1
        bezier(self,newdot, olddot)
class funcbezier(Scene):

    def construct(self):
        dot_list = [
            np.array([-3, -1.5, 0]),
            np.array([-3.6, 1.5, 0]),
            np.array([0, 1.5, 0]),
            np.array([3, -1.5, 0])
        ]
        dotgroup = VGroup()
        for i in range(4):
            dotgroup.add(Dot(dot_list[i], color=YELLOW_E).scale(0.5))
        newdot = VGroup()
        bezier(self,dotgroup,newdot)

