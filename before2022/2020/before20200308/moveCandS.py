from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class TestRotatingWhileMoving(ThreeDScene):

  def construct(self):
    square = Square(side_length=0.8, color=GREEN, fill_opacity=1)
    circle = Circle(radius=0.8, color=ORANGE, fill_opacity=1, shade_in_3d=True)
    square.add_updater(lambda m, dt: m.rotate(0.5 * dt))
    circle.add_updater(lambda m, dt: m.rotate(0.3 * dt, axis=UP))
    group = Group(circle, square)
    group.arrange_submobjects(RIGHT, buff=0.5)
    self.add(group)
    for vec in (UP + RIGHT,LEFT * 3, DOWN*2, RIGHT*4+UP):
      circle.resume_updating(), square.resume_updating()
      self.play(ApplyMethod(group.shift, vec), run_time= int(get_norm(vec))+1)
      circle.suspend_updating(), square.suspend_updating()

    # self.play(ShowCreation(circle1))
    # self.play(FadeIn(square1))
    # self.play(ApplyMethod(group.shift, LEFT * 2), run_time=0.5)
    # self.play(ApplyMethod(group.shift, UP * 2), run_time=0.5)
    # self.play(ApplyMethod(group.shift, RIGHT * 4), run_time=0.5)
    # self.play(ApplyMethod(group.shift, DOWN * 4), run_time=0.5)
    # self.play(ApplyMethod(group.shift, LEFT * 4), run_time=0.5)
    # self.play(ApplyMethod(group.shift, UP * 2), run_time=0.5)
    # self.play(ApplyMethod(group.shift, RIGHT * 2), run_time=0.5)
    # self.wait(2)
