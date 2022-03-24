from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class debugformula4(Scene):

    def construct(self):
# object
        formula = [
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over 2}}}",
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over 2}}}}}",
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over 2}}}}}}}}",
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over 2}}}}}}}}}}",
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over 2}}}}}}}}}}}}",
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\ddots}}}}}}}}}}}}}",
        ]
        formula_group = VGroup(*[
            TexMobject(tex).to_corner(UR) for tex in formula
        ])
# position
        self.add(formula_group[-1])
        debugTeX(self,formula_group[-1][0])
        self.wait(3)
# show

