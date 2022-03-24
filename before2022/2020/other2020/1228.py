from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class TypesOfText2(Scene):
    def construct(self):
        typesOfText = TextMobject("""
            This is a regular text,
            $\\frac{x}{y}$,
            $x^2+y^2=a^2$
            $$x^2+y^2=a^2$$
            """)
        self.play(Write(typesOfText))
        self.wait(3)
        
# object

# position

# show

