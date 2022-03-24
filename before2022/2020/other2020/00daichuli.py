from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

# 线性变换
class LinearTransformation(LinearTransformationScene):
    CONFIG = {
        "include_background_plane": True,
        "include_foreground_plane": True,
        "foreground_plane_kwargs": {
            "x_radius": FRAME_WIDTH,
            "y_radius": FRAME_HEIGHT,
            "secondary_line_ratio": 0
        },
        "background_plane_kwargs": {
            "color": GREY,
            "secondary_color": DARK_GREY,
            "axes_color": GREY,
            "stroke_width": 2,
        },
        "show_coordinates": False,
        "show_basis_vectors": True,
        "basis_vector_stroke_width": 6,
        "i_hat_color": X_COLOR,
        "j_hat_color": Y_COLOR,
        "leave_ghost_vectors": False,
    }

    def construct(self):
        mob = Circle()
        mob.move_to(RIGHT + UP * 2)
        vector_array = np.array([[1], [2]])
        matrix = [[0, 1], [-1, 1]]

        self.add_transformable_mobject(mob)

        self.add_vector(vector_array)

        self.apply_matrix(matrix)

        self.wait()
# 放大镜
class ZoomedSceneExample(ZoomedScene):
    CONFIG = {
        "zoom_factor": 0.3,
        "zoomed_display_height": 1,
        "zoomed_display_width": 6,
        "image_frame_stroke_width": 20,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 3,
        },
    }

    def construct(self):
        # Set objects
        dot = Dot().shift(UL * 2)

        image = ImageMobject(np.uint8([[0, 100, 30, 200],
                                       [255, 0, 5, 33]]))
        image.set_height(7)
        frame_text = TextMobject("Frame", color=PURPLE).scale(1.4)
        zoomed_camera_text = TextMobject("Zommed camera", color=RED).scale(1.4)

        self.add(image, dot)

        # Set camera
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(dot)
        frame.set_color(PURPLE)

        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(DOWN)

        # brackground zoomed_display
        zd_rect = BackgroundRectangle(
            zoomed_display,
            fill_opacity=0,
            buff=MED_SMALL_BUFF,
        )

        self.add_foreground_mobject(zd_rect)

        # animation of unfold camera
        unfold_camera = UpdateFromFunc(
            zd_rect,
            lambda rect: rect.replace(zoomed_display)
        )

        frame_text.next_to(frame, DOWN)

        self.play(
            ShowCreation(frame),
            FadeInFromDown(frame_text)
        )

        # Activate zooming
        self.activate_zooming()

        self.play(
            # You have to add this line
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera
        )

        zoomed_camera_text.next_to(zoomed_display_frame, DOWN)
        self.play(FadeInFromDown(zoomed_camera_text))

        # Scale in     x   y  z
        scale_factor = [0.5, 1.5, 0]

        # Resize the frame and zoomed camera
        self.play(
            frame.scale, scale_factor,
            zoomed_display.scale, scale_factor,
            FadeOut(zoomed_camera_text),
            FadeOut(frame_text)
        )

        # Resize the frame
        self.play(
            frame.scale, 3,
            frame.shift, 2.5 * DOWN
        )

        # Resize zoomed camera
        self.play(
            ScaleInPlace(zoomed_display, 2)
        )

        self.wait()

        self.play(
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera,
            # -------> Inverse
            rate_func=lambda t: smooth(1 - t),
        )
        self.play(
            Uncreate(zoomed_display_frame),
            FadeOut(frame),
        )
        self.wait()
# 数字移动显示
class UpdateNumber(Scene):
    def construct(self):
        number_line = NumberLine(x_min=-1, x_max=1)
        triangle = RegularPolygon(3, start_angle=-PI / 2) \
            .scale(0.2) \
            .next_to(number_line.get_left(), UP, buff=SMALL_BUFF)
        decimal = DecimalNumber(
            0,
            num_decimal_places=3,
            include_sign=True,
            unit="\\rm cm",  # Change this with None
        )

        decimal.add_updater(lambda d: d.next_to(triangle, UP * 0.1))
        decimal.add_updater(lambda d: d.set_value(triangle.get_center()[0]))
        #       You can get the value of decimal with: .get_value()

        self.add(number_line, triangle, decimal)

        self.play(
            triangle.shift, RIGHT * 2,
            rate_func=there_and_back,  # Change this with: linear,smooth
            run_time=5
        )

        self.wait()
#移动缩小同时进行
class MultipleAnimationVGroup(Scene):
  def construct(self):
    rect, circ = Rectangle(), Circle()
    vgroup = VGroup(rect, circ)

    def modify(vg):
      r, c = vg
      r.set_height(1)
      vg.arrange(DOWN, buff=0)
      return vg

    self.add(vgroup)
    self.play(
      ApplyFunction(modify, vgroup)
    )
    self.wait()
#边转边移动
class RotationAndMove(Scene):
    def construct(self):
        square1, square2 = VGroup(
                Square(color=RED), Square(color=BLUE)
            ).scale(0.5).set_x(-5)

        reference = DashedVMobject(Line(LEFT*5,RIGHT*5,color=GRAY))
        self.add(square1,square2,reference)

        self.play(
                # Red square
                square1.rotate,3*PI,
                square1.move_to, [5,0,0],
                # Blue square
                ShiftAndRotate(square2, RIGHT*10, 3*PI),
                run_time=4
            )
        self.wait()
#沿着曲线
class RotateWithPath(Scene):
    def construct(self):
        square1, square2 = VGroup(
                Square(color=RED), Square(color=BLUE)
            ).scale(0.5).set_x(-5)

        path = Line(LEFT*5,RIGHT*5,stroke_opatity=0.5)
        path.points[1:3] += UP*2

        square2.save_state()
        def update_rotate_move(mob,alpha):
            square2.restore()
            square2.move_to(path.point_from_proportion(alpha))
            square2.rotate(3*PI*alpha)

        self.add(square1,square2,path)
        self.play(
                # Red square
                MoveAlongPath(square1,path),
                Rotate(square1,2*PI/3,about_point=square1.get_center()),
                # Blue square
                UpdateFromAlphaFunc(square2,update_rotate_move),
                run_time=4
            )
        self.wait()


