import math

import moderngl
from scipy.interpolate import interp2d

from manim import *
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_mobject import OpenGLMobject, OpenGLPoint
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
from PIL import Image

circle_r = 1
move_speed = 1
circle_init_point = np.array([0, 0, 0])
x_list = np.arange(-1, 5, 0.5)


class LineToCircle(Scene):
    def construct(self):

        self.show001()

    def show001(self):

        self.camera.move_to(RIGHT * 2)

        circle = Circle(radius=circle_r)
        line = NumberLine(include_ticks=False, x_range=[-10, 10])
        dot_list = [Dot(point=[x + circle_r, 0, 0], radius=0.04) for x in x_list]
        path_list = [TracedPath(dot.get_center) for dot in dot_list]

        self.add(circle, line, *dot_list, *path_list)

        self.time = 0

        def upadate_func(dt):
            self.time += dt

            circle_point = circle_init_point + np.array([self.time, 0, 0])
            circle.move_to(circle_point)

            for index, dot in enumerate(dot_list):
                update_dot(dot, x_list[index], self.time)

        def update_dot(dot: Dot, init_x, rad):
            if rad >= init_x:
                real_rad = rad - init_x
                x = np.cos(-real_rad) + real_rad
                y = np.sin(-real_rad)
                new_point = np.array([x + init_x, y, 0])
                dot.move_to(new_point)

        self.add_updater(func=upadate_func)
        self.wait(2 * PI)


points = []
rgbas = []


class ProjectionDemo(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=15 * DEGREES)
        self.camera.move_to(RIGHT * 3.5)

        circle = Circle(radius=circle_r)
        image_obj = OpenGLImageMobject("mini.jpg")
        # self.add(image_obj.shift(UP * 2))
        # self.wait(2)
        self.add(circle)

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
        points = np.array(points) + UP * 2 + RIGHT * 4
        rgbas = np.array(rgbas)
        mpoint.points = points.copy()
        mpoint.rgbas = rgbas.copy()

        self.time = 0
        self.image_pixel = pixel
        self.image_data = mpoint
        first = mpoint.points[0]
        end = mpoint.points[-1]
        scale = (first - end)[0] / (2 * PI)

        cylinder = Cylinder(radius=1, height=height, show_ends=False, checkerboard_colors=[BLUE_D])
        cylinder.rotate(axis=RIGHT, angle=PI / 2)

        cylinder.move_to(UP * height / 2 + LEFT * abs(1))
        # cylinder.move_to()
        self.add(cylinder)
        self.add(mpoint)
        self.add(ThreeDAxes())
        cylinder_center = cylinder.get_center()

        def update_func(dt):
            self.time += dt
            rad = self.time
            current_points = mpoint.points.copy()
            for index, point in enumerate(mpoint.points):
                init_point = points[index]
                init_x = init_point[0]
                init_y = init_point[1]
                if rad >= init_x:
                    real_rad = rad - init_x
                    x = np.cos(real_rad / scale) + rad - 1
                    z = np.sin(real_rad / scale)
                    new_point = np.array([x, init_y, z])
                    current_points[index] = new_point
            mpoint.points = current_points
            cx, cy, cz = cylinder.get_center()
            cylinder.move_to([cx + dt, cy, cz])

        self.add_updater(func=update_func)
        self.wait(2 * PI * 1.3)

    def projection_point(self, point, index, time):

        pass

    def image_coor_to_screen_coor(self, point: np.ndarray, height: int, width: int):
        """
        把图片坐标，转到 manim 的平面坐标
        """
        y = -(point[1] - height / 2)
        x = point[0] - width / 2
        return (int(x), int(y))


