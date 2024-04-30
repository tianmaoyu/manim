import random
import time

from manim import *
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np


class Image001(ThreeDScene):
    def construct(self):
        image = OpenGLImageMobject("mini.jpg")

        self.add(image)

        self.move_camera(phi=45 * DEGREES, theta=15 * DEGREES, run_time=2)
        image.points
        self.time = 0

        def update_func(dt):
            self.time += dt
            n_to_select = 500
            select_indices = np.random.choice(image.points.shape[0], n_to_select, replace=False)
            selected_points = image.points[select_indices]
            selected_points[:, 2] += np.random.randint(low=0, high=2)
            image.points[select_indices, 2] = selected_points[:, 2]

        self.add_updater(func=update_func)
        self.wait(4)


class Image002(ThreeDScene):
    def construct(self):
        image = ImagePixelMobject("mini.jpg")
        image.to_center()
        self.add(image)

        self.move_camera(phi=45 * DEGREES, theta=15 * DEGREES, run_time=2)
        image.points
        self.time = 0

        def update_func(dt):
            self.time += dt
            n_to_select = 500
            select_indices = np.random.choice(image.points.shape[0], n_to_select, replace=False)
            selected_points = image.points[select_indices]
            selected_points[:, 2] += int(self.time)
            image.points[select_indices, 2] = selected_points[:, 2]

        print(self.time)
        self.add_updater(func=update_func)
        self.wait(4)
        self.move_camera(phi=75 * DEGREES, theta=135 * DEGREES, run_time=2)


class Image003(ThreeDScene):
    def construct(self):
        image = ImagePixelMobject("mini.jpg")
        image.to_center()
        self.add(image)
        self.move_camera(phi=45 * DEGREES, theta=15 * DEGREES, run_time=2)

        self.time = 0
        final_z = 2
        duration = 4  # 移动到最终高度所需的时间（秒）

        def update_func(dt):
            self.time += dt
            n_to_select = 500
            select_indices = np.random.choice(image.points.shape[0], n_to_select, replace=False)
            selected_points = image.points[select_indices]
            progress = min(self.time / duration, 1)
            new_z_values = progress * final_z
            selected_points[:, 2] = new_z_values + selected_points[:, 2]
            image.points[select_indices, 2] = selected_points[:, 2]

        self.add_updater(func=update_func)
        self.wait(4)
        self.move_camera(phi=75 * DEGREES, theta=135 * DEGREES, run_time=2)


class Image004(ThreeDScene):
    def construct(self):
        image = ImagePixelMobject("mini.jpg")
        image.to_center()
        self.add(image.shift(IN * 2))
        self.move_camera(phi=75 * DEGREES, theta=0 * DEGREES, run_time=2)

        self.time = 0
        final_z = 2
        duration = 4  # 移动到最终高度所需的时间（秒）
        self.begin_ambient_camera_rotation(rate=0.5)

        def update_func(dt):
            self.time += dt
            n_to_select = 500
            select_indices = np.random.choice(image.points.shape[0], n_to_select, replace=False)
            selected_points = image.points[select_indices]
            progress = min(self.time / duration, 1)
            new_z_values = progress * final_z
            selected_points[:, 2] = new_z_values + selected_points[:, 2]
            image.points[select_indices, 2] = selected_points[:, 2]

        self.add_updater(func=update_func)
        self.wait(4)
        self.remove_updater(func=update_func)

        def update_func(dt):
            z_values = image.points[:, 2]
            max_increase = 2 - z_values
            random_increases = np.random.uniform(0, 10, size=z_values.shape) * max_increase
            new_z_values = z_values + random_increases / (3 * 60)
            image.points[:, 2] = new_z_values

        self.add_updater(func=update_func)
        # self.set_camera_orientation(phi=45 * DEGREES, theta=180 * DEGREES)
        self.wait(6)


# 给 没一个像素点，四处散开
class Image005(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=65 * DEGREES, theta=15 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.3)

        image2 = ImagePixelMobject("rose.jpg")
        image2.to_center()
        self.add(image2)
        self.add(ThreeDAxes())

        height, width = image2.init_image.shape[:2]

        move_vector = []

        for y in range(height):
            for x in range(width):
                vector = (np.array([random.random(), random.random(), random.random()]) - 0.5) * 0.025
                move_vector.append(vector)

        # verctor_list = (np.random.random((height * width, 3)) -0.5)*0.0125

        self.time = 0

        def update_func(dt):
            self.time += dt
            image2.points = image2.points + move_vector

        self.add_updater(func=update_func)
        self.wait(5)


# 让像素点旋转起来
class Image006(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=65 * DEGREES, theta=15 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.3)

        image2 = ImagePixelMobject("rose.jpg")
        image2.to_center()
        self.add(image2)
        self.add(ThreeDAxes())

        height, width = image2.init_image.shape[:2]

        move_vector = []

        for y in range(height):
            for x in range(width):
                vector = (np.array([random.random(), random.random(), random.random()]) - 0.5) * 0.025
                move_vector.append(vector)

        # verctor_list = (np.random.random((height * width, 3)) -0.5)*0.0125

        self.time = 0

        def update_func_move(dt):
            self.time += dt
            image2.points = image2.points + move_vector

        self.add_updater(func=update_func_move)
        self.wait(5)
        self.remove_updater(func=update_func_move)
        self.stop_ambient_camera_rotation()
        #每次旋转 1.5度
        theta = np.deg2rad(1.5)
        matrix_r = np.matrix([[np.cos(theta), -np.sin(theta), 0],
                              [np.sin(theta), np.cos(theta), 0],
                              [0, 0, 1]])

        def update_func_rotation(dt):
            self.time += dt
            # 一般 是 matrix 乘上 point ，numpy 是反的
            image2.points =image2.points @ matrix_r

        self.add_updater(func=update_func_rotation)
        self.wait(5)

# "renderer": "opengl" "quality": "fourk_quality",
with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    Image006().render()
    exit(1)
