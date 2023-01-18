from manimlib import *
import numpy as np


class S1(Scene):
    def setup(self):
        de_words = Tex("A^2", "+", "B^2", "=", "C^2")
        de_words.set_x(-3).to_edge(UP)
        self.play(ShowCreation(de_words),run_time = 3)
        self.wait()