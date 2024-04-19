import math

import moderngl
from scipy.interpolate import interp2d

from manim import *
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_mobject import OpenGLMobject, OpenGLPoint
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
from PIL import Image

from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVMobject


class CircleRun(Scene):
    def construct(self):
        axes = Axes()
        circle = Circle(radius=1).shift(UP)
        dot = Dot().move_to(circle.get_right())
        self.add(circle, dot, axes)
        self.wait()

        # animate= MoveToTarget(circle, TAU, about_point=circle.get_center(), rate_func=linear)
        target_position = circle.get_center() + RIGHT * 2 * PI
        animate = circle.animate.move_to(target_position)

        value_tracker = ValueTracker()
        value_tracker_animate = value_tracker.animate.set_value(2 * PI)

        def updata_func(dot: Dot, dt):
            deg = np.rad2deg(value_tracker.get_value() * PI / 180)
            x = value_tracker.get_value() + np.cos(deg)
            y = np.sin(deg)
            dot.move_to([x, y+1, 0])

        dot_animate = UpdateFromAlphaFunc(dot, update_function=updata_func)

        path = TracedPath(dot.get_center, stroke_color=dot.get_color(), stroke_width=2.0)
        self.add(path)

        self.play(animate, value_tracker_animate, dot_animate, run_time=3)








class ProjectionDemo(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=75 * DEGREES, theta=15 * DEGREES)
        image_obj = OpenGLImageMobject("mini.jpg")
        self.add(image_obj.shift(UP * 2))
        # self.wait(2)

        image = Image.open("mini.jpg").convert("RGBA")
        image_data = np.array(image)

        h, w, _ = image_data.shape
        width = image_obj.width
        height = image_obj.height
        # 每个图片像素 在平面上的长度，宽度
        pixel = width / w

        points = []
        rgbas = []
        for i in range(h):
            for j in range(w):
                data = image_data[i, j] / 255
                x, y = self.image_coor_to_screen_coor([j, i], h, w)
                screen_point = np.array([x, y, 0]) * pixel
                points.append(screen_point)
                rgbas.append(data)

        mpoint = OpenGLPMPoint(stroke_width=2)
        mpoint.points = np.array(points)
        mpoint.rgbas = np.array(rgbas)
        self.add(mpoint.next_to(image_obj, direction=DOWN))

    def image_coor_to_screen_coor(self, point: np.ndarray, height: int, width: int):
        """
        把图片坐标，转到 manim 的平面坐标
        """
        y = -(point[1] - height / 2)
        x = point[0] - width / 2
        return (int(x), int(y))


# "renderer": "opengl"  "background_color":"WHITE",
with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    CircleRun().render()
    exit(1)
