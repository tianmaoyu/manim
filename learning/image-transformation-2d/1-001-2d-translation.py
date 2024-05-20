import random
import time

from manim import *
from manim.mobject.opengl.opengl_cylinder import OpenGLCylinder
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject
from manim.mobject.opengl.opengl_shpere import OpenGLSphere
from manim.mobject.opengl.opengl_something import OpenGLCone, OpenGLLine3D
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np

from manim.typing import Image


class NumpyImage(OpenGLPMobject):
    def __init__(self, image_array: np.ndarray, **kwargs):
        super().__init__(**kwargs, stroke_width=4.0,depth_test=True)

        # 构建三维坐标
        height, width,channel = image_array.shape
        assert channel==4,"必须是r,g,b,a"
        points = np.zeros((height * width, 3))
        y_indices, x_indices = np.mgrid[0:height, 0:width]
        points[:, 0] = x_indices.flatten()  # x坐标
        points[:, 1] = y_indices.flatten()  # y坐标
        rgbas = image_array.reshape(-1, 4)
        scale= 0.025
        #y轴反转和缩小- 一个坐标间隔为1
        points=points * scale * np.array([1, -1, 1])
        # 居中
        points += np.array([-width* scale / 2, height* scale / 2, 0])
        self.points =points
        self.rgbas = rgbas / 255

    def to_center(self):
        height, width = self.init_image.shape[:2]
        self.points = self.points + np.array([-width / 2, height / 2, 0]) * 0.025
        return self


class Translation001(ThreeDScene):
    def construct(self):
        image = ImagePixelMobject("src/mini.jpg")
        image.to_center()
        self.add(image)

        self.move_camera(phi=45 * DEGREES, theta=15 * DEGREES, run_time=2)
        image.points
        self.time = 0

        def update_func(dt):
            self.time += dt
            n_to_select = 500
            select_indices = np.random.choice(image.points.shape[0], n_to_select, replace=False)
            selected_points = image.points[select_indices]
            selected_points[:, 2] += np.random.randint(low=0, high=2)
            image.points[select_indices, 2] = selected_points[:, 2]

        self.add_updater(func=update_func)
        self.wait(4)


class Translation002(ThreeDScene):

    def construct(self):
        red_img = np.zeros((100, 100, 4), dtype=np.uint8)
        red_img[:, :, 0] = 255
        red_img[:, :, 3] = 255
        image = NumpyImage(red_img)
        axes = ThreeDAxes()
        obj = OpenGLLine3D(start=[0,0,-2],end=[0,0,2])

        obj = OpenGLCylinder()
        self.add(obj)
        self.add(image)

        self.move_camera(phi= 65*DEGREES,theta=15*DEGREES)


class Translation003(ThreeDScene):
    pass


class Translation004(ThreeDScene):
    pass


with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    Translation002().render()
    exit(1)
