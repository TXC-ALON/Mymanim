from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class testdotoncir(Scene):

    def construct(self):
        ci = Circle(radius = 2).set_color(BLUE)
        dot = Dot().move_to([np.cos(0)*2,np.sin(0)*2,0])
# object

# position

# show
        self.add(ci,dot)

