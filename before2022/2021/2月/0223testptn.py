from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class testptn(Scene):

    def construct(self):
# object
        dot_p = Dot(np.sqrt(3) * RIGHT + UP, color=BLUE).set_height(0.25)
# position
        #value_p = p2n(dot_p)
        print(dot_p[0])
# show

