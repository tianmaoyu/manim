import math

import moderngl
from scipy.interpolate import interp2d

from manim import *
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_mobject import OpenGLMobject, OpenGLPoint
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
from PIL import Image


class CircleRun(Scene):
    def construct(self):
        # self.show_001()
        # self.show_002()
        self.show_004()

    def show_001(self):
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
            dot.move_to([x, y + 1, 0])

        dot_animate = UpdateFromAlphaFunc(dot, update_function=updata_func)

        path = TracedPath(dot.get_center, stroke_color=dot.get_color(), stroke_width=2.0)
        self.add(path)

        self.play(animate, value_tracker_animate, dot_animate, run_time=3)

    def show_002(self):
        axes = Axes()
        circle = Circle(radius=1).shift(UP)
        dot = Dot()
        self.add(circle, dot, axes)
        self.wait()

        # animate= MoveToTarget(circle, TAU, about_point=circle.get_center(), rate_func=linear)
        target_position = circle.get_center() + RIGHT * 2 * PI
        animate = circle.animate.move_to(target_position)

        value_tracker = ValueTracker()
        value_tracker.set_value(-1 / 2 * PI)
        value_tracker_animate = value_tracker.animate.increment_value(2 * PI)

        def updata_func(dot: Dot, dt):
            rad = value_tracker.get_value()
            # 不是从 0开始，要初始的距离差差 s=rad*r， y 也要移动
            s = (rad + PI / 2)
            x = np.cos(rad) + s
            y = np.sin(rad)
            dot.move_to([x, y + 1, 0])

        dot_animate = UpdateFromAlphaFunc(dot, update_function=updata_func)

        path = TracedPath(dot.get_center, stroke_color=dot.get_color(), stroke_width=2.0)
        self.add(path)

        self.play(animate, value_tracker_animate, dot_animate, run_time=3)

    def show_003(self):
        self.camera.move_to(RIGHT * 2)
        axes = Axes(x_range=[-10, 10], x_length=20)
        circle = Circle(radius=1)
        dot = Dot().move_to(circle.get_right())
        self.add(circle, dot, axes)
        self.wait()

        target_position = circle.get_center() + RIGHT * 2 * PI
        animate = circle.animate.move_to(target_position)

        value_tracker = ValueTracker()
        value_tracker_animate = value_tracker.animate.increment_value(2 * PI)

        def updata_func(dot: Dot, dt):
            rad = value_tracker.get_value()
            x = np.cos(rad) + rad
            y = np.sin(rad)
            dot.move_to([x, y, 0])

        dot_animate = UpdateFromAlphaFunc(dot, update_function=updata_func)

        path = TracedPath(dot.get_center, stroke_color=dot.get_color(), stroke_width=2.0)
        self.add(path)

        self.play(animate, value_tracker_animate, dot_animate, run_time=3)

    #顺时针旋转
    def show_004(self):
        self.camera.move_to(RIGHT * 2)
        axes = Axes(x_range=[-10, 10], x_length=20)
        circle = Circle(radius=1)
        dot = Dot().move_to(circle.get_right())
        self.add(circle, dot, axes)
        self.wait()

        target_position = circle.get_center() + RIGHT * 2 * PI
        animate = circle.animate.move_to(target_position)

        value_tracker = ValueTracker()
        value_tracker_animate = value_tracker.animate.increment_value(-2 * PI)

        def updata_func(dot: Dot, dt):
            rad = value_tracker.get_value()
            x = np.cos(rad) - rad
            y = np.sin(rad)
            dot.move_to([x, y, 0])

        dot_animate = UpdateFromAlphaFunc(dot, update_function=updata_func)

        path = TracedPath(dot.get_center, stroke_color=dot.get_color(), stroke_width=2.0)
        self.add(path)

        self.play(animate, value_tracker_animate, dot_animate, run_time=3)

R=1

