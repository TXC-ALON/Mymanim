from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class testsquarepoints(Scene):

    def construct(self):
# object
        squ = Square()
        #squ.points[0:4] += RIGHT
        print(squ[0][0])
        dot = Dot().set_color(RED).move_to(squ.points[0])
# position
        self.add(squ,dot)
        debugAllPoints(self,squ)
# show

