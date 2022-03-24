from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L
def HSL(hue, saturation=1, lightness=0.5):
    return Color(hsl=(hue, saturation, lightness))


class gra_annulus(Scene):

    def construct(self):
        # object
        gradient_annulus = Annulus(
            outer_radius=3,
            inner_radius=2.5,
            fill_opacity=1,
            # Gradient direction
            sheen_direction=RIGHT,
            stroke_width=0
        )
        gradient_annulus.set_color(color=self.get_hsl_set_colors())
        # position

        # show
        self.add(gradient_annulus)
        self.wait(3)

    def get_hsl_set_colors(self, saturation=1, lightness=0.5):
        return [*[HSL(i / 360, saturation, lightness) for i in range(360)]]
