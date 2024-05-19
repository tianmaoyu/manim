import time

import rich

from manim import *
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
from rich.progress import track



"""
theta: 0-2PI  0-360°
phi: 3/4PI - PI  120°-180°
假设：new_r= 2r 
坐标z: 映射到 z=-r 平面上"""

import numpy as np


class DemoSkybox008(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        axes.add(axes.get_axis_labels())
        self.add(axes)

        image = ImagePixelMobject("src/360mini1.jpg", image_width=8, stroke_width=6.0)
        image.to_center()
        points= image.points.copy()
        spherical_points = np.empty_like(points)
        # 归一化，弧度化 映射
        width = 4
        spherical_points[:, 2] = PI * (points[:, 1] / width) - PI / 2
        spherical_points[:, 1] = PI * points[:, 0] / width
        spherical_points[:, 0] = 1  # 半径


        #笛卡尔坐标
        cartesian_points=[]
        for point in spherical_points:
            #极坐标转 笛卡尔坐标
            cartesian= spherical_to_cartesian(point)
            cartesian_points.append(cartesian)


        obj = OpenGLPMobject()
        obj.points=np.array(cartesian_points)
        obj.rgbas=image.rgbas.copy()
        self.add(obj)
        self.set_camera_orientation(phi=75 * DEGREES, theta=15 * DEGREES)
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(2)

        #转 正方体坐标
        cartesian_points2 = cartesian_points.copy()
        cube_points = []
        for point in cartesian_points2:
            x, y, z = point
            abs_max = max(abs(x), abs(y), abs(z))
            #两个组合会得到一些奇怪的形状
            abs_min = min(abs(x), abs(y), abs(z))
            cube_points.append([x / abs_max, y / abs_max, z / abs_max])

        obj2 = OpenGLPMobject()
        obj2.points = np.array(cube_points)
        obj2.rgbas =image.rgbas.copy()
        self.add(obj2)

        self.wait(2)
        self.remove(obj)
        self.remove(image)

        # 六个面
        copy_cube_points=cube_points.copy()
        new_cube_points=[]
        for point in copy_cube_points:
            x, y, z = point
            abs_x, abs_y, abs_z = abs(x), abs(y), abs(z)
            move_vector=[0,0,0]
            if abs_x >= abs_y and abs_x >= abs_z:
                if x > 0:
                    # right_face_points.append(point)
                    move_vector=ORIGIN
                else:
                    # left_face_points.append(point)
                    move_vector=ORIGIN
            elif abs_y >= abs_x and abs_y >= abs_z:
                if y > 0:
                    # up_face_points.append(point)
                    move_vector = UP
                else:
                    # down_face_points.append(point)
                    move_vector=DOWN
            else:
                if z > 0:
                    # front_face_points.append(point)
                    move_vector =OUT
                else:
                    # back_face_points.append(point)
                    move_vector = IN
            new_point=point+move_vector
            new_cube_points.append(new_point)

        obj2.points = np.array(new_cube_points)
        self.wait(9)




with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    DemoSkybox008().render()
    exit(1)
