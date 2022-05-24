from manimlib import *
import numpy as np


class Scene1(Scene):
    def setup(self):
        tex_config = {
            "isolate" : "\\circ",
            "tex_to_color_map" : {
                "A" : Google_RED,
                "B":Google_GREEN,
                "C" :Google_YELLOW
            }

        }
        tex1 = MTex("\\left( A \\circ B \\right) \\circ C", **tex_config)
        tex2 = MTex("A \\circ \\left( B \\circ C \\right)", **tex_config)
        self.play(ShowCreation(tex1))
        self.wait
        self.play(TransformMatchingStrings(tex1,tex2),run_time = 3)
        self.wait