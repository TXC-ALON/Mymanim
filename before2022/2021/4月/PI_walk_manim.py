from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class introduce(Scene):

    def construct(self):
# object
        introduce = VGroup(
            Text("众所周知，圆周率作为最常见也是最神秘的无理数之一",font="方正清刻本悦宋简体"),
            Text("历来受到无数代数学家的重视和研究",font="方正清刻本悦宋简体"),
            Text("历来受到无数代数学家的重视和研究",font="方正清刻本悦宋简体"),
            Text("众所周知，圆周率作为最常见也是最神秘的无理数之一",font="方正清刻本悦宋简体"),
            Text("历来受到无数代数学家的重视和研究",font="方正清刻本悦宋简体"),
            Text("历来受到无数代数学家的重视和研究",font="方正清刻本悦宋简体"),
        ).arrange_submobjects(
            DOWN, aligned_edge=LEFT, buff=0.5
        ).move_to(LEFT)

# position

# show
        self.play(ShowCreation(introduce))
        self.wait(4)