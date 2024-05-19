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


class DemoSkybox001(ThreeDScene):
    def construct(self):
        self.next_section(skip_animations=False)
        image = ImagePixelMobject("src/360mini1.jpg", image_width=16, stroke_width=6.0)
        image.to_center()
        self.add(image)

        axex = ThreeDAxes()
        axex.add(axex.get_axis_labels())
        self.add(axex.shift([-3,0,0]))
        self.set_camera_orientation(phi=75 * DEGREES, theta=15 * DEGREES)

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

        self.next_section(name="扣图")

        selct1=((spherical_points[:, 1]>0)&(spherical_points[:, 1]<90*DEGREES)
                & (spherical_points[:, 2]> -90*DEGREES) &(spherical_points[:, 2]< 0))
        cartesian_points[selct1]+=np.array([-3,0,0])
        image.points=cartesian_points
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(2)
        # self.set_camera_orientation(theta=0 * DEGREES, phi=90 * DEGREES)

        # # self.bring_to_back(image)
        # cartesian_points += np.array([3, 0, 0])
        # image.points = cartesian_points
        # self.wait(0.5)
        #
        # self.next_section(name="sphere_to_skybox",skip_animations=True)
        # animate = Rotate(image, angle=120 * DEGREES, axis=OUT, about_point=image.get_center())
        # self.play(animate,run_time=2)
        #
        # self.next_section(name="向量")
        # square_1 = Square(side_length=2.0).shift(DOWN)
        # square_2 = Square(side_length=2.0).next_to(square_1, direction=UP)
        # square_3 = Square(side_length=2.0).next_to(square_2, direction=UP)
        # self.add(square_1, square_2, square_3)
        # animate= square_1.animate.rotate(angle=90*DEGREES,axis=RIGHT,about_point=square_1.get_center())
        # self.play(animate,run_time=2)
        # # self.wait(0.5)





        # perspective_point = (0, 0, 3)
        # pm_omject = OpenGLPMobject()
        # pm_omject.rgbas = image.rgbas
        # def update_func(dt):
        #     projection_point_list = point_from_collinearity_np(perspective_point, cartesian_points, 2)
        #     pm_omject.points = projection_point_list
        #
        #
        # self.add(pm_omject)
        # self.add_updater(func=update_func)
        # self.play(animate,run_time=2)



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
    DemoSkybox001().render()
    exit(1)
