from manim import *
from manim.mobject.geometry.tips import ArrowTriangleFilledTipSmall
from manim.mobject.opengl.opengl_cylinder import OpenGLCylinder
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_mobject import OpenGLGroup
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject, NumpyImage
from manim.mobject.opengl.opengl_shpere import OpenGLSphere
from manim.mobject.opengl.opengl_something import OpenGLCone, OpenGLLine3D, OpenGLArrow3D
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
import sympy as sp
from manim.typing import Image
from PIL import Image

class Euler001(ThreeDScene):
    """
    证明 饶 Z,Y,X 旋转的
    """
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))
        self.play(Create(axes))

        yawRad = 45 * DEGREES
        pitchRad = 45 * DEGREES
        rollRad = 45 * DEGREES
        Rz = np.array([
            [np.cos(yawRad), -np.sin(yawRad), 0],
            [np.sin(yawRad), np.cos(yawRad), 0],
            [0, 0, 1]
        ]);

        Ry = np.array([
            [np.cos(pitchRad), 0, np.sin(pitchRad)],
            [0, 1, 0],
            [-np.sin(pitchRad), 0, np.cos(pitchRad)]
        ]);

        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(rollRad), -np.sin(rollRad)],
            [0, np.sin(rollRad), np.cos(rollRad)]
        ]);

        axes1 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)

        axes1.add(axes1.get_axis_labels())
        axes1.set_color(YELLOW)
        self.play(Create(axes1))
        #
        # matrix = MathTex(r"""
        # M=\begin{bmatrix}
        # 1 & 0 & 0 & a\\
        # 0 & 1 & 0 & b\\
        # 0 & 0 & 1 & c\\
        # 0 & 0 & 0 & 1
        # \end{bmatrix}
        # """).move_to(UR).set_color(YELLOW).scale(0.8)
        # self.play(Create(matrix))


        animate = axes1.animate.apply_matrix(matrix=Rx)
        self.play(animate)
        self.wait()

        animate = axes1.animate.apply_matrix(matrix=Rx@Ry@Rx.T)
        self.play(animate)
        self.wait()
        #
        animate = axes1.animate.apply_matrix(matrix=(Rx@Ry)@Rz@(Rx@Ry).T)
        self.play(animate)
        self.wait()

