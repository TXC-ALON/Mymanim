from manimlib import *
import numpy as np

from manimlib.utils import color


class CustomScene(Scene):
    def construct(self):
        # 创建一个圆环
        circle = Annulus(inner_radius=0.5, outer_radius=1, color=WHITE)

        # 创建一个正方形
        square = Square(side_length=1, fill_opacity=1, fill_color=WHITE)

        # 创建点P
        dot = Dot(radius=0.05, color=WHITE)

        # 创建文本，用于显示点P的坐标和颜色信息
        text = Text("", font="Arial")

        # 添加圆环、正方形、点和文本到场景中
        self.add(circle, square, dot, text)

        # 动画的总时长
        total_time = 10

        # 圆周上的采样点数
        num_points = 360

        for i in range(num_points):
            # 计算当前角度
            angle = TAU * i / num_points

            # 计算点P的坐标
            x = circle.outer_radius * np.cos(angle)
            y = circle.outer_radius * np.sin(angle)

            # 更新点P的位置
            dot.move_to(np.array([x, y, 0]))

            # 计算当前颜色（使用HSV颜色空间）
            hsv_color = np.array([angle / TAU, 1, 1])
            rgb_color = color.hex_to_rgb(hsv_color)

            # 更新圆环的颜色
            circle.set_color(rgb_color)

            # 更新正方形的颜色
            square.set_fill(rgb_color)

            # 更新文本
            text.become(
                Text(f"X: {x:.2f}\nY: {y:.2f}\nR: {rgb_color[0]:.2f}\nG: {rgb_color[1]:.2f}\nB: {rgb_color[2]:.2f}",
                     font="Arial"))

            # 播放当前帧
            self.play(
                circle.animate.set_color(rgb_color),
                square.animate.set_fill(rgb_color),
                dot.animate.move_to(np.array([x, y, 0])),
                Transform(text, text.copy()),
                run_time=total_time / num_points,
                rate_func=linear,
            )
