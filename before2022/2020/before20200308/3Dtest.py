from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class TD(ThreeDScene):

  def construct(self):
    # object
    # TA = ThreeDAxes()
    sphere1 = Sphere(radius=1.5, fill_color="#FFFF00")
    cube1 = Cube(side_length=2, fill_color="#E1A158", fill_opacity=0.75)
    prism1 = Prism(dimensions=[1, 6, 1.5], fill_color="#ECABC1", fill_opacity=0.75)
    obgroup = VGroup(sphere1, cube1, prism1)
    # position
    cube1.shift(LEFT * 4)
    prism1.shift(RIGHT * 4)
    # show
    # self.play(TA, run_time=2)
    self.set_camera_orientation(phi=65 * PI / 180, theta=PI / 3)
    self.play(FadeInFromLarge(sphere1))
    self.play(ShowCreation(cube1), run_time=2)
    self.play(ShowCreation(prism1), run_time=2)
    self.wait(2)
    self.begin_ambient_camera_rotation(rate=0.1)
    self.wait(5)
    # Stop move camera
    self.stop_ambient_camera_rotation()
    self.move_camera(phi=80 * DEGREES, theta=-PI / 2)
    self.wait()
    self.play(Rotating(obgroup))
    self.wait(1)
