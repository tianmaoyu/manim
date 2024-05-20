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


class DemoSkybox007(ThreeDScene):
    def construct(self):

        self.next_section(name="init",skip_animations=False)

        image = ImagePixelMobject("src/360-1280-640.jpg", image_width=16, stroke_width=6.0)
        image.to_center()
        self.add(image)
        axex = ThreeDAxes().shift([-3,0,0])
        axex.add(axex.get_axis_labels())
        self.add(axex)
        self.wait(2)
        self.move_camera(phi=75 * DEGREES, theta=15 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.5)
        self.play(image.animate.scale(4),run_time=1)
        self.play(image.animate.scale(1/4), run_time=1)
        self.wait(0.5)

        self.next_section(name="平面转球面",skip_animations=False)
        points = image.points
        image_points=points.copy()
        # 平面转球面;
        # 1：平面尺寸映射：归一化；2. 归一化的长度 弧度化 映射，； 3： 再补充的半径就是极坐标
        # [r,phi,theta]
        spherical_points = np.empty_like(points)
        # 归一化，弧度化 映射
        width = 8
        spherical_points[:, 2] = PI * (points[:, 1] / width) - PI / 2
        spherical_points[:, 1] = PI * points[:, 0] / width
        spherical_points[:, 0] = 2  # 半径

        # 性能改进
        r = spherical_points[:, 0]
        theta = spherical_points[:, 1]
        phi = spherical_points[:, 2]

        x = r * np.cos(theta) * np.sin(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(phi)

        cartesian_points = np.stack((x, y, z), axis=-1)
        shpere_points= cartesian_points.copy()
        self.play(ApplyMethod(image.set_points, cartesian_points), run_time=2, rate_func=smooth)
        image.points = cartesian_points
        self.wait(0.5)



        self.next_section(name="球面变天空合子",skip_animations=False)
        box_points= cartesian_points.copy()
        # box_points += np.array([4, 0, 0])
        # cube_points = []
        # for point in box_points:
        #     x, y, z = point
        #     abs_max = max(abs(x), abs(y), abs(z))
        #     cube_points.append([x / abs_max, y / abs_max, z / abs_max])

        # 使用NumPy的广播和向量化操作来计算每个点的最大绝对值并进行归一化
        abs_values = np.abs(box_points)
        abs_max = np.max(abs_values, axis=1, keepdims=True)
        cube_points = box_points*2 / abs_max

        self.play(ApplyMethod(image.set_points, cube_points), run_time=2, rate_func=smooth)
        self.wait(2)

        self.next_section(name="进出天空盒子内部",skip_animations=False)
        self.play(image.animate.scale(7), run_time=2)
        self.wait(2)
        self.play(image.animate.scale(1/7), run_time=1)

        self.next_section(name="盒子变球")
        print("盒子变球----")
        self.play(ApplyMethod(image.set_points, shpere_points), run_time=2, rate_func=smooth)

        self.next_section(name="球变小行星")
        self.stop_ambient_camera_rotation()
        self.move_camera(theta=0,phi=0,run_time=1)
        perspective_point = (0, 0, 2)
        projection_points = point_from_collinearity_np(perspective_point, cartesian_points, 1.2)
        self.play(ApplyMethod(image.set_points, projection_points), run_time=2, rate_func=smooth)
        animate = Rotate(image, angle=180 * DEGREES, axis=OUT, about_point=ORIGIN)
        self.play(animate,run_time=2)
        self.next_section(name="选择")

        self.next_section(name="星球-转平面图片")
        self.play(ApplyMethod(image.set_points, image_points), run_time=2, rate_func=smooth)
        self.move_camera(phi=75 * DEGREES, theta=15 * DEGREES)
        self.wait(1)





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


# "disable_caching": True,
with tempconfig({"preview": True, "renderer": "opengl"}):
    DemoSkybox007().render()
    exit(1)
