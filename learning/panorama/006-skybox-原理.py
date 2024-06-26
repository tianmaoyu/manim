import time

import rich

from manim import *
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
from rich.progress import track


# 三点共线，已经知道 O,P 坐标 以及 G（x,y,z）坐标中的z值，计算 x,y 并返回G
def point_from_collinearity(O: dict, P: dict, z: float) -> dict:
    if P[2] - O[2] == 0 or z - P[2] == 0:
        return (float('inf'), float('inf'), z)

    λ = (P[2] - O[2]) / (z - P[2])
    # λ 为负数时 todo
    x = (P[0] - O[0]) / λ + P[0]
    y = (P[1] - O[1]) / λ + P[1]
    return (x, y, z)


"""
theta: 0-2PI  0-360°
phi: 3/4PI - PI  120°-180°
假设：new_r= 2r 
坐标z: 映射到 z=-r 平面上"""

import numpy as np


class DemoSkybox003(ThreeDScene):
    def construct(self):
        size=100000
        # 极坐标
        spherical_points = np.array([[1.5, np.random.uniform(-np.pi, np.pi), np.random.uniform(-np.pi, 0)] for _ in range(size)])

        #笛卡尔坐标
        cartesian_points=[]
        for point in spherical_points:
            #极坐标转 笛卡尔坐标
            cartesian= spherical_to_cartesian(point)
            cartesian_points.append(cartesian)

        cocols=np.ones((size,4))
        cocols[:,0]= np.random.uniform(0.1, 0.5,size=size)
        cocols[:, 1] = 0
        cocols[:, 2] = 0
        cocols[:, 3] =1

        obj = OpenGLPMobject()
        obj.points=np.array(cartesian_points)
        obj.rgbas=cocols
        self.add(obj)

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
        cocols2= cocols.copy()
        cocols2[:, 2] = 0.5
        obj2.rgbas =cocols2
        self.add(obj2)
        self.set_camera_orientation(phi=75 * DEGREES, theta=15 * DEGREES)
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(2)


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
                    move_vector=RIGHT
                else:
                    # left_face_points.append(point)
                    move_vector=LEFT
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

        obj2.points = np.array(new_cube_points) * 1.5
        self.wait(9)


def point_from_collinearity_np(light, points: np.ndarray, z):
    """
    light ，灯光点
    points 需要投影的数据，
    z 值
    """
    λ = (points[:, 2] - light[2]) / (z- points[:, 2] )
    x = (points[:, 0] - light[0]) / λ + points[:, 0]
    y = (points[:, 1] - light[1]) / λ + points[:, 1]
    z = np.full_like(x, z)
    return np.column_stack((x, y, z))



with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    DemoSkybox003().render()
    exit(1)
