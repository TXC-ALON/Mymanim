from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class testAngle(Scene):
    CONFIG = {
        'radius': 1,
        'color': RED,
        'opacity': 0.4,
        'stroke_width': 10,
        # 'below_180': True,
    }
    def construct(self):
        # object
        A = np.array([2, 3, 4])
        O = np.array([0, 0, 0])
        B = np.array([-1, 2, 8])
        OA, OB = A - O, B - O
        theta = np.angle(complex(*OA[:2]) / complex(*OB[:2]))  # angle of OB to OA
        point_O = Dot().move_to(O)
        line_OA = Line(O, A)
        line_OB = Line(O, B)
        Arc_small = Arc(start_angle=Line(O, B).get_angle(), angle=theta, radius=self.radius/2,
                        stroke_width=self.stroke_width, color=GREEN)
        Arc_large = Arc(start_angle=Line(O, B).get_angle(), angle=theta, radius=self.radius,
                        stroke_width=self.stroke_width, color=self.color)
        Arc_group = VGroup(point_O, line_OA, line_OB, Arc_small, Arc_large)
        self.add(Arc_group)
        debugPoints(self,Arc_group[3])
# position

# show
