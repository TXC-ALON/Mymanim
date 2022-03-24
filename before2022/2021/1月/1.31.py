from manim_sandbox.utils.imports import *
from manimlib.imports import *

class colored_ring(Scene):
    def construct(self):
        n = 36
        angles = [TAU / n for i in range(1, n + 1)]
        ring = Arcs(colors=[RED, BLUE, GREEN, YELLOW, RED], angle_list=angles, radius=2.5, stroke_width=50)
        self.add(ring)
        self.wait(3)

class Colored_ring2(Scene):
    def construct(self):
        n = 36
        angles = [[TAU/k/5 for i in range(5*k)] for k in range(1, 51)]
        ring = Arcs(colors=[RED, BLUE, GREEN, YELLOW, RED], angle_list=angles[0],
                    radius=2.5, stroke_width=50)
        self.play(ShowCreation(ring))
        self.wait(0.5)
        for i in range(1, 50):
            ring_new = Arcs(colors=[RED, BLUE, GREEN, YELLOW, RED], angle_list=angles[i],
                       radius=2.7, stroke_width=80)
            self.play(ReplacementTransform(ring, ring_new), run_time=0.5)
            self.wait(0.1)
        self.wait(2)