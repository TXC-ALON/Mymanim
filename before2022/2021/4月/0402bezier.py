from manim_sandbox.utils.imports import *

'''
# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L
import numpy as np
PI = np.pi
step=80
list = []
for i in range(0,step):
    angle = 2*PI/step*i
    dot = np.array([np.cos(angle),np.sin(angle),0])
    list.append(dot)

print(list)



dot_lst = [
    np.array([1., 0., 0.]), np.array([0.99691733, 0.0784591, 0.]), np.array([0.98768834, 0.15643447, 0.]),
    np.array([0.97236992, 0.23344536, 0.]), np.array([0.95105652, 0.30901699, 0.]),
    np.array([0.92387953, 0.38268343, 0.]), np.array([0.89100652, 0.4539905, 0.]),
    np.array([0.85264016, 0.52249856, 0.]), np.array([0.80901699, 0.58778525, 0.]),
    np.array([0.76040597, 0.64944805, 0.]), np.array([0.70710678, 0.70710678, 0.]),
    np.array([0.64944805, 0.76040597, 0.]), np.array([0.58778525, 0.80901699, 0.]),
    np.array([0.52249856, 0.85264016, 0.]), np.array([0.4539905, 0.89100652, 0.]),
    np.array([0.38268343, 0.92387953, 0.]), np.array([0.30901699, 0.95105652, 0.]),
    np.array([0.23344536, 0.97236992, 0.]), np.array([0.15643447, 0.98768834, 0.]),
    np.array([0.0784591, 0.99691733, 0.]), np.array([6.123234e-17, 1.000000e+00, 0.]),
    np.array([-0.0784591, 0.99691733, 0.]), np.array([-0.15643447, 0.98768834, 0.]),
    np.array([-0.23344536, 0.97236992, 0.]), np.array([-0.30901699, 0.95105652, 0.]),
    np.array([-0.38268343, 0.92387953, 0.]), np.array([-0.4539905, 0.89100652, 0.]),
    np.array([-0.52249856, 0.85264016, 0.]), np.array([-0.58778525, 0.80901699, 0.]),
    np.array([-0.64944805, 0.76040597, 0.]), np.array([-0.70710678, 0.70710678, 0.]),
    np.array([-0.76040597, 0.64944805, 0.]), np.array([-0.80901699, 0.58778525, 0.]),
    np.array([-0.85264016, 0.52249856, 0.]), np.array([-0.89100652, 0.4539905, 0.]),
    np.array([-0.92387953, 0.38268343, 0.]), np.array([-0.95105652, 0.30901699, 0.]),
    np.array([-0.97236992, 0.23344536, 0.]), np.array([-0.98768834, 0.15643447, 0.]),
    np.array([-0.99691733, 0.0784591, 0.]), np.array([-1.0000000e+00, 1.2246468e-16, 0.]),
    np.array([-0.99691733, -0.0784591, 0.]), np.array([-0.98768834, -0.15643447, 0.]),
    np.array([-0.97236992, -0.23344536, 0.]), np.array([-0.95105652, -0.30901699, 0.]),
    np.array([-0.92387953, -0.38268343, 0.]), np.array([-0.89100652, -0.4539905, 0.]),
    np.array([-0.85264016, -0.52249856, 0.]), np.array([-0.80901699, -0.58778525, 0.]),
    np.array([-0.76040597, -0.64944805, 0.]), np.array([-0.70710678, -0.70710678, 0.]),
    np.array([-0.64944805, -0.76040597, 0.]), np.array([-0.58778525, -0.80901699, 0.]),
    np.array([-0.52249856, -0.85264016, 0.]), np.array([-0.4539905, -0.89100652, 0.]),
    np.array([-0.38268343, -0.92387953, 0.]), np.array([-0.30901699, -0.95105652, 0.]),
    np.array([-0.23344536, -0.97236992, 0.]), np.array([-0.15643447, -0.98768834, 0.]),
    np.array([-0.0784591, -0.99691733, 0.]), np.array([-1.8369702e-16, -1.0000000e+00, 0.]),
    np.array([0.0784591, -0.99691733, 0.]), np.array([0.15643447, -0.98768834, 0.]),
    np.array([0.23344536, -0.97236992, 0.]), np.array([0.30901699, -0.95105652, 0.]),
    np.array([0.38268343, -0.92387953, 0.]), np.array([0.4539905, -0.89100652, 0.]),
    np.array([0.52249856, -0.85264016, 0.]), np.array([0.58778525, -0.80901699, 0.]),
    np.array([0.64944805, -0.76040597, 0.]), np.array([0.70710678, -0.70710678, 0.]),
    np.array([0.76040597, -0.64944805, 0.]), np.array([0.80901699, -0.58778525, 0.]),
    np.array([0.85264016, -0.52249856, 0.]), np.array([0.89100652, -0.4539905, 0.]),
    np.array([0.92387953, -0.38268343, 0.]), np.array([0.95105652, -0.30901699, 0.]),
    np.array([0.97236992, -0.23344536, 0.]), np.array([0.98768834, -0.15643447, 0.]),
    np.array([0.99691733, -0.0784591, 0.])]
'''


