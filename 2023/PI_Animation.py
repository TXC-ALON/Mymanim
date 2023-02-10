from manimlib import *
import numpy as np
from math import pi,cos,sin

class PiAnimation(Scene):
    def setup(self):
        with open("10W_digits_of_pi.txt", "r") as file:
            pi_string = file.read()
        # 定义圆的半径
        radius = 4

        # 创建一个圆
        circle = Circle(radius=radius)
        self.add(circle)

        # 将圆均分 10 段
        points = []
        for i in range(10):
            angle = i * pi / 5
            x = radius * cos(angle)
            y = radius * sin(angle)
            points.append((x, y))

        # 生成每一段中至少保留 30000 个连接点
        section_points = []
        for i in range(10):
            section = []
            for j in range(30000):
                angle = (i * pi / 5) + (j / 30000) * (pi / 5)
                x = radius * cos(angle)
                y = radius * sin(angle)
                section.append((x, y))
            section_points.append(section)

        # 对 π 的每个数字进行相连
        start = section_points[int(pi_string[0])][0]
        for i in range(1, len(pi_string)):
            end = section_points[int(pi_string[i])][0]
            line = Line(start, end)
            self.add(line)
            start = end

        # 显示动画
        self.play(ShowCreation(circle), run_time=2)
        self.wait(2)
        self.play(ShowCreation(line), run_time=5)

