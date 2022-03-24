from manimlib.imports import *
from Z.Z import *

# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class NumberCreation(Scene):

    def construct(self):
        # object
        creature = SVGMobject("Z_plain").scale(2)
        creature[4].set_color("#FFF252")
        # position

        # show
        self.add(creature)



class Z(Scene):
    def construct(self):
        Ale = Alex().to_edge(DOWN)
        palabras_ale = TextMobject("Learn to do \\\\animations with me!!")
        self.add(Ale)
        self.play(ZSays(
            Ale, palabras_ale,
            bubble_kwargs={"height": 4, "width": 6},
            target_mode="speaking"
        ))
        self.wait()
        self.play(Blink(Ale))
        self.wait(1)
        self.play(Blink(Ale))
        self.wait(1)
        self.play(Blink(Ale))
        self.wait(1)
        self.play(Blink(Ale))
        self.wait(1)