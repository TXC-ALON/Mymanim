from manimlib.imports import *
from amanimza.Alexander.MyAnimations.box.box_object import *
#from big_ol_pile_of_manim_imports import *
from manimlib.imports import *

class Box(VMobject):
    CONFIG={
        "width":3,
        "height":2,
        "stroke_color":"#D2B48C",
        "fill_color":"#cdab7e",
        "size_lid":0.95,
        "lid_width":11,
    }
    def __init__(self):
        VMobject.__init__(self)
        self.set_points_as_corners([UP*self.height+LEFT*self.width/2,
                                LEFT*self.width/2,
                                RIGHT*self.width/2,
                                UP*self.height+RIGHT*self.width/2])
        self.set_stroke(width=6)
        tapaI=VMobject().set_points_as_corners([self.points[0],self.points[0]+RIGHT*self.width*self.size_lid/2]).set_stroke(width=self.lid_width)
        tapaD=VMobject().set_points_as_corners([self.points[-1],self.points[-1]+LEFT*self.width*self.size_lid/2]).set_stroke(width=self.lid_width)
        self.add(tapaI,tapaD)
        self.set_stroke(self.stroke_color)
        self.set_fill(self.fill_color,1)

    def tapa_derecha(self):
        return self[2]

    def tapa_izquierda(self):
        return self[1]

    def box_center(self):
        rect=Rectangle(height=self.height,width=self.width)
        rect.move_to(self[0],aligned_edge=DOWN)
        return rect.get_center()

class open_box(Animation):
    CONFIG = {
        "run_time": 0.75,
        "rate_func": smooth,
    }

    def interpolate_mobject(self, alpha):
        self.mobject.become(self.starting_mobject)
        sobre_izq=self.mobject.points[0]
        sobre_der=self.mobject.points[-1]
        self.mobject[1].rotate(
            alpha * PI*2.3/2,
            about_point=sobre_izq,
            about_edge=sobre_izq,
        )
        self.mobject[2].rotate(
            -alpha * PI*2.3/2,
            about_point=sobre_der,
            about_edge=sobre_der,
        )

class close_box(Animation):
    CONFIG = {
        "run_time": 0.75,
        "rate_func": smooth,
    }

    def interpolate_mobject(self, alpha):
        self.mobject.become(self.starting_mobject)
        sobre_izq=self.mobject.points[0]
        sobre_der=self.mobject.points[-1]
        self.mobject[1].rotate(
            -alpha * PI*2.3/2,
            about_point=sobre_izq,
            about_edge=sobre_izq,
        )
        self.mobject[2].rotate(
            alpha * PI*2.3/2,
            about_point=sobre_der,
            about_edge=sobre_der,
        )

class NoteBox(ImageMobject):
    def __init__(self):
        ImageMobject.__init__(self,filename_or_array="note_box.png")


class BoxAnimation(Scene):
    def construct(self):
        # Set objects
        box = Box()
        note = NoteBox()
        label = TexMobject("A", color=BLACK)
        # Set properties
        note.set_height(label.get_height() * 2)
        note.move_to(box)
        label.move_to(note)

        self.play(DrawBorderThenFill(box))
        self.wait()
        self.play(FadeIn(note))
        note.add_updater(lambda d: d.move_to(box.box_center()))
        self.play(Write(label))
        label.add_updater(lambda d: d.move_to(note))

        self.play(box.shift, DOWN * 3 + LEFT * 2, path_arc=PI / 4)
        self.wait()
        self.play(open_box(box))

        self.play(box.shift, UP * 4.5 + RIGHT * 4)
        self.wait()
        self.play(close_box(box))
        self.wait()


