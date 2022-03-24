from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class CameraPosition3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES)
        self.play(ShowCreation(circle), ShowCreation(axes))
        self.wait()


class ParametricCurve1(ThreeDScene):
    def construct(self):
        curve1 = ParametricFunction(
            lambda u: np.array([
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u / 2
            ]), color=RED, t_min=-TAU, t_max=TAU,
        )
        curve2 = ParametricFunction(
            lambda u: np.array([
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u
            ]), color=RED, t_min=-TAU, t_max=TAU,
        )
        axes = ThreeDAxes()

        self.add(axes)

        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(ShowCreation(curve1))
        self.wait()
        self.play(Transform(curve1, curve2), rate_func=there_and_back, run_time=3)
        self.wait()


class Te(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = TextMobject("This is a 3D text").scale(2)
        text3d.rotate(PI / 2, axis=UP)
        self.add(axes, text3d)


class Text3D34(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = TextMobject("This is a 3D text")

        self.add_fixed_in_frame_mobjects(text3d)  # <----- Add this
        text3d.to_corner(UL)

        self.add(axes)
        self.begin_ambient_camera_rotation()
        # self.play(Write(text3d))

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2, checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        self.play(LaggedStart(ShowCreation(sphere)))
        self.wait(2)


class S(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        text3d = Text("这是一些3D图形", font="方正清刻本悦宋简体").set_height(0.7)
        text3d1 = Text("这是圆柱体", font="方正清刻本悦宋简体").set_height(0.7)
        text3d2 = Text("这是抛物面",font = "方正清刻本悦宋简体").set_height(0.7)
        self.add_fixed_in_frame_mobjects(text3d)  # <----- Add this
        text3d.to_corner(UL)

        self.begin_ambient_camera_rotation()
        self.play(Write(text3d))

        self.set_camera_orientation(phi=75 * DEGREES )
        self.begin_ambient_camera_rotation(rate=0.2)

        cylinder = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2 * (1 - u)
            ]),
            resolution=(6, 32)).fade(0.5)  # Resolution of the surfaces

        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                np.cos(v) * u,
                np.sin(v) * u,
                u ** 2
            ]), v_max=TAU,
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(10, 32)).scale(2)

        self.add(axes)
        self.play(Uncreate(text3d))
        self.add_fixed_in_frame_mobjects(text3d1)  # <----- Add this
        text3d1.to_corner(UL)
        self.play(Write(cylinder))
        self.play(Uncreate(text3d1))
        self.add_fixed_in_frame_mobjects(text3d2)  # <----- Add this
        text3d2.to_corner(UL)
        self.play(ReplacementTransform(cylinder, paraboloid))
        # self.play(ReplacementTransform(text3d, text3d1))

        self.wait()
        # self.play(ReplacementTransform(text3d1, text3d2))