class ProjectionRefactor(ThreeDScene):
    def construct(self):
        # self.show001()
        # self.show002()
        # self.show003()
        # self.show004()
        self.show005()

    def show001(self):
        circle = Circle(radius=1)
        axes = ThreeDAxes(x_range=[-5, 5, 1], y_range=[-3, 3, 1])
        dot = Dot()
        image_mobj = OpenGLImageMobject("world-daytime.jpg")
        self.add(image_mobj, circle, axes, dot)

    def show002(self):
        image_obj = OpenGLImageMobject("mini.jpg")

        image = Image.open("mini.jpg").convert("RGBA")
        image_data = np.array(image)
        height, width = image_data.shape[:2]
        # 单个像素的长度
        pixel_width = image_obj.width / width
        # 需要把图片数据，转成对应的坐标点&&点对应的rgba颜色
        y_indices, x_indices = np.mgrid[0:height, 0:width]
        points = np.zeros((height * width, 3))
        points[:, 0] = x_indices.flatten()  # x坐标
        points[:, 1] = y_indices.flatten()  # y坐标
        # 创建一个颜色数组，每个颜色是一个(r, g, b, a)四元组
        rgbas = image_data.reshape(-1, 4)
        point_obj = OpenGLPMPoint(stroke_width=2)
        # 坐标点的处理: 每个坐标进行缩放 && y轴翻转
        point_obj.points = points * pixel_width * [1, -1, 1]
        # 颜色的处理 / 255
        point_obj.rgbas = rgbas / 255
        self.add(point_obj)

    def show003(self):
        circle = Circle(radius=1)
        axes = ThreeDAxes(x_range=[-5, 5, 1], y_range=[-3, 3, 1])
        dot = Dot().shift(RIGHT)
        dot_path = TracedPath(dot.get_center)
        self.add(circle, axes, dot, dot_path)
        self.time = 0

        def update_func(dt):
            self.time += dt;
            distance = move_speed * self.time
            circle.move_to([distance, 0, 0])
            # rad 弧长是有放心的，默认逆时针
            rad = distance / circle_r
            x = np.cos(-rad) + distance
            y = np.sin(-rad)
            point = [x, y, 0]
            dot.move_to(point)

        self.add_updater(func=update_func)
        self.wait(2 * PI * circle_r)

    def show004(self):
        circle = Circle(radius=1)
        axes = ThreeDAxes(x_range=[-5, 5, 1], y_range=[-3, 3, 1])
        dot_list = [Dot(point=[x + circle_r, 0, 0], stroke_width=1) for x in x_list]
        dot_path_list = [TracedPath(dot.get_center, stroke_width=1) for dot in dot_list]
        self.add(circle, axes, *dot_list, *dot_path_list)
        self.time = 0

        def update_func(dt):
            self.time += dt;
            distance = move_speed * self.time
            circle.move_to([distance, 0, 0])
            for index, dot in enumerate(dot_list):
                init_x = x_list[index]
                if distance >= init_x:
                    # rad 弧长是有放心的，默认逆时针
                    read_rad = (distance - init_x) / circle_r
                    x = np.cos(-read_rad) + distance
                    y = np.sin(-read_rad)
                    point = [x, y, 0]
                    dot.move_to(point)

        self.add_updater(func=update_func)
        self.wait(2 * PI * circle_r)

    def show005(self):
        image_obj = OpenGLImageMobject("mini.jpg")
        self.add(image_obj)
        self.wait(2)
        axes = ThreeDAxes()
        self.add(axes)
        self.move_camera(65 * DEGREES, 15 * DEGREES)
        self.remove(image_obj)

        image = Image.open("mini.jpg").convert("RGBA")
        image_data = np.array(image)
        height, width = image_data.shape[:2]
        # 单个像素的长度
        pixel_width = image_obj.width / width
        # 需要把图片数据，转成对应的坐标点&&点对应的rgba颜色
        y_indices, x_indices = np.mgrid[0:height, 0:width]
        points = np.zeros((height * width, 3))
        points[:, 0] = x_indices.flatten()  # x坐标
        points[:, 1] = y_indices.flatten()  # y坐标
        # 创建一个颜色数组，每个颜色是一个(r, g, b, a)四元组
        rgbas = image_data.reshape(-1, 4)
        point_obj = OpenGLPMPoint(stroke_width=2)
        # 坐标点的处理: 每个坐标进行缩放 && y轴翻转
        point_obj.points = points * pixel_width * [1, -1, 1]
        # 颜色的处理 / 255
        point_obj.rgbas = rgbas / 255

        self.set_camera_orientation(65 * DEGREES, 15 * DEGREES)
        self.camera.move_to(RIGHT * 2)


        self.time = 0
        self.is_end = False
        init_points = point_obj.points.copy()
        circle_r = image_obj.width / (2 * PI)
        cylinder = Cylinder(radius=circle_r, height=image_obj.height, show_ends=False, checkerboard_colors=[GREY])
        cylinder.rotate(axis=RIGHT, angle=PI / 2)
        cylinder.move_to(DOWN * image_obj.height / 2 + LEFT * circle_r)
        # self.add(cylinder)
        self.add(point_obj)

        self.begin_ambient_camera_rotation(rate=0.8)
        self.play(point_obj.animate.scale(4),run_time=3)
        self.wait(1)
        self.play(point_obj.animate.scale(1/4), run_time=2)
        self.wait(1.8)
        self.stop_ambient_camera_rotation()


        def update_func(dt):
            if self.is_end:
                return
            self.time += dt
            distance = move_speed * self.time
            current_points = point_obj.points.copy()
            for index, point in enumerate(point_obj.points):
                init_x, init_y = init_points[index][:2]
                if distance >= init_x:
                    real_rad = (distance - init_x) / circle_r
                    x = circle_r * np.cos(-real_rad) + distance - circle_r
                    z = circle_r * np.sin(-real_rad)
                    new_point = np.array([x, init_y, z])
                    current_points[index] = new_point
            point_obj.points = current_points
            cx, cy, cz = cylinder.get_center()
            cylinder.move_to([cx + dt, cy, cz])

        self.add_updater(func=update_func)
        self.wait(2 * PI * circle_r)
        self.is_end = True
        ani= self.camera.animate.move_to(RIGHT * 4)
        self.play(ani)
        self.move_camera(75 * DEGREES, theta=135 * DEGREES,run_time=2)


# "renderer": "opengl"  "background_color":"WHITE",
with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    ProjectionRefactor().render()
    exit(1)
