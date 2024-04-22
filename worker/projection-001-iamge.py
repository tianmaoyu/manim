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


class ProjectionDemo(ThreeDScene):
    def construct(self):
        image_obj = OpenGLImageMobject("mini.jpg")
        self.add(image_obj)

        # self.set_camera_orientation(phi=75 * DEGREES, theta=15 * DEGREES)
        # self.begin_ambient_camera_rotation(rate=1)
        # self.add(ThreeDAxes())

        # point= OpenGLPMPoint(stroke_width=5)
        # point.points=np.array([[1, 1, 1],[0, 0, 0]])
        # point.rgbas=np.array([[1, 0, 0, 1]])
        # self.add(point)
        # self.wait(1)

        image= Image.open("mini.jpg").convert("RGBA")
        image_data=np.array(image)

        h,w= image_data.shape[:2]
        width = image_obj.width
        height = image_obj.height
        pixel = width/w
        print("一个图像的大小",pixel)
        #取第一个像素点 ，四个角
        data0= image_data[0,0]/255
        data1 = image_data[h-1, 0]
        data2 = image_data[h-1, w-1]
        data3 = image_data[0,w-1]

        point = OpenGLPMPoint(stroke_width=5)
        x,y= self.image_coor_to_screen_coor([0,0],h,w)
        point0=np.array([x,y,100])*pixel
        point.points = np.array([point0])
        point.rgbas = np.array([data0])
        self.add(point)

        # self.wait()

    def image_coor_to_screen_coor(self,point:np.ndarray,heigth,width):
         y= point[0]+heigth/2
         x= point[1]-width/2
         return (int(x),int(y))


class ProjectionDemo2(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=75 * DEGREES, theta=15 * DEGREES)
        image_obj = OpenGLImageMobject("mini.jpg")
        self.add(image_obj.shift(UP*2))
        # self.wait(2)

        image = Image.open("mini.jpg").convert("RGBA")
        image_data = np.array(image)

        h, w, _ = image_data.shape
        width = image_obj.width
        height = image_obj.height
        #每个图片像素 在平面上的长度，宽度
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
        self.add(mpoint.next_to(image_obj,direction=DOWN))



    def image_coor_to_screen_coor(self, point: np.ndarray, height: int, width: int):
        """
        把图片坐标，转到 manim 的平面坐标
        """
        y = -(point[1] - height / 2)
        x = point[0] - width / 2
        return (int(x), int(y))


# "renderer": "opengl"  "background_color":"WHITE",
with tempconfig({"preview": True, "disable_caching": True,"renderer": "opengl"}):
    ProjectionDemo2().render()
    exit(1)
