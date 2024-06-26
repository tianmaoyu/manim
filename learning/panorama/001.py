import time

from manim import *
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np


class Demo001(ThreeDScene):
    def construct(self):
        image = ImagePixelMobject("src/360-2048-1024.jpg", image_width=16, stroke_width=6.0)
        image.to_center()
        self.add(image)
        axex = ThreeDAxes(x_length=[-4, 4, 1], x_range=[-4, 4, 1], z_range=[-4, 4, 1])
        self.add(axex)

        self.set_camera_orientation(phi=75 * DEGREES, theta=15 * DEGREES)

        points = image.points
        # [r,phi,theta]
        spherical_points = np.empty_like(points)
        width = 8
        spherical_points[:, 2] = PI * (points[:, 1] / width) - PI / 2
        spherical_points[:, 1] = PI * points[:, 0] / width
        spherical_points[:, 0] = 3

        # 性能改进
        r = spherical_points[:, 0]
        theta = spherical_points[:, 1]
        phi = spherical_points[:, 2]

        x = r * np.cos(theta) * np.sin(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(phi)

        cartesian_points = np.stack((x, y, z), axis=-1)

        image.points = cartesian_points
        return

        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(2)


"""
theta: 0-2PI  0-360°
phi: 3/4PI - PI  120°-180°
假设：new_r= 2r 
坐标z: 映射到 z=-r 平面上"""


class Demo002(ThreeDScene):
    def construct(self):
        image = ImagePixelMobject("src/360-2048-1024.jpg", image_width=16, stroke_width=6.0)
        image.to_center()
        self.add(image)
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
        self.wait(0.5)

        # 球面- 映射到平面-小行星
        sphere_points = cartesian_points.copy()

        #一个 极坐标-到 另一个极坐标

        r2 = 6
        theta2 = theta
        phi2 = np.arccos(z / r2)

        # 极坐标映射成到一个平面


        x2 = r2 * np.cos(theta2) * np.sin(phi2)
        y2 = r2 * np.sin(theta2) * np.sin(phi2)
        z2 = r2 * np.cos(phi2)
        cartesian_points2 =np.stack((x2,y2,z2),axis=-1)
        pm_omject2 = OpenGLPMobject()
        pm_omject2.points=cartesian_points2
        pm_omject2.rgbas=image.rgbas

        self.add(pm_omject2)
        self.remove(image)
        self.wait(0.5)
        self.move_camera(phi=75 * DEGREES, theta=150 * DEGREES, run_time=1)



# self.play(image.animate.scale(7),axex.animate.scale(6),run_time=1)
# self.play(ApplyMethod(image.set_points, cartesian_points), run_time=2, rate_func=smooth)
# cartesian_points = np.apply_along_axis(spherical_to_cartesian, axis=1, arr=spherical_points)
# self.move_camera(phi=75 * DEGREES, theta=150 * DEGREES, run_time=1)
# "renderer": "opengl" "quality": "fourk_quality","force_window":True, "disable_caching": True,
with tempconfig({"preview": True, "renderer": "opengl"}):
    Demo002().render()
    exit(1)
