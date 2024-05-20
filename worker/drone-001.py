from manim import *
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np


class Drone3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=15 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.5)
        # 创建一个3D坐标系
        axes = ThreeDAxes()
        self.add(axes)

        # 定义无人机的形状
        drone_body = Prism(dimensions=[1, 1, 0.5], fill_color=BLUE, fill_opacity=1).rotate(PI / 4)
        drone_arm = Cube(side_length=1, fill_color=RED, fill_opacity=1)
        drone_propeller = Circle(radius=0.2, color=GREEN, fill_opacity=1)
        cylinder = Cylinder(radius=0.5, show_ends=True, height=2, checkerboard_colors=[RED, YELLOW], stroke_color=GREEN,
                            fill_opacity=1)
        # cone = Cone(direction=X_AXIS + Y_AXIS + 2 * Z_AXIS, resolution=8)
        drone_arm = drone_arm.scale(np.array([2, 1, 1]))
        # 定义无人机的位置和旋转
        drone_body.move_to([0, 0, 0.25])
        drone_arm.move_to([0, 0, 0.05])
        drone_propeller.move_to([0, 0, 0.55])

        self.add_fixed_in_frame_mobjects(
            MarkupText("固定不动的文本", font="Source Han Sans CN", tex_template=TexTemplateLibrary.ctex).to_edge(UR))
        # 添加无人机的组件到场景中
        # self.add(drone_body)
        self.add(cylinder)
        # self.add(drone_propeller)

        # 添加动画效果，让无人机旋转
        # self.play(Rotate(drone_body, angle=PI/2, axis=OUT))
        self.play(Rotate(drone_propeller, angle=PI / 2, axis=OUT), run_time=1.5)
        self.move_camera(phi=45 * DEGREES, theta=115 * DEGREES)
        # self.add_foreground_mobject(drone_arm)
        self.wait(1)


class Drone4D(ThreeDScene):
    def construct(self):
        # 加载纹理图片

        # OpenGLSurface()

        # 创建一个球面并应用纹理
        # sphere = Sphere(radius=1, texture=texture)
        # 将球面添加到场景中
        # self.add(sphere)
        self.wait(1)


class ParametricSurfaceExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=15 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.5)
        # self.camera.light_source.animate.move_to()
        def uv_func(u, v):
            return 2 * np.array([
                np.cos(u) * np.sin(v),
                np.sin(u) * np.sin(v),
                -np.cos(v)
            ])
        #必须严格的 分辨率，范围
        sphere = OpenGLSurface(
            uv_func,
            u_range=[0, TAU],
            v_range=[0, PI],
            checkerboard_colors=[RED_D, RED_E],
            resolution=(101, 51))

        # 替换为你的纹理图片的路径
        texture = OpenGLTexturedSurface(uv_surface=sphere, image_file="world-daytime.jpg", dark_image_file="world-night.jpg")
        self.add(texture)
        self.wait(5)  # 显示一段时间
        # 创建一个移动光源的动画
        # move_animation = UpdateFromFunc(
        #     self.camera.light_source,
        #     lambda m: m.move_to(RIGHT+0.001)
        # )
        # # 播放移动动画
        # self.play(move_animation)


# "renderer": "opengl"
with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    ParametricSurfaceExample().render()
    exit(1)
