from __future__ import annotations

__all__ = [
    "ImagePixelMobject",
]

from pathlib import Path

import numpy as np
from PIL import Image
from PIL.Image import Resampling

from manim import OpenGLPMobject, Animation
from manim.mobject.opengl.opengl_surface import OpenGLSurface, OpenGLTexturedSurface
from manim.utils.images import get_full_raster_image_path

__all__ = ["ImagePixelMobject"]


class ImagePixelMobject(OpenGLPMobject):
    """
     一张图片进行像素点化，方便操作 每一个像素点
    """

    def __init__(
            self,
            filename: str=None,
            image:np.ndarray=None,
            y_inversion:bool=True,
            image_width=8,
            **kwargs,
    ):
        super().__init__(**kwargs,depth_test=True)

        if filename is not None and len(filename):
            image = np.array(Image.open(filename).convert("RGBA"))

        height, width,channel = image.shape
        assert channel == 4, "只支持 r,g,b,a"
        # 单个像素的长度 这是参考  OpenGLImageMobject 中图片长度得的固定值
        pixel_width = image_width / width
        self.pixel_width = pixel_width
        self.image_width = pixel_width * width
        self.image_height = pixel_width * height

        points = np.zeros((height * width, 3))
        y_indices, x_indices = np.mgrid[0:height, 0:width]
        points[:, 0] = x_indices.flatten()  # x坐标
        points[:, 1] = y_indices.flatten()  # y坐标
        # 创建一个颜色数组，每个颜色是一个(r, g, b, a)四元组
        rgbas = image.reshape(-1, 4)
        # 图像反转，平移到中间
        if y_inversion:
            points = points * pixel_width * [1, -1, 1]
        else:
            points = points * pixel_width
        # 颜色的处理 / 255
        rgbas = rgbas / 255

        self.init_image = image
        self.init_points = points.copy()
        self.init_rgbas = rgbas.copy()
        self.points = points
        self.rgbas = rgbas

    def to_center(self):
        height, width =self.init_image.shape[:2]
        self.points = self.points + np.array([-width / 2, height / 2, 0]) * self.pixel_width
        return self
    def _cylinder_func(self,cylinder_r,move_distance):

        self.time=0
        def update_func(mobj:ImagePixelMobject, dt):
            mobj.time += dt
            distance = move_distance * self.time
            current_points = mobj.points.copy()
            for index, point in enumerate(mobj.points):
                init_x, init_y = mobj.init_points[index][:2]
                if distance >= init_x:
                    real_rad = (distance - init_x) / cylinder_r
                    x = cylinder_r * np.cos(-real_rad) + distance - cylinder_r
                    z = cylinder_r * np.sin(-real_rad)
                    new_point = np.array([x, init_y, z])
                    current_points[index] = new_point
            mobj.points = current_points

        return update_func

    def set_points(self,new_points:np.ndarray):
        self.points=new_points

    def cylinder_animation(self,radius,move_distance):
        """
        圆柱半径
        要滚动的距离
        """
        return CylinderAnimation(self,radius,move_distance)

class NumpyImage(OpenGLPMobject):
    def __init__(self, image_array: np.ndarray, stroke_width=2.0, distance=0.025, **kwargs):
        super().__init__(**kwargs, stroke_width=stroke_width, depth_test=True)

        # 构建三维坐标
        height, width, channel = image_array.shape
        assert channel == 4, "必须是r,g,b,a"
        points = np.zeros((height * width, 3))
        y_indices, x_indices = np.mgrid[0:height, 0:width]
        points[:, 0] = x_indices.flatten()  # x坐标
        points[:, 1] = y_indices.flatten()  # y坐标
        rgbas = image_array.reshape(-1, 4)

        # y轴反转和缩小- 一个坐标间隔为1
        points = points * distance * np.array([1, -1, 1])
        # 居中
        points += np.array([-width * distance / 2, height * distance / 2, 0])
        self.points = points
        self.rgbas = rgbas / 255

    def set_points(self,points:np.ndarray):
        self.points = points
        return self

class CylinderAnimation(Animation):
    def __init__(self, mobject:ImagePixelMobject, radius, move_distance, **kwargs):
        self.radius = radius
        self.move_distance = move_distance
        self.mobject=mobject
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        """alpha  0-1 之间"""
        self.mobject._cylinder_func(self.radius, self.move_distance)(self.mobject, alpha)