class testdot20(DarkScene):
    def construct(self):
        dot_list = [
            np.array([3., 0., 0.]), np.array([2.85316955, 0.92705098, 0.]), np.array([2.42705098, 1.76335576, 0.]),
            np.array([1.76335576, 2.42705098, 0.]), np.array([0.92705098, 2.85316955, 0.]),
            np.array([1.8369702e-16, 3.0000000e+00, 0.0000000e+00]), np.array([-0.92705098, 2.85316955, 0.]),
            np.array([-1.76335576, 2.42705098, 0.]), np.array([-2.42705098, 1.76335576, 0.]),
            np.array([-2.85316955, 0.92705098, 0.]), np.array([-3.0000000e+00, 3.6739404e-16, 0.]),
            np.array([-2.85316955, -0.92705098, 0.]), np.array([-2.42705098, -1.76335576, 0.]),
            np.array([-1.76335576, -2.42705098, 0.]), np.array([-0.92705098, -2.85316955, 0.]),
            np.array([-5.5109106e-16, -3.0000000e+00, 0.0000000e+00]), np.array([0.92705098, -2.85316955, 0.]),
            np.array([1.76335576, -2.42705098, 0.]), np.array([2.42705098, -1.76335576, 0.]),
            np.array([2.85316955, -0.92705098, 0.]), np.array([3., 0., 0.])]
        listlen = len(dot_list)
        dotgroup = VGroup()  # dot group
        line_inner = VGroup()
        line_group_vertical = VGroup()
        line_group_horizontal = VGroup()
        for i in range(listlen):
            dotgroup.add(Dot(dot_list[i], color=YELLOW_E).scale(0.5))
            line_inner.add(DashedLine(ORIGIN, Dot(dot_list[i], color=YELLOW_E)).set_stroke(width=0.8))
            line_group_vertical.add(
                Line(np.array([dot_list[i][0], 4, 0]), np.array([dot_list[i][0], -4, 0]), color=BLUE).set_stroke(
                    width=0.7))
            line_group_vertical.add(
                Line(np.array([-4, dot_list[i][1], 0]), np.array([4, dot_list[i][1], 0]), color=PINK).set_stroke(
                    width=0.7))
        cir = Circle().scale(3).set_color(GREEN)
        self.add(cir)
        self.play(ShowCreation(dotgroup))
        self.play(ShowCreation(line_inner))
        self.wait()
        self.play(ShowCreation(line_group_vertical))
        self.wait()
        self.play(ShowCreation(line_group_horizontal))
        self.wait()


class twentyDim(DarkScene):
    def construct(self):
        dot_lst = [np.array([3., 0., 0.]), np.array([2.42705098, 1.76335576, 0.]),
                   np.array([0.92705098, 2.85316955, 0.]), np.array([0.92705098, 2.85316955, 0.]),

                   np.array([-0.92705098, 2.85316955, 0.]), np.array([-2.42705098, 1.76335576, 0.]),
                   np.array([-3.0000000e+00, 3.6739404e-16, 0.0000000e+00]),
                   np.array([-3.0000000e+00, 3.6739404e-16, 0.0000000e+00]),
                   np.array([-2.42705098, -1.76335576, 0.]),
                   np.array([-0.92705098, -2.85316955, 0.]), np.array([0.92705098, -2.85316955, 0.]),
                   np.array([0.92705098, -2.85316955, 0.])]
        obj = BezierGenerator(dot_lst)
        dot_anim = obj.dot_anim
        line_anim = obj.sync_line
        obj[1].add_updater(line_anim)
        path = obj.curve_path
        self.add(obj)
        self.wait()
        self.play(UpdateFromAlphaFunc(obj[0], dot_anim),
                  ShowCreation(path),
                  run_time=6.5)
        self.wait()
