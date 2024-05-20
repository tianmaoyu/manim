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


        self.next_section(name="init",skip_animations=True)

        image = ImagePixelMobject("src/360-1280-640.jpg", image_width=8, stroke_width=6.0)
        image.to_center()
        # self.add(image)
        self.play(Create(image))
        axex = ThreeDAxes().shift([-3,0,0])
        axex.add(axex.get_axis_labels())
        # self.add(axex)
        self.play(Create(axex))
        self.wait(2)
        self.move_camera(phi=75 * DEGREES, theta=15 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.5)
        self.play(image.animate.scale(20),run_time=4)
        self.play(image.animate.scale(1/20), run_time=4)
        self.wait(0.5)


        # self.next_section(name="粒子化",skip_animations=True)
        # self.time = 0
        # final_z = 2
        # duration = 4  # 移动到最终高度所需的时间（秒）
        # self.begin_ambient_camera_rotation(rate=0.5)
        # def update_func(dt):
        #     self.time += dt
        #     n_to_select = 5000
        #     select_indices = np.random.choice(image.points.shape[0], n_to_select, replace=False)
        #     selected_points = image.points[select_indices]
        #     progress = min(self.time / duration, 1)
        #     new_z_values = progress * final_z
        #     selected_points[:, 2] = new_z_values + selected_points[:, 2]
        #     image.points[select_indices, 2] = selected_points[:, 2]
        #
        # self.add_updater(func=update_func)
        # self.wait(4)
        # self.remove_updater(func=update_func)
        #
        # def update_func(dt):
        #     z_values = image.points[:, 2]
        #     max_increase = 2 - z_values
        #     random_increases = np.random.uniform(0, 10, size=z_values.shape) * max_increase
        #     new_z_values = z_values + random_increases / (3 * 60)
        #     image.points[:, 2] = new_z_values
        #
        # self.add_updater(func=update_func)
        # # self.set_camera_orientation(phi=45 * DEGREES, theta=180 * DEGREES)
        # self.wait(6)
        # self.remove_updater(func=update_func)
        # # image.points-=np.array([0,0,final_z])


        self.next_section(name="平面转球面",skip_animations=True)
        points = image.points
        image_points=points.copy()
        # 平面转球面;
        # 1：平面尺寸映射：归一化；2. 归一化的长度 弧度化 映射，； 3： 再补充的半径就是极坐标
        # [r,phi,theta]
        spherical_points = np.empty_like(points)
        # 归一化，弧度化 映射
        width = 4
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

        self.next_section(name="进入球",skip_animations=True)
        self.play(image.animate.scale(7), run_time=2)
        self.wait(2)
        self.play(image.animate.scale(1 / 7), run_time=2)
        self.wait(1)

        #
        # verctor_list = np.zeros_like(cartesian_points)
        # move_vector=(cartesian_points -points)
        # self.count = 0
        # count_size=1500
        # def update_func_move(dt):
        #     end=(self.count + 1) * count_size
        #     start= self.count * count_size
        #     if verctor_list.shape[0]<=end:
        #         image.points[start:verctor_list.shape[0]] += move_vector[start:verctor_list.shape[0]]
        #         return
        #     image.points[start:end] += move_vector[start:end]
        #     self.count += 1
        #
        # self.add_updater(func=update_func_move)
        #
        # self.wait(10)
        # image.points = cartesian_points


        self.next_section(name="球面变天空合子",skip_animations=False)
        box_points= cartesian_points.copy()

        #奇怪的转换
        # # box_points += np.array([4, 0, 0])
        # cube_points = []
        # for point in box_points:
        #     x, y, z = point
        #     abs_min = min(abs(x), abs(y), abs(z))
        #     abs_max = max(abs(x), abs(y), abs(z))
        #     cube_points.append([x / abs_min, y / abs_min, z / abs_max])
        # cube_points=np.array(cube_points)

        # 使用NumPy的广播和向量化操作来计算每个点的最大绝对值并进行归一化
        abs_values = np.abs(box_points)
        abs_max = np.max(abs_values, axis=1, keepdims=True)
        cube_points = box_points*2 / abs_max

        self.play(ApplyMethod(image.set_points, cube_points), run_time=2, rate_func=smooth)
        self.wait(2)
        return

        self.next_section(name="进出天空盒子内部",skip_animations=True)
        self.play(image.animate.scale(7), run_time=2)
        self.wait(2)
        self.play(image.animate.scale(1/7), run_time=2)
        self.wait(1)


        self.next_section(name="盒子变球",skip_animations=True)
        print("盒子变球----")
        self.play(ApplyMethod(image.set_points, shpere_points), run_time=2, rate_func=smooth)

        self.next_section(name="添加极坐标",skip_animations=True)
        polar = PolarPlane().shift([0,0,1.2])
        self.add(polar)
        self.wait(2)
        self.add(image)
        self.next_section(name="球表球形形小行星",skip_animations=True)
        self.stop_ambient_camera_rotation()
        self.move_camera(theta=0, phi=0, run_time=3)
        perspective_point = (0, 0, 2)
        projection_points = point_from_collinearity_np(perspective_point, cartesian_points, 1.2)
        self.play(ApplyMethod(image.set_points, projection_points), run_time=2, rate_func=smooth)
        animate = Rotate(image, angle=179 * DEGREES, axis=OUT, about_point=ORIGIN)
        self.play(animate, run_time=4)


        self.next_section(name="球变正方形-小行星",skip_animations=True)
        self.stop_ambient_camera_rotation()
        self.move_camera(theta=0,phi=0,run_time=3)
        perspective_point = (0, 0, 2)
        projection_points = point_from_collinearity_np(perspective_point, cartesian_points, 1.2)
        self.play(ApplyMethod(image.set_points, projection_points), run_time=2, rate_func=smooth)
        animate = Rotate(image, angle=180 * DEGREES, axis=OUT, about_point=ORIGIN)
        self.play(animate,run_time=2)


        self.next_section(name="选择",skip_animations=True)
        self.next_section(name="星球-转平面图片")
        self.play(ApplyMethod(image.set_points, image_points), run_time=2, rate_func=smooth)
        self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES,run_time=2)
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
with tempconfig({"preview": True,"disable_caching": False, "renderer": "opengl"}):
    DemoSkybox007().render()
    exit(1)
