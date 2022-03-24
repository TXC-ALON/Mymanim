from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class testgettop(Scene):

    def construct(self):
# object
        text = Text("天行有常",font = "方正清刻本悦宋简体")
        dot = Dot().move_to(text.get_top())

# position
        self.add(text,dot)
# show