class LineToCircle(Scene):
    def construct(self):
        # self.show001()
        self.show003()

    def show001(self):
        circle = Circle()
        # circle.move_to(UP)
        line = NumberLine(include_ticks=False)
        self.add(circle, line)
        dot_list = []
        for item in np.arange(0, 5, 0.5):
            point = RIGHT * item
            dot = Dot(point=point)
            dot_list.append(dot)

        self.add(*dot_list)

        move_animate = circle.animate.move_to(RIGHT * 2 * PI)
        value_tracker = ValueTracker()
        value_tracker_animate = value_tracker.animate.increment_value(TAU)
        path = TracedPath(dot_list[0].get_center, stroke_color=dot_list[0].get_color(), stroke_width=2.0)
        self.add(path)

        def update_func(obj: Dot, dt):
            rad = value_tracker.get_value()
            center = obj.get_center()
            if center[0] - 1 <= rad:
                obj.start_run = True
            if hasattr(obj, "start_run"):
                x = np.cos(rad)
                y = np.sin(rad)
                obj.move_to([x, y, 0])

        update_animates = []
        for dot in dot_list:
            animate = UpdateFromAlphaFunc(dot, update_function=update_func)
            update_animates.append(animate)

        self.play(move_animate, update_animates, value_tracker_animate, run_time=2)

    def show002(self):
        circle = Circle()
        circle.move_to(LEFT)
        line = NumberLine(include_ticks=False)
        self.add(circle, line)

        dot_list = []
        for item in np.arange(0, 5, 0.5):
            point = RIGHT * item
            dot = Dot(point=point)
            dot_list.append(dot)

        dot=dot_list[4]
        self.add(dot)

        move_animate = circle.animate.move_to(RIGHT * 2 * PI)
        value_tracker = ValueTracker()
        value_tracker_animate = value_tracker.animate.increment_value(TAU)

        path= TracedPath(dot.get_center, stroke_color=dot.get_color(), stroke_width=2.0)
        self.add(path)

        def update_func(obj: Dot, dt):
            rad = value_tracker.get_value()
            center = obj.get_center()
            dif_rad= center[0]
            print(f"dif:{dif_rad} x:{center[0]}y:{center[1]}")
            if not hasattr(obj, "start_run"):
                obj.start_run = True
                obj.start_center = center
                obj.start_dif_rad = dif_rad
            elif dif_rad <= rad:
                x = np.cos(rad - obj.start_dif_rad)
                y = np.sin(rad - obj.start_dif_rad)
                obj.move_to([x, y, 0])

        self.time=0
        def func(dt):
            self.time+=dt
            print("self------", self.time)
        self.add_updater(func=func)


        animate = UpdateFromAlphaFunc(dot, update_function=update_func)

        self.play(move_animate, animate, value_tracker_animate, run_time=2)

    def show003(self):
        circle = Circle(radius=R)
        circle.move_to(UP)
        line = NumberLine(include_ticks=False)
        self.add(circle, line)

        dot_list = []
        for item in np.arange(0, 5, 0.5):
            point = RIGHT * item
            dot = Dot(point=point)
            dot_list.append(dot)

        dot = dot_list[4]
        self.add(dot)

        move_animate = circle.animate.move_to(UP+RIGHT * 2 * PI)
        value_tracker = ValueTracker()
        value_tracker_animate = value_tracker.animate.increment_value(-TAU)

        path = TracedPath(dot.get_center, stroke_color=dot.get_color(), stroke_width=2.0)
        self.add(path)


        def update_func(obj: Dot, dt):
            rad = value_tracker.get_value()
            center = obj.get_center()
            dif_rad = center[0]
            print(f"dif:{dif_rad} ,rad:{rad} x:{center[0]}y:{center[1]}")
            if not hasattr(obj, "start_run"):
                obj.start_run = True
                obj.start_center = center
                obj.start_dif_rad = dif_rad
            elif -(obj.start_dif_rad)<= -rad :
                x = np.cos(rad)- rad
                y = np.sin(rad)
                obj.move_to([x, y, 0])

        self.time = 0
        # def func(dt):
        #     self.time += dt
        #     print("self------", self.time)
        # self.add_updater(func=func)

        animate = UpdateFromAlphaFunc(dot, update_function=update_func)
        self.play(move_animate, animate, value_tracker_animate, run_time=2)


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
    ProjectionDemo().render()
    exit(1)
