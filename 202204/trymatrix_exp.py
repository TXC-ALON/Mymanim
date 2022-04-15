from manim_imports_ext import *

class VideoWrapper(Scene):
    title = "hello"

    def construct(self):
        self.add(FullScreenRectangle())
        screen_rect = ScreenRectangle(height=6)
        screen_rect.set_stroke(BLUE_D, 1)
        screen_rect.set_fill(BLACK, 1)
        screen_rect.to_edge(DOWN)
        self.add(screen_rect)

        title = TexText(self.title, font_size=90)
        if title.get_width() > screen_rect.get_width():
            title.set_width(screen_rect.get_width())
        title.next_to(screen_rect, UP)

        self.play(Write(title))
        self.wait()