from manimlib import *
import numpy as np

def calculate_fibonacci_recursive(n, base=1.0):
    if n <= 0:
        return []
    if n == 1:
        return [base]
    if n == 2:
        return [base, base]
    fibonacci_list = calculate_fibonacci_recursive(n - 1, base)
    fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return fibonacci_list

class testCamera(ThreeDScene):
    def setup(self):
        # 初始化坐标系
        self.plane = NumberPlane()
        self.plane.add_coordinate_labels()
        self.add(self.plane)

    def t_func(self, t):
        # 螺线参数方程
        a, b = 3, 3
        return np.array([
            a * np.cos(t) / t,
            b * np.sin(t) / t,
            0
        ])

    def construct(self):
        # 获取相机帧的引用
        frame = self.camera.frame
        # 创建螺线
        curve = ParametricCurve(self.t_func, t_range=[0.1, 100, 0.05], color=YELLOW)
        self.add(curve)
        print(frame.get_height())
        #frame.center().move_to(np.array([0.0,4.0,9.0]))
        self.play(frame.animate.move_to(np.array([0.0,4.0,30.0])),run_time = 5)
        #frame.set_orientation((Rotation([0.8, 0.2, 0.1, 0.9])))
        #self.play(frame.animate.set_width(30),run_time = 4)
        self.wait(0.5)