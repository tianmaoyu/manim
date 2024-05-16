import time

from manim import *
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
from rich.progress import track


# 三点共线，已经知道 O,P 坐标 以及 G（x,y,z）坐标中的z值，计算 x,y 并返回G




class Demo004(ThreeDScene):
    def construct(self):
        image = ImagePixelMobject("src/360.jpg", image_width=16, stroke_width=2.0)
        image.to_center()
        self.add(image)
        axex = ThreeDAxes(x_length=[-4, 4, 1], x_range=[-4, 4, 1], z_range=[-4, 4, 1])


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
        self.remove(image)
        # 球面- 映射到平面-小行星
        perspective_point = [0, 0, 3]
        z = -2
        # 版本 一
        # projection_point_list = []
        # for given_point in cartesian_points:
        #     projection_point = point_from_collinearity(perspective_point, given_point, z)
        #     projection_point_list.append(projection_point)

        # 优化版本 二
        projection_point_list = point_from_collinearity_np(perspective_point, cartesian_points, z)

        pm_omject = OpenGLPMobject()
        pm_omject.points = projection_point_list
        pm_omject.rgbas = image.rgbas
        self.add(pm_omject)

        valueTracker = ValueTracker(-3)
        points= cartesian_points.copy()
        z=-6
        def update_func(dt):
            value = valueTracker.get_value()

            matrix_z = [[np.cos(value), -np.sin(value), 0],
                       [np.sin(value), np.cos(value), 0],
                      [0, 0, 1]]

            matrix_y = [[np.cos(value), 0, np.sin(value)],
                        [0, 1, 0],
                        [-np.sin(value), 0, np.cos(value)]]

            matrix_x = [[1, 0, 0],
                        [0, np.cos(value), -np.sin(value)],
                        [0, np.sin(value), np.cos(value)]]

            points_t = np.transpose(points)
            _points=np.dot(matrix_x,points_t)
            _points=np.transpose(_points)

            projection_point_list = point_from_collinearity_np(perspective_point, points, value)

            projection_point_list[(np.abs(projection_point_list[:,0]) >3)|(np.abs(projection_point_list[:,1])>3)]=float('inf')
            # squared_sums = np.square(points[:, 0]) + np.square(points[:, 1])
            # points[squared_sums > 9] = float('inf')
            # 找到平方和大于15的点，并将这些点的值设置为无限大
            # points[squared_sums > 15] = float('inf')

            pm_omject.points = projection_point_list


        self.add_updater(func=update_func)
        self.play(valueTracker.animate.increment_value(5), run_time=2)
        self.remove_updater(func=update_func)
        self.add(axex)
        self.move_camera(phi=75*DEGREES,theta=15*DEGREES,run_time=3)

        self.move_camera(phi=175 * DEGREES, theta=15 * DEGREES, run_time=3)


def point_from_collinearity(light: dict, point: dict, z: float) -> dict:
    """
    light: 光
    point：已知点
    z: 要投射的z 平面的值
    """
    if point[2] - light[2] == 0 or z - point[2] == 0:
        return (float('inf'), float('inf'), z)
    λ = (point[2] - light[2]) / (z - point[2])
    # λ 为负数时 todo
    x = (point[0] - light[0]) / λ + point[0]
    y = (point[1] - light[1]) / λ + point[1]
    return (x, y, z)


def point_from_collinearity_np(light: dict, points: np.ndarray, z: float):
    λ = (points[:, 2] - light[2]) / (z - points[:, 2])
    x = (points[:, 0] - light[0]) / λ + points[:, 0]
    y = (points[:, 1] - light[1]) / λ + points[:, 1]
    z = np.full_like(x, z)
    return np.column_stack((x, y, z))


with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    Demo004().render()
    exit(1)
