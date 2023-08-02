from manimlib import *
import numpy as np

square_length1 = 2


def calculate_target_position(dot, square_length):
    return dot.get_center() + LEFT * square_length + DOWN * square_length


POS = [UP, LEFT, DOWN, RIGHT]
FiboSquarelist = []
FiboPointlist = []
colorlist = [RED, YELLOW, GREEN, BLUE]


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


class MyPoint():
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def print(self):
        print("this P x is {0} y is {1}".format(self.x, self.y))


def calculate_fibonacci_Points(n, base):
    FiboPL = [MyPoint(0.0, 0.0)]
    FiboList = calculate_fibonacci_recursive(n + 3, base)
    Dir = [MyPoint(0, 1), MyPoint(-1, 0), MyPoint(0, -1), MyPoint(1, 0)]
    FiboNumpyL = []
    if (n == 0):
        return FiboPL
    else:
        for i in range(1, n):
            curP = FiboPL[-1]
            nextP = MyPoint(curP.x + Dir[(i + 2) % 4].x * FiboList[i - 1],
                            curP.y + Dir[(i + 2) % 4].y * FiboList[i - 1])
            resultP = MyPoint(nextP.x + Dir[(i + 3) % 4].x * FiboList[i - 1],
                              nextP.y + Dir[(i + 3) % 4].y * FiboList[i - 1])
            FiboPL.append(resultP)
    for i in range(1, len(FiboPL)):
        P_1 = FiboPL[i - 1]
        P_2 = FiboPL[i]
        resP = MyPoint((P_1.x + P_2.x) / 2, (P_1.y + P_2.y) / 2)
        resnp_p = np.array([resP.x, resP.y, 0])
        FiboNumpyL.append(resnp_p)
    for P in FiboPL:
        print("Fibo")
        P.print()
    return [FiboNumpyL, FiboPL]


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

        self.draw_fibonacci_square(7, 1)
        self.wait(2)

    def draw_fibonacci_square(self, n, base):
        FiboList = calculate_fibonacci_recursive(n + 3, base)
        FiboCenterList = calculate_fibonacci_Points(n + 3, base)[0]
        FiboArcList = calculate_fibonacci_Points(n + 3, base)[1]
        print(FiboList)
        for i in range(0, n):
            print("this {0} time length {1},pos = {2}".format(i, FiboList[i], FiboCenterList[i]))
            square = Square(side_length=FiboList[i], fill_color=colorlist[i % 4], fill_opacity=0.8)
            arc = Arc(((3 + i) / 4) * TAU, TAU / 4, radius=FiboList[i])
            FiboSquarelist.append(square)
            square.move_to(FiboCenterList[i])
            resP = MyPoint(FiboArcList[i].x, FiboArcList[i].y)
            resP.print()
            movepoint = np.array([resP.x, resP.y, 0]) + POS[i] * FiboList[i]
            print("0802-- movepoint{0} ".format(movepoint))
            arc.move_arc_center_to(movepoint)
            self.play(ShowCreation(square))
            self.play(ShowCreation(arc))
