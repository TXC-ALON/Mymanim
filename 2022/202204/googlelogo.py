from manimlib import *
import numpy as np

Google_BLUE = '#4285F4'
Google_RED = '#DB4437'
Google_YELLOW = '#F4B400'
Google_GREEN = '#0F9D58'
class testcolor(Scene):
    def setup(self):
        cir1 = Circle().set_color(Google_BLUE).move_to(LEFT * 2)
        cir2 = Circle().set_color(Google_RED).move_to(LEFT * 1)
        cir3 = Circle().set_color(Google_YELLOW).move_to(LEFT * -1)
        cir4 = Circle().set_color(Google_GREEN).move_to(LEFT * -2)
        cir = VGroup(cir1,cir2,cir3,cir4)
        self.play(ShowCreation(cir),run_time = 4)
        self.wait()
