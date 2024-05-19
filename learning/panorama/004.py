import time

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


class Demo002(ThreeDScene):
    def construct(self):
        image = ImagePixelMobject("src/3602.jpg", image_width=16, stroke_width=6.0)
        image.to_center()
        # self.add(image)
        axex = ThreeDAxes(x_length=[-4, 4, 1], x_range=[-4, 4, 1], z_range=[-4, 4, 1])
        self.add(axex)

        # self.set_camera_orientation(phi=75 * DEGREES, theta=15 * DEGREES)

        points = image.points

        # 平面转球面;
        # 1：平面尺寸映射：归一化；2. 归一化的长度 弧度化 映射，； 3： 再补充的半径就是极坐标
        # [r,phi,theta]
        spherical_points = np.empty_like(points)
        # 归一化，弧度化 映射
        width = 8
        spherical_points[:, 2] = PI * (points[:, 1] / width) - PI / 2
        spherical_points[:, 1] = PI * points[:, 0] / width
        spherical_points[:, 0] = 3  # 半径

        # 性能改进
        r = spherical_points[:, 0]
        theta = spherical_points[:, 1]
        phi = spherical_points[:, 2]

        x = r * np.cos(theta) * np.sin(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(phi)

        cartesian_points = np.stack((x, y, z), axis=-1)
        image.points = cartesian_points
        # self.set_camera_orientation(theta=0 * DEGREES, phi=90 * DEGREES)
        animate=Rotate(image,angle=189*DEGREES,axis=UP,about_point=ORIGIN)
        # animate= image.animate.rotate(angle=89*DEGREES,axis=UP)
        # self.play(animate,run_time=1)
        self.bring_to_back(image)




        perspective_point = (0, 0, 3)
        pm_omject = OpenGLPMobject()
        pm_omject.rgbas = image.rgbas
        def update_func(dt):
            projection_point_list = point_from_collinearity_np(perspective_point, cartesian_points, 2)
            pm_omject.points = projection_point_list


        self.add(pm_omject)
        self.add_updater(func=update_func)
        self.play(animate,run_time=2)



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
    Demo002().render()
    exit(1)
