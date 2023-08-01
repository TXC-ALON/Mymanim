from manimlib import *
import numpy as np

square_length1 = 2


def calculate_target_position(dot, square_length):
    return dot.get_center() + LEFT * square_length + DOWN * square_length


POS = [UP, LEFT, DOWN, RIGHT]
FiboSquarelist = []
colorlist = [RED, YELLOW, GREEN, BLUE]


def calculate_fibonacci_recursive(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibonacci_list = calculate_fibonacci_recursive(n - 1)
    fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return fibonacci_list


def getprecenter(FiboSquarelist):
    if len(FiboSquarelist) < 2:
        return Dot()
    total_x = 0.0
    total_y = 0.0
    square_1 = FiboSquarelist[-1]
    square_2 = FiboSquarelist[-2]
    total_x += square_1.get_center()[0] +square_2.get_center()[0]
    total_y += square_1.get_center()[1] + square_2.get_center()[1]
    average_x = total_x / 2
    average_y = total_y / 2
    result_P = Dot()
    return np.array([average_x, average_y, 0])


class MyScene(Scene):
    def construct(self):
        intro_words = Text("""
            今天为大家演示斐波那契数列的图像画法
        """, font='Smiley Sans', weight='Medium', slant='oblique')
        intro_words.to_edge(UP)
        # self.play(Write(intro_words))
        # self.wait(1)
        # self.play(FadeOut(intro_words))
        # self.wait()

        # circle = Circle(radius=3, color=RED)  # 创建一个半径为2的红色圆
        # dot = Dot(color=BLUE)  # 创建一个蓝色的点
        # square = Square(square_length1)
        # dot.move_to(circle.point_from_proportion(0))  # 将点移动到圆上的起始位置
        # square.add_updater(lambda a: a.move_to(calculate_target_position(dot, square_length1)))
        # self.add(circle, dot, square)  # 将圆和点添加到场景中
        # self.play(MoveAlongPath(dot, circle), run_time=5)  # 点沿着圆形路径运动，运行时间为5秒
        # self.wait()  # 等待动画结束

        self.draw_fibonacci_square(5)
        self.wait(2)

    def draw_fibonacci_square(self, n):
        FiboList = calculate_fibonacci_recursive(n + 1)
        print(FiboList)
        for i in range(0, n):
            if i == 0:
                square = Square(side_length=FiboList[i], fill_color=colorlist[i % 4], fill_opacity=0.8)
                FiboSquarelist.append(square)
                self.play(ShowCreation(square))
            elif i == 1:
                square = Square(side_length=FiboList[1], fill_color=colorlist[i % 4],fill_opacity=0.8)
                square.move_to(np.array([-1.0,0.0,0.0]))
                FiboSquarelist.append(square)
                self.play(ShowCreation(square))
            else:
                square = Square(side_length=FiboList[i], fill_color=colorlist[i % 4],fill_opacity=0.8)

                precenter = getprecenter(FiboSquarelist)
                print("第{}次precenter为".format(i))
                print(precenter)
                nextP = precenter + POS[i % 4] * (FiboList[i])
                print("第{}次nextP为".format(i))
                print(nextP)
                print("2-----\n")
                square.move_to(nextP)
                FiboSquarelist.append(square)
                self.play(ShowCreation(square))
