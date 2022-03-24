from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class cube(ThreeDScene):

    def construct(self):
# object
        cube = Cube(color=PINK, fill_opacity=0.0, stroke_width=4, stroke_color=YELLOW).scale(1)
        axes  = ThreeDAxes()
# position
        #self.move_camera(phi=75 * DEGREES, theta=-60 * DEGREES, distance=10, run_time=3)
# show
        print(len(cube))
        cube[0].set_color(RED)
        cube[1].set_color(ORANGE)
        cube[2].set_color(YELLOW)
        cube[3].set_color(GREEN)
        cube[4].set_color(BLUE)
        cube[5].set_color(PURPLE)

        #self.add(axes,cube)
        debugPoints(self,cube)

        self.play(ShowCreation(cube),run_time = 4)

class cube10(ThreeDScene):

    def construct(self):
        self.move_camera(phi=75 * DEGREES, theta=-60 * DEGREES, distance=10)
        axes = ThreeDAxes()
        self.add(axes)
        '''
        for vect in IN, OUT, LEFT, RIGHT, UP, DOWN:
            face = Square(
                side_length=2,
                shade_in_3d=True,
            )
            face.flip()
            face.shift(2 * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))

            self.add(face)
        '''

        face = Square(side_length=2, shade_in_3d=True).set_color(RED)
        dot = Dot3d().move_to(face.points[0]).set_color(BLUE_D)
        dot.add_updater(lambda c: c.move_to(face.points[0]))
        face.flip()
        self.add(face, dot)
        self.play(face.flip, run_time=1)
        self.wait()
        self.play(face.shift, OUT, run_time=1)
        self.wait()
        face_2 = face.copy().apply_matrix(z_to_vector(IN))
        self.play(ReplacementTransform(face, face_2))
        self.wait(2)

        face2 = Square(side_length=2, shade_in_3d=True).set_color(ORANGE)
        dot2 = Dot3d().move_to(face.points[0]).set_color(BLUE_D)
        dot2.add_updater(lambda c: c.move_to(face2.points[0]))
        face2.flip()
        self.add(face2, dot2)
        self.play(face2.flip, run_time=1)
        self.wait()
        self.play(face2.shift, OUT, run_time=1)
        self.wait()
        face2_2 = face2.copy().apply_matrix(z_to_vector(OUT))
        self.play(ReplacementTransform(face2, face2_2))
        self.wait(2)

        face3 = Square(side_length=2, shade_in_3d=True).set_color(YELLOW)
        dot3 = Dot3d().move_to(face.points[0]).set_color(BLUE_D)
        dot3.add_updater(lambda c: c.move_to(face3.points[0]))
        face3.flip()
        self.add(face3, dot3)
        self.play(face3.flip, run_time=1)
        self.wait()
        self.play(face3.shift, OUT, run_time=1)
        self.wait()
        face3_2 = face3.copy().apply_matrix(z_to_vector(LEFT))
        self.play(ReplacementTransform(face3, face3_2))
        self.wait(2)

        face4 = Square(side_length=2, shade_in_3d=True).set_color(GREEN)
        dot4 = Dot3d().move_to(face.points[0]).set_color(PURPLE)
        dot4.add_updater(lambda c: c.move_to(face4.points[0]))
        face4.flip()
        self.add(face4, dot4)
        self.play(face4.flip, run_time=1)
        self.wait()
        self.play(face4.shift, OUT, run_time=1)
        self.wait()
        face4_2 = face4.copy().apply_matrix(z_to_vector(RIGHT))
        self.play(ReplacementTransform(face4, face4_2))
        self.wait(2)

        face5 = Square(side_length=2, shade_in_3d=True).set_color(PINK)
        dot5 = Dot3d().move_to(face.points[0]).set_color(PURPLE)
        dot5.add_updater(lambda c: c.move_to(face5.points[0]))
        face5.flip()
        self.add(face5, dot5)
        self.play(face5.flip, run_time=1)
        self.wait()
        self.play(face5.shift, OUT, run_time=1)
        self.wait()
        face5_2 = face5.copy().apply_matrix(z_to_vector(UP))
        self.play(ReplacementTransform(face5, face5_2))
        self.wait(2)

        face6 = Square(side_length=2, shade_in_3d=True).set_color(BLUE)
        dot6 = Dot3d().move_to(face.points[0]).set_color(PURPLE)
        dot6.add_updater(lambda c: c.move_to(face6.points[0]))
        face6.flip()
        self.add(face6, dot6)
        self.play(face6.flip, run_time=1)
        self.wait()
        self.play(face6.shift, OUT, run_time=1)
        self.wait()
        face6_2 = face6.copy().apply_matrix(z_to_vector(DOWN))
        self.play(ReplacementTransform(face6, face6_2))
        self.wait(2)

        #debugPoints(self,face)
