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
circle_init_point = np.array([0, 0, 0])
x_list = np.arange(-1, 6, 0.1)


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
        self.camera.move_to(RIGHT*3.5)

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
        points = np.array(points)+UP*2 +RIGHT*4
        rgbas = np.array(rgbas)
        mpoint.points = points.copy()
        mpoint.rgbas = rgbas.copy()


        self.time = 0
        self.image_pixel = pixel
        self.image_data = mpoint
        first=  mpoint.points[0]
        end = mpoint.points[-1]
        scale= (first-end)[0]/(2*PI)

        cylinder = Cylinder(radius=1,height=height, show_ends = False, checkerboard_colors = [BLUE_D])
        cylinder.rotate(axis=RIGHT, angle=PI / 2)

        cylinder.move_to(UP * height/2 +LEFT * abs(1))
        # cylinder.move_to()
        self.add(cylinder)
        self.add(mpoint)
        self.add(ThreeDAxes())
        cylinder_center = cylinder.get_center()
        def update_func(dt):
            self.time += dt
            rad=self.time
            current_points= mpoint.points.copy()
            for index, point in enumerate(mpoint.points):
                init_point = points[index]
                init_x = init_point[0]
                init_y = init_point[1]
                if rad >= init_x:
                    real_rad = rad - init_x
                    x = np.cos(real_rad/scale)+rad -1
                    z = np.sin(real_rad/scale)
                    new_point = np.array([x, init_y, z])
                    current_points[index] = new_point
            mpoint.points=current_points
            cx,cy,cz = cylinder.get_center()
            cylinder.move_to([cx+dt,cy,cz])

        self.add_updater(func=update_func)
        self.wait(2*PI*1.3)

    def projection_point(self, point, index, time):

        pass

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