class Euler_WorldDemo(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=-95 * DEGREES)
        axes1 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6,depth_test=True)

        axes1.add(axes1.get_axis_labels())
        axes1.set_color(YELLOW)

        self.begin_ambient_camera_rotation(rate=0.5)
        # self.camera.light_source.animate.move_to()
        def uv_func(u, v):
            return 1 * np.array([
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
        # 替换为你的纹理图片的路径 dark_image_file="world-night.jpg"
        texture = OpenGLTexturedSurface(uv_surface=sphere, image_file="world-daytime.jpg",dark_image_file="world-night.jpg",depth_test=True,opacity=0.5)
        self.add(texture)
        self.play(Create(axes1))
        self.wait(1)


class Euler_WorldDemo002(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=15 * DEGREES)
        x_axis = OpenGLArrow3D(start=[-3, 0, 0], end=[3, 0, 0], color=RED)
        y_axis = OpenGLArrow3D(start=[0, -3, 0], end=[0, 3, 0], color=GREEN)
        z_axis = OpenGLArrow3D(start=[0, 0, -3], end=[0, 0, 3], color=BLUE)
        # 添加箭头到场景中
        self.add(x_axis, y_axis, z_axis)
        # 创建并添加标签
        x_label = Text("x").next_to(x_axis.get_end(), RIGHT)
        y_label = Text("y").next_to(y_axis.get_end(), UP)
        z_label = Text("z").next_to(z_axis.get_end(), OUT)
        # 添加标签到场景中
        self.add(x_label, y_label, z_label)

        circle = Circle(radius=1.01, fill_color=WHITE, fill_opacity=1,depth_test=True)

        # self.begin_ambient_camera_rotation(rate=0.5)
        def uv_func(u, v):
            return 1 * np.array([
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

        earth = OpenGLTexturedSurface(uv_surface=sphere, image_file="world-daytime.jpg",dark_image_file="world-night.jpg",depth_test=True)

        self.add(circle)

        lon, lat = -63*DEGREES,127*DEGREES
        point = uv_func(lon, lat)
        beijing=OpenGLArrow3D(start=ORIGIN,end=point*1.3).set_color(YELLOW)
        self.add(beijing)
        self.add(earth)
        self.wait(1)

        yawRad = 45 * DEGREES
        pitchRad = 45 * DEGREES
        rollRad = 45 * DEGREES
        Rz = np.array([
            [np.cos(yawRad), -np.sin(yawRad), 0],
            [np.sin(yawRad), np.cos(yawRad), 0],
            [0, 0, 1]
        ]);

        Ry = np.array([
            [np.cos(pitchRad), 0, np.sin(pitchRad)],
            [0, 1, 0],
            [-np.sin(pitchRad), 0, np.cos(pitchRad)]
        ]);

        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(rollRad), -np.sin(rollRad)],
            [0, np.sin(rollRad), np.cos(rollRad)]
        ]);

        earth_animate= Rotate(earth,axis=OUT,angle=45*DEGREES)
        beijing_animate = Rotate(beijing,about_point=ORIGIN, axis=OUT, angle=45 * DEGREES)
        self.play(earth_animate,beijing_animate)

        self.wait()

        # animate = axes1.animate.apply_matrix(matrix=Rx@Ry@Rx.T)
        # self.play(animate)
        # self.wait()
        # #
        # animate = axes1.animate.apply_matrix(matrix=(Rx@Ry)@Rz@(Rx@Ry).T)
        # self.play(animate)
        # self.wait()

class Euler_WorldDemo001(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=15 * DEGREES)
        x_axis = OpenGLArrow3D(start=[-3, 0, 0], end=[3, 0, 0], color=RED)
        y_axis = OpenGLArrow3D(start=[0, -3, 0], end=[0, 3, 0], color=GREEN)
        z_axis = OpenGLArrow3D(start=[0, 0, -3], end=[0, 0, 3], color=BLUE)
        # 添加箭头到场景中
        self.add(x_axis, y_axis, z_axis)
        # 创建并添加标签
        x_label = Text("x").next_to(x_axis.get_end(), RIGHT)
        y_label = Text("y").next_to(y_axis.get_end(), UP)
        z_label = Text("z").next_to(z_axis.get_end(), OUT)
        # 添加标签到场景中
        self.add(x_label, y_label, z_label)

        circle = Circle(radius=1.01, fill_color=WHITE, fill_opacity=1,depth_test=True)

        # self.begin_ambient_camera_rotation(rate=0.5)
        def uv_func(u, v):
            return 1 * np.array([
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

        earth = OpenGLTexturedSurface(uv_surface=sphere, image_file="world-daytime.jpg",dark_image_file="world-night.jpg",depth_test=True,opacity=1)

        self.add(circle)

        lon, lat = -63*DEGREES,127*DEGREES
        point = uv_func(lon, lat)
        beijing=OpenGLArrow3D(start=ORIGIN,end=point*1.3).set_color(YELLOW)
        self.add(beijing)
        self.add(earth)
        self.wait(1)

        yawRad = 45 * DEGREES
        pitchRad = 45 * DEGREES
        rollRad = 45 * DEGREES
        Rz = np.array([
            [np.cos(yawRad), -np.sin(yawRad), 0],
            [np.sin(yawRad), np.cos(yawRad), 0],
            [0, 0, 1]
        ]);

        Ry = np.array([
            [np.cos(pitchRad), 0, np.sin(pitchRad)],
            [0, 1, 0],
            [-np.sin(pitchRad), 0, np.cos(pitchRad)]
        ]);

        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(rollRad), -np.sin(rollRad)],
            [0, np.sin(rollRad), np.cos(rollRad)]
        ]);


        beijing_animate = Rotate(beijing,about_point=ORIGIN, axis=OUT, angle=45 * DEGREES)
        self.play(beijing_animate)
        self.wait()

        # animate = axes1.animate.apply_matrix(matrix=Rx@Ry@Rx.T)
        # self.play(animate)
        # self.wait()
        # #
        # animate = axes1.animate.apply_matrix(matrix=(Rx@Ry)@Rz@(Rx@Ry).T)
        # self.play(animate)
        # self.wait()




# "#004000"
with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl","background_color" : "#004000"}):
    Euler_WorldDemo002().render()
    exit(1)
