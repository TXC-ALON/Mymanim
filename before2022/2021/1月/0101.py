from manimlib.imports import *

#$6b PLOT3D
# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L
def get_axis(self, min_val, max_val, axis_config):
    new_config = merge_config([
        axis_config,
        {"x_min": min_val, "x_max": max_val},
        self.number_line_config,
    ])
    return NumberLine(**new_config)


class CameraPosition2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=30 * DEGREES)
        self.play(ShowCreation(circle), ShowCreation(axes))
        self.wait()


# 移动镜头
class MoveCamera1(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.play(ShowCreation(circle), ShowCreation(axes))
        self.move_camera(phi=30 * DEGREES, theta=-45 * DEGREES, distance=4, gamma=30 * DEGREES, run_time=5)
        self.wait()


# 移动镜头，测试gamma
class MoveCamera2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.play(ShowCreation(circle), ShowCreation(axes))
        self.move_camera(phi=30 * DEGREES, theta=-45 * DEGREES, distance=8, gamma=60 * DEGREES, run_time=5)
        self.wait()


# 移动镜头测试距离
class MoveCamera3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES)
        self.play(ShowCreation(circle), ShowCreation(axes))
        self.begin_ambient_camera_rotation(rate=0.3)  # Start move camera
        self.wait(5)
        self.stop_ambient_camera_rotation()  # Stop move camera
        self.move_camera(phi=80 * DEGREES, theta=PI / 2)  # Return the position of the camera
        self.wait()
        self.move_camera(phi=-80 * DEGREES, theta=-PI / 2, run_time=2)
        # - 代表逆时针
        self.wait()


# 测试慢慢移动镜头，且判断方向
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
                u/3
            ]), color=PINK, t_min=-TAU/2, t_max=TAU/2,
        )
        axes = ThreeDAxes()

        self.add(axes)

        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(ShowCreation(curve1))
        self.wait()
        self.play(Transform(curve1, curve2), rate_func=there_and_back, run_time=3)
        self.wait()

class ParametricCurve2(ThreeDScene):
    def construct(self):
        curve1=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u/2
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
        curve2=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )

        curve1.set_shade_in_3d(True)
        curve2.set_shade_in_3d(True)

        axes = ThreeDAxes()

        self.add(axes)

        self.set_camera_orientation(phi=80 * DEGREES,theta=-60*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(ShowCreation(curve1))
        self.wait()
        self.play(Transform(curve1,curve2),rate_func=there_and_back,run_time=3)
        #there_and_back 就是恢复原来状态，，待进一步研究
        self.wait()
#todo 测试参数方程线，但都出现问题 missing 1 required positional argument: 'kwargs'  等等貌似是普遍问题，更换sense后解决



class SurfacesAnimation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cylinder = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2 * (1 - u)
            ]),
            resolution=(6, 32)).fade(0.5) #Resolution of the surfaces

        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                np.cos(v)*u,
                np.sin(v)*u,
                u**2
            ]),v_max=TAU,
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(10, 32)).scale(2)

        para_hyp = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-v**2
            ]),v_min=-2,v_max=2,u_min=-2,u_max=2,checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)).scale(1)

        cone = ParametricSurface(
            lambda u, v: np.array([
                u*np.cos(v),
                u*np.sin(v),
                u
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[GREEN_D, GREEN_E],
            resolution=(15, 32)).scale(1)

        hip_one_side = ParametricSurface(
            lambda u, v: np.array([
                np.cosh(u)*np.cos(v),
                np.cosh(u)*np.sin(v),
                np.sinh(u)
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[YELLOW_D, YELLOW_E],
            resolution=(15, 32))

        ellipsoid=ParametricSurface(
            lambda u, v: np.array([
                1*np.cos(u)*np.cos(v),
                2*np.cos(u)*np.sin(v),
                0.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[TEAL_D, TEAL_E],
            resolution=(15, 32)).scale(2)

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)


        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(sphere))
        self.wait()
        self.play(ReplacementTransform(sphere,ellipsoid))
        self.wait()
        self.play(ReplacementTransform(ellipsoid,cone))
        self.wait()
        self.play(ReplacementTransform(cone,hip_one_side))
        self.wait()
        self.play(ReplacementTransform(hip_one_side,para_hyp))
        self.wait()
        self.play(ReplacementTransform(para_hyp,paraboloid))
        self.wait()
        self.play(ReplacementTransform(paraboloid,cylinder))
        self.wait()
        self.play(FadeOut(cylinder))
#各种三维物体
class Text3D3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)


        self.add(axes)
        self.begin_ambient_camera_rotation()

        text3d0 = TextMobject("This is a 3D text").scale(1)
        self.add(axes, text3d0)
        text3d1 = TextMobject("PI / 2, axis=RIGHT").scale(2).set_shade_in_3d(True)
        text3d1.rotate(PI / 2, axis=RIGHT)
        text3d1.set_color(RED)
        text3d2 = TextMobject("PI / 2, axis=LEFT").scale(2).set_shade_in_3d(False)
        text3d2.rotate(PI / 2, axis=LEFT)
        text3d2.set_color(GREEN)
        text3d3 = TextMobject("-PI / 2, axis=RIGHT").scale(2).set_shade_in_3d(True)
        text3d3.rotate(-PI / 2, axis=RIGHT)
        text3d3.set_color(BLUE)
        text3d4 = TextMobject("PI, axis=UP").scale(2).set_shade_in_3d(True)
        text3d4.rotate(PI, axis=array([0.0, 1.0, 0.0]))
        text3d4.set_color(PINK)

        self.wait()
        self.play(ShowCreation(text3d1))
        self.wait()
        self.play(Uncreate(text3d1))
        self.wait()
        self.play(ShowCreation(text3d2))
        self.wait()
        self.play(Uncreate(text3d2))
        self.wait()
        self.play(ShowCreation(text3d3))
        self.wait()
        self.play(Uncreate(text3d3))
        self.wait()
        self.play(ShowCreation(text3d4))
        self.wait()
#实验文字

class Text3D32(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)
        text3d=TextMobject("This is a 3D text")

        self.add_fixed_in_frame_mobjects(text3d) #<----- Add this
        text3d.to_corner(UL)

        self.add(axes)
        self.begin_ambient_camera_rotation()
        self.play(Write(text3d))
#todo 添加正常字失败  'tuple' object has no attribute 'sort'


class Text3D4(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)
        self.add(axes)
        text3d4 = TextMobject("PI, axis=UP").scale(2).set_shade_in_3d(True)
        text3d4.rotate(PI/2+PI/18, axis=[0, 1.0, 1.0])
        text3d4.set_color(PINK)


        self.play(ShowCreation(text3d4))
        self.wait(2)
#todo 想探究下axis 感觉还是学会循环和update再说