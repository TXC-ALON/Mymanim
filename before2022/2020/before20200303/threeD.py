from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class SP(ThreeDScene):

  def construct(self):
    # object
    r = 7
    sun = Sphere(radius=1.6)
    planet = Sphere(radius=0.4)
    orbit = Circle(radius=r)
    planet.shift(UP * r)
    system = VGroup(orbit, sun, planet)
    system.shift(DOWN * 2 + LEFT * 1.2)

    F_vector = Vector(np.array([0, -5, 0]), color=YELLOW)
    F_vector.next_to(planet, DOWN * 0.6)
    F_fomula = TextMobject('$\\vec{F}= G m_1 m_2 \\frac{(\\vec{r_1}-\\vec{r_2})}{r^3}$', color=GOLD)
    # F_fomula.scale(0.9)
    # position
    F_fomula.rotate_about_origin(PI / 2)
    F_fomula.next_to(F_vector, LEFT * 0.4)

    self.set_camera_orientation(phi=65 * PI / 180, theta=PI / 3)

    # show
    self.play(ShowCreation(orbit))
    self.wait(1)
    self.play(FadeIn(sun), FadeInFromLarge(planet))
    self.wait(1)
    self.play(ShowCreation(F_vector))
    self.play(Write(F_fomula))
    self.wait(2)
