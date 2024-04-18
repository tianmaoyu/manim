import math

from scipy.interpolate import interp2d

from manim import *
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
from PIL import Image


class WorldDemo(ThreeDScene):
    def construct(self):
        iamge = OpenGLImageMobject("Whole_world_-_land_and_oceans_12000.jpg")
        self.add(iamge)
        self.set_camera_orientation(phi=75 * DEGREES, theta=15 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.5)
        scale = iamge.animate.scale(10)
        self.play(scale, run_time=2)
        self.wait(3)


class WorldToSphere(ThreeDScene):
    def construct(self):
        iamge = OpenGLImageMobject("Whole_world_-_land_and_oceans_12000.jpg")

        def uv_func(u, v):
            return 5 * np.array([
                np.cos(u) * np.sin(v),
                np.sin(u) * np.sin(v),
                -np.cos(v)
            ])
            # 必须严格的 分辨率，范围

        sphere = OpenGLSurface(
            uv_func,
            u_range=[0, TAU],
            v_range=[0, PI],
            checkerboard_colors=[RED_D, RED_E],
            resolution=(101, 51)
        )

        sphere2 = OpenGLSurface(
            uv_func,
            u_range=[0, TAU],
            v_range=[0, PI],
            checkerboard_colors=[RED_D, RED_E],
            resolution=(101, 51))

        # 替换为你的纹理图片的路径
        texture = OpenGLTexturedSurface(uv_surface=sphere, image_file="Whole_world_-_land_and_oceans_12000.jpg")

        self.add(iamge)

        self.wait(1)
        self.play(FadeTransform(iamge, texture))


class WorldToSphere2(ThreeDScene):

    def inverse_mercator_projection(self, x, y):
        """
        球面墨卡托投影的反操作
        :param x: 墨卡托投影的x坐标
        :param y: 墨卡托投影的y坐标
        :return: longitude, latitude 经度和纬度，单位为度
        """
        longitude = math.degrees(x)
        latitude = math.degrees(2 * math.atan(math.exp(y)) - math.pi / 2)

        return longitude, latitude

    def spherical_to_cartesian(self, latitude, longitude, radius=1):
        """
        将经纬度转换为球面坐标
        :param latitude: 纬度，单位为度
        :param longitude: 经度，单位为度
        :param radius: 球体的半径
        :return: x, y, z 球面坐标
        """
        phi = np.radians(90 - latitude)
        theta = np.radians(longitude)

        x = radius * np.sin(phi) * np.cos(theta)
        y = radius * np.sin(phi) * np.sin(theta)
        z = radius * np.cos(phi)

        return x, y, z

    def construct(self):
        image = Image.open("Whole_world.jpg").convert("RGB")
        img_array = np.array(image)
        # 图像的宽度和高度
        width, height = img_array.shape[:2]
        # 将图像转为一维数组，便于插值
        flat_img = img_array.reshape(-1, 3)

        # 定义经纬度范围
        theta_min, theta_max = 0, 2 * np.pi
        phi_min, phi_max = -np.pi / 2, np.pi / 2
        # 为球面上每个点计算对应的图像坐标
        num_points = 1000  # 示例数量，可根据需求调整
        theta = np.linspace(theta_min, theta_max, num_points)
        phi = np.linspace(phi_min, phi_max, num_points)
        theta_grid, phi_grid = np.meshgrid(theta, phi)

        # 计算3D笛卡尔坐标
        x = 50 * np.cos(phi_grid) * np.sin(theta_grid)
        y = 50 * np.sin(phi_grid)
        z = 50 * np.cos(phi_grid) * np.cos(theta_grid)

        # 将经纬度转换为图像坐标，这里假设你的图像是一个equirectangular projection
        # 实际上这是一个复杂的映射，这里简化处理，假设图像宽高比和经纬度一致
        u = theta / (2 * np.pi) * width
        v = (phi + np.pi / 2) / np.pi * height

        # 创建一个双线性插值器
        # interpolator = interp2d(width, height, flat_img.T, kind='linear')
        #
        # # 获取每个球面点的像素颜色
        # rgb_values = interpolator(u.flatten(), v.flatten()).T


class WorldToSphere3(ThreeDScene):
    def plane_func(self, lenght: float, width: float) -> np.ndarray:
        return np.array([lenght, width, 0])

    def cylinder_func(self, phi: float, height: float) -> np.ndarray:
        r = 2
        return np.array([r * np.cos(phi), r * np.sin(phi), height])

    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=15 * DEGREES)
        #平面
        plane_surface = Surface(
            self.plane_func,
            u_range=[-PI, PI],
            v_range=[-PI, PI],
            resolution=(101, 51)
        )
        #圆柱面
        cylinder_surface = Surface(
            self.cylinder_func,
            u_range=[0, TAU],
            v_range=[-PI, PI],
            resolution=(101, 51)
        )
        self.add(plane_surface)
        self.wait(1)
        self.add(cylinder_surface)
        self.wait(1)

        # self.play(Transform(plane_surface, cylinder_surface))
        # self.play(FadeTransform(plane_surface, cylinder_surface))


class ProjectImageOnSphere(ThreeDScene):

    def plane_func(self, lenght: float, width: float) -> np.ndarray:
        return np.array([lenght, width, 0])

    def cylinder_func(self, phi: float, height: float) -> np.ndarray:
        r = 2
        return np.array([r * np.cos(phi), r * np.sin(phi), height])

    def construct(self):
        # iamge = OpenGLImageMobject("Whole_world.jpg")
        # self.add(iamge)
        self.set_camera_orientation(phi=65 * DEGREES, theta=15 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.5)

        plane_surface = OpenGLSurface(
            self.plane_func,
            u_range=[-PI, PI],
            v_range=[-PI, PI],
            color=YELLOW,
            checkerboard_colors=[YELLOW, RED_E],
            resolution=(101, 51)
        )
        Surface
        plane_texture = OpenGLTexturedSurface(uv_surface=plane_surface, image_file="Whole_world.jpg")
        self.add(plane_texture)

        # scale_animate = plane_texture.animate.scale(3)
        # self.play(scale_animate, run_time=2)
        self.wait(1)

        def update_func(obj: OpenGLSurface, dt):
            obj.uv_func()
            print(dt)

        plane_surface.add_updater(update_function=update_func)
        self.wait(1)

        # self.play(FadeOut(plane_texture))

        # 赤道，和高相同
        cylinder_surface = OpenGLSurface(
            self.cylinder_func,
            u_range=[0, TAU],
            v_range=[-PI, PI],
            color=YELLOW,
            checkerboard_colors=[YELLOW, RED_E],
            resolution=(101, 51)
        )
        cylinder_texture = OpenGLTexturedSurface(uv_surface=cylinder_surface,
                                                 image_file="Whole_world_-_land_and_oceans_12000.jpg")
        # self.play(Create(texture))

        # self.play(ReplacementTransform(plane_texture, cylinder_texture))
        # shader_data= img_texture.get_shader_data()
        self.add(cylinder_texture)
        self.wait(5)


# "renderer": "opengl"
with tempconfig({"preview": True, "disable_caching": True}):
    WorldToSphere3().render()
    exit(1)
