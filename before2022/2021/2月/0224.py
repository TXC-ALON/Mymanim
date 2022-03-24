from manimlib.imports import *

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
                                                + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(u/2) * OUT,
                                           u_min=0, u_max=TAU, v_min=-r, v_max=r, resolution=(80, 16),
                                           checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.6,
                                           stroke_width=1.2, fill_color=BLUE, fill_opacity=0.8)
        mobius_edge = ParametricFunction(lambda t: R * np.array([np.cos(t), np.sin(t), 0])
                                         + r * np.cos(t/2) * np.array([np.cos(t), np.sin(t), 0])
                                         + r * np.sin(t/2) * OUT,
                                         t_min=0, t_max=TAU * 2, color=RED, stroke_width=10, stroke_opacity=0.5)
        h = 0.08
        ball_path = lambda t: R * np.array([np.cos(t), np.sin(t), 0] + h * np.sin(-t/2) * np.array([np.cos(t), np.sin(t), 0]) + h * np.cos(t/2) * OUT)
        ball = Sphere(checkerboard_colors=None, fill_color=RED).set_height(0.48)
        self.time = 0
        def update_ball(b, dt):
            self.time+=dt/2
            b.move_to(ball_path(self.time))

        self.play(ShowCreation(mobius_surface), run_time=2)
        self.wait(1)
        self.play(ShowCreation(mobius_edge), run_time=2.5)
        self.play(FadeOut(mobius_edge), run_time=1.5)
        self.wait()
        ball.add_updater(update_ball)
        self.add(ball)
        self.wait(20)


class Mobius_Strip_heartshape0(SpecialThreeDScene):

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
        heart_shape_mobius = ParametricSurface(lambda u, v: heart_curve_func(u) + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(-u/2) * OUT,
                                               u_min=-PI, u_max=PI, v_min=-r, v_max=r, resolution=(80, 12),
                                               checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.8,
                                               stroke_width=1.5, fill_color=average_color(RED, PINK), fill_opacity=0.8)

        heart_curve = ParametricFunction(heart_curve_func, t_min=-PI, t_max=PI, color=RED, stroke_width=10, stroke_opacity=0.9)

        self.play(ShowCreation(heart_curve))
        self.wait()

        self.play(ShowCreation(heart_shape_mobius))
        self.wait()

        heart_shape_mobius.add_updater(lambda m, dt: m.rotate(5 * DEGREES, axis=UP))

        self.wait(8)

'''
16 * np.sin(t) ** 3 * RIGHT  x
(13 * np.cos(t) - 5 * np.cos(2 * t) - 3 * np.cos(3 * t)- np.cos(4 * t)) * UP y
np.sin(t) * (1 - aθs(-t/PI)) ** 2 * 8 * OUT  z
ParametricPlot3D[{cos[t] (3 + r cos[t/2]), sin[t] (3 + r cos[t/2]), r sin[t/2]}

np.cos(t)*(3+u)
曲面((1 + h*cos(θ / 2))*cos(θ), (1 + h*cos(θ / 2))*sin(θ), h*sin(θ / 2), θ, 0, 2π, h, -0.5, 0.5)
curve(16 * sin(t) ** 3,(13 * cos(t) - 5 *cos(2 * t) - 3 *cos(3 * t)-cos(4 * t)),sin(t) * (1 - aθs(-t/PI)) ** 2 * 8)
曲面(16sin³(θ), 13cos(θ) - 5cos(2θ) - 3cos(3θ) - cos(4θ), 1), θ, 0, 2π)
曲线((16sin³(θ), 13cos(θ) - 5cos(2θ) - 3cos(3θ) - cos(4θ), 1), θ, 0, 2π)
ParametricPlot[{6/25 cos[t] + 4/25 cos[3/2 t],
6/25 sin[t] - 4/25 sin[3/2 t]}, {t, 0, 4 Pi}, Axes -> False]
曲线(6 / 25 cos(θ) + 4 / 25 cos(3 / 2 θ), 6 / 25 sin(θ) - 4 / 25 sin(3 / 2 θ),1, θ, 0, 4π)

曲线((aθs[cos[t]]*cos[t] + aθs[sin[t]]*sin[t] + 1, aθs[cos[t]]*cos[t] - aθs[sin[t]]*sin[t] + 1),t,0,2π)

r=10+(3*sin(θ*2.5))^2 
 
x=r*cos(θ)
 
y=r*sin(θ) （0≤θ≤2π）
curve((cos(aθ)cos(θ),cos(aθ)sin(θ),θ,0,2pi))
curve((1+cos(k))cos(k),(1+cos(k))sin(k),k,0,2pi)
curve(10+(3*sin(θ*2.5)+1)^2*cos(θ),10+(3*sin(θ*2.5)+1)^2*sin(θ),θ,0,a)
'''

class Mobius_Strip_heartshape0(SpecialThreeDScene):

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
        heart_shape_mobius = ParametricSurface(lambda u, v: heart_curve_func(u) + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(-u/2) * OUT,
                                               u_min=-PI, u_max=PI, v_min=-r, v_max=r, resolution=(80, 12),
                                               checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.8,
                                               stroke_width=1.5, fill_color=average_color(RED, PINK), fill_opacity=0.8)

        heart_curve = ParametricFunction(heart_curve_func, t_min=-PI, t_max=PI, color=RED, stroke_width=10, stroke_opacity=0.9)

        self.play(ShowCreation(heart_curve))
        self.wait()

        self.play(ShowCreation(heart_shape_mobius))
        self.wait()

        heart_shape_mobius.add_updater(lambda m, dt: m.rotate(5 * DEGREES, axis=UP))

        self.wait(8)

class Mobius_Strip_fiveshape2(SpecialThreeDScene):

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

        five_curve_func = lambda t: ((3*np.sin(t*2.5))**2*np.cos(t)* RIGHT +
                                     (3*np.sin(t*2.5))**2*np.sin(t)* UP +
                                     1 * OUT) * 0.2
        r = 0.5
        five_shape_mobius = ParametricSurface(lambda u, v: five_curve_func(u) + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(-u/2) * OUT,
                                               u_min=-PI, u_max=PI, v_min=-r, v_max=r, resolution=(80, 12),
                                               checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.8,
                                               stroke_width=1.5, fill_color=average_color(RED, PINK), fill_opacity=0.8).scale(1.5)

        five_curve = ParametricFunction(five_curve_func, t_min=-PI, t_max=PI, color=RED, stroke_width=10, stroke_opacity=0.9).scale(1.5)
        self.play(ShowCreation(five_shape_mobius))
        self.wait()
        self.play(ShowCreation(five_curve))
        self.wait()

        #five_shape_mobius.add_updater(lambda m, dt: m.rotate(5 * DEGREES, axis=UP))
        #self.wait(8)