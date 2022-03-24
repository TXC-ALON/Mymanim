from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L


class Mobius_Strip(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 66 * DEGREES,
            "theta": -60 * DEGREES,
            "distance": 50,
        },
        'camera_config': {'background_color': WHITE},
    }

    def construct(self):
        self.set_camera_to_default_position()
        R, r = 3.2, 0.8
        mobius_surface = ParametricSurface(lambda u, v: R * np.array([np.cos(u), np.sin(u), 0])
                                                        + v * np.cos(u / 2) * np.array([np.cos(u), np.sin(u), 0])
                                                        + v * np.sin(u / 2) * OUT,
                                           u_min=0, u_max=TAU, v_min=-r, v_max=r, resolution=(80, 16),
                                           checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.6,
                                           stroke_width=1.2, fill_color=BLUE, fill_opacity=0.8)
        mobius_edge = ParametricFunction(lambda t: R * np.array([np.cos(t), np.sin(t), 0])
                                                   + r * np.cos(t / 2) * np.array([np.cos(t), np.sin(t), 0])
                                                   + r * np.sin(t / 2) * OUT,
                                         t_min=0, t_max=TAU * 2, color=RED, stroke_width=10, stroke_opacity=0.5)
        mobius_edge1 = ParametricFunction(lambda t: R * np.array([np.cos(t), np.sin(t), 0])
                                                   + r * np.sin(t / 2) * np.array([np.cos(t), np.sin(t), 0])
                                                   + r * np.sin(t / 2) * OUT,
                                         t_min=0, t_max=TAU * 2, color=YELLOW, stroke_width=10, stroke_opacity=0.5)
        mobius_edge2 = ParametricFunction(lambda t: R * np.array([np.cos(t), np.sin(t), 0])
                                                   + r * np.cos(t / 2) * np.array([np.cos(t), np.sin(t), 0])
                                                   + r * np.cos(t / 2) * OUT,
                                         t_min=0, t_max=TAU * 2, color=PINK, stroke_width=10, stroke_opacity=0.5)
        h = 0.08
        '''
        lambda u, v: R * np.array([np.cos(u), np.sin(u), 0])
                                                        + v * np.cos(u / 2) * np.array([np.cos(u), np.sin(u), 0])
                                                        + v * np.sin(u / 2) * OUT,
        '''
        ball_path = lambda t: R * np.array([np.cos(t), np.sin(t), 0]
                                           + h * np.sin(-t / 2) * np.array([np.cos(t), np.sin(t), 0])
                                           + h * np.cos(t / 2) * OUT)
        ball_edge = ParametricFunction(lambda t: R * np.array([np.cos(t), np.sin(t), 0]
                                           + h * np.sin(-t / 2) * np.array([np.cos(t), np.sin(t), 0])
                                           + h * np.cos(t / 2) * OUT),
                                         t_min=0, t_max=TAU * 2, color=GREEN, stroke_width=10, stroke_opacity=1)
        ball = Sphere(checkerboard_colors=None, fill_color=RED).set_height(0.48)
        self.time = 0

        def update_ball(b, dt):
            self.time += dt / 2
            b.move_to(ball_path(self.time))

        self.add(mobius_surface)
        self.wait(1)
        self.play(ShowCreation(mobius_edge),run_time =2)
        self.play(FadeOut(mobius_edge), run_time=1.5)
        self.play(ShowCreation(mobius_edge1), run_time=2)
        self.play(FadeOut(mobius_edge1), run_time=1.5)
        self.play(ShowCreation(mobius_edge2), run_time=2)
        self.play(FadeOut(mobius_edge2), run_time=1.5)
        self.play(ShowCreation(ball_edge), run_time=2.5)

        self.wait()
        #ball.add_updater(update_ball)
        #self.add(ball)
        #self.wait(20)

class Mobius_Strip_heartshape4(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 30 * DEGREES,
            "theta": -80 * DEGREES,
            "distance": 50,
            },
        'camera_config': {'background_color': WHITE},
    }

    def construct(self):

        self.set_camera_to_default_position()

        heart_curve_func = lambda t: (16 * np.sin(t) ** 3 * RIGHT + (13 * np.cos(t) - 5 * np.cos(2 * t) - 3 * np.cos(3 * t)
                                      - np.cos(4 * t)) * UP + np.sin(t) * (1 - abs(-t/PI)) ** 2 * 8 * OUT) * 0.2
        r = 0.5
        heart_shape_mobius = ParametricSurface(lambda u, v: heart_curve_func(u)
                                                            + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                            + v * np.sin(u/2) * OUT,
                                               u_min=-PI, u_max=PI, v_min=-r, v_max=r, resolution=(80, 12),
                                               checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.8,
                                               stroke_width=1.5, fill_color=average_color(RED, PINK), fill_opacity=0.8).scale(1)

        heart_curve = ParametricFunction(lambda t: heart_curve_func(t)
                                                            + 0.08 * np.cos(t/2) * np.array([np.cos(t), np.sin(t), 0])
                                                            + 0.08 * np.sin(t/2) * OUT,
                                         t_min=-PI, t_max=3*PI, color=RED, stroke_width=5, stroke_opacity=0.9).scale(1)

        self.add(heart_shape_mobius)
        self.play(ShowCreation(heart_curve),run_time = 3)
        self.wait(3)
        #self.play(ShowCreation(ball_edge))
        #self.wait()

class Mobius_Strip2(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 66 * DEGREES,
            "theta": -60 * DEGREES,
            "distance": 50,
            },
        'camera_config': {'background_color': WHITE},
    }
    def construct(self):
        self.set_camera_to_default_position()
        R, r = 3.2, 0.8
        mobius_surface = ParametricSurface(lambda u, v: R * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(u/2) * OUT,
                                           u_min=0, u_max=2*TAU, v_min=-r, v_max=r, resolution=(80, 16),
                                           checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.6,
                                           stroke_width=1.2, fill_color=BLUE, fill_opacity=0.8)
        mobius_edge = ParametricFunction(lambda t: R * np.array([np.cos(t), np.sin(t), 0])
                                         + r * np.cos(t/2) * np.array([np.cos(t), np.sin(t), 0])
                                         + r * np.sin(t/2) * OUT,
                                         t_min=0, t_max=2*TAU, color=RED, stroke_width=10, stroke_opacity=0.5)
        h = 0.08
        ball_path = lambda t: R * np.array([np.cos(t), np.sin(t), 0]
                                           + h * np.sin(-t/2) * np.array([np.cos(t), np.sin(t), 0])
        
                                           + h * np.cos(t/2) * OUT)
        ball = Sphere(checkerboard_colors=None, fill_color=RED).set_height(0.48)
        self.time = 0
        def update_ball(b, dt):
            self.time+=dt/2
            b.move_to(ball_path(self.time))

        self.play(ShowCreation(mobius_surface), run_time=3)
        self.wait(1)
        self.play(ShowCreation(mobius_edge), run_time=2.5)
        self.play(FadeOut(mobius_edge), run_time=1.5)
        self.wait()

