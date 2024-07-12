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

# 坐标轴 -三维的
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
        # self.add(earth)
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

        arc= Arc(start_angle=0,angle=45*DEGREES,arc_center=ORIGIN,radius=1.2,color=YELLOW)

        line= Line(start=ORIGIN,end=[1.2,0,0],depth_test=True).set_color(YELLOW)
        line_animate = Rotate(line, about_point=ORIGIN, axis=OUT, angle=45 * DEGREES)

        self.play(beijing_animate, Create(arc),line_animate)
        self.wait()
        # animate = axes1.animate.apply_matrix(matrix=Rx@Ry@Rx.T)
        # self.play(animate)
        # self.wait()
        # #
        # animate = axes1.animate.apply_matrix(matrix=(Rx@Ry)@Rz@(Rx@Ry).T)
        # self.play(animate)
        # self.wait()

class Euler_zxz_in(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=115 * DEGREES)
        axis_config = {
            # "include_tip": False,
            "numbers_to_include": None,
            "include_ticks": False,
        }
        axes = ThreeDAxes(include_numbers=False,
                          x_range=[0, 3, 1],
                          y_range=[0, 3, 1],
                          z_range=[0, 3, 1],
                          x_length=3, y_length=3, z_length=3,
                          axis_config=axis_config,)

        axes.add(axes.get_axis_labels())
        axes.set_color(BLUE_C)
        axes.shift(ORIGIN - axes.c2p(0, 0, 0))
        self.play(Create(axes))
        zRad = 30 * DEGREES
        yRad = 30 * DEGREES
        xRad = 30 * DEGREES
        Rz = np.array([
            [np.cos(zRad), -np.sin(zRad), 0],
            [np.sin(zRad), np.cos(zRad), 0],
            [0, 0, 1]
        ]);
        Ry = np.array([
            [np.cos(yRad), 0, np.sin(yRad)],
            [0, 1, 0],
            [-np.sin(yRad), 0, np.cos(yRad)]
        ]);
        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(xRad), -np.sin(xRad)],
            [0, np.sin(xRad), np.cos(xRad)]
        ]);

        axes1 = ThreeDAxes(include_numbers=False,
                           x_range=[0, 3, 1],
                           y_range=[0, 3, 1],
                           z_range=[0, 3, 1],
                           x_length=3, y_length=3, z_length=3,
                           axis_config=axis_config )
        # axes1.move_to(ORIGIN)
        axes1.shift(ORIGIN - axes1.c2p(0, 0, 0))
        circle = Circle(radius=3, color=BLUE_C, fill_opacity=0.1)
        # self.add(circle)
        self.play(Create(circle))
        axes1.add(axes1.get_axis_labels())
        axes1.set_color(RED)
        self.play(Create(axes1))

        alpha_arc = Arc(start_angle=0, angle=zRad, arc_center=ORIGIN)
        alpha_arc.add_tip(tip_length=0.15, tip_width=0.15)
        alpha_labels= MathTex(r"\alpha")
        alpha_labels.next_to(alpha_arc)
        alpha_labels.fix_orientation()

        animate = axes1.animate.apply_matrix(matrix=Rz)
        self.play(animate,Create(alpha_arc))
        self.play(Create(alpha_labels))
        # self.add(alpha_labels)
        self.wait()

        start_point=np.array([-3.2,0,0])
        end_point=np.array([4,0,0])
        start_point= (Rz @ start_point.T).T
        end_point =  (Rz @ end_point.T).T
        arrow = Arrow(start=start_point, end=end_point, color=GREEN)
        self.add(arrow)

        beta_arc = Arc(start_angle=90*DEGREES, angle=35*DEGREES, arc_center=ORIGIN)
        beta_arc.add_tip(tip_length=0.15, tip_width=0.15)
        beta_label = MathTex(r"\beta")
        beta_arc.rotate(axis=RIGHT,angle=90*DEGREES,about_point=ORIGIN)
        beta_arc.rotate(axis=OUT, angle=90*DEGREES, about_point=ORIGIN)
        beta_label.next_to(beta_arc, OUT)
        beta_label.fix_orientation()

        animate = axes1.animate.apply_matrix(matrix=Rz @ Rx @ Rz.T)
        self.play(animate,Create(beta_arc))
        # self.add(beta_label)
        self.play(Create(beta_label))
        self.wait()

        arrow_vector = arrow.get_vector()
        circle_red = Circle(radius=3, color=RED,fill_opacity=0.1)
        circle_red.rotate(axis=arrow_vector, angle=30 * DEGREES, about_point=ORIGIN)
        self.play(Create(circle_red))


        gamma_arc = Arc(start_angle=30*DEGREES, angle=30 * DEGREES, arc_center=ORIGIN,radius=1.5)
        gamma_arc.add_tip(tip_length=0.15, tip_width=0.15)
        gamma_label = MathTex(r"\gamma")
        gamma_arc.rotate(axis=arrow_vector, angle=30 * DEGREES, about_point=ORIGIN)
        gamma_label.next_to(gamma_arc, RIGHT+UP,buff=SMALL_BUFF)
        gamma_label.fix_orientation()


        animate = axes1.animate.apply_matrix(matrix=(Rz @ Rx) @ Rz @ (Rz @ Rx).T)
        self.play(animate,Create(gamma_arc))
        # self.add(gamma_label)
        self.play(FadeIn(gamma_label))
        self.wait()

class Euler_zxz_in2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=115 * DEGREES)
        axis_config = {
            # "include_tip": False,
            "numbers_to_include": None,
            "include_ticks": False,
        }
        axes = ThreeDAxes(include_numbers=False,
                          x_range=[0, 3, 1],
                          y_range=[0, 3, 1],
                          z_range=[0, 3, 1],
                          x_length=3, y_length=3, z_length=3,
                          axis_config=axis_config,)

        axes.add(axes.get_axis_labels())
        axes.set_color(BLUE_C)
        axes.shift(ORIGIN - axes.c2p(0, 0, 0))
        self.play(Create(axes))
        zRad = 30 * DEGREES
        yRad = 30 * DEGREES
        xRad = 30 * DEGREES
        Rz = np.array([
            [np.cos(zRad), -np.sin(zRad), 0],
            [np.sin(zRad), np.cos(zRad), 0],
            [0, 0, 1]
        ]);
        Ry = np.array([
            [np.cos(yRad), 0, np.sin(yRad)],
            [0, 1, 0],
            [-np.sin(yRad), 0, np.cos(yRad)]
        ]);
        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(xRad), -np.sin(xRad)],
            [0, np.sin(xRad), np.cos(xRad)]
        ]);

        axes1 = ThreeDAxes(include_numbers=False,
                           x_range=[0, 3, 1],
                           y_range=[0, 3, 1],
                           z_range=[0, 3, 1],
                           x_length=3, y_length=3, z_length=3,
                           axis_config=axis_config )

        axes1.shift(ORIGIN - axes1.c2p(0, 0, 0))
        circle = Circle(radius=3, color=BLUE_C, fill_opacity=0.1)
        self.play(Create(circle))
        axes1.add(axes1.get_axis_labels())
        axes1.set_color(RED)
        self.play(Create(axes1))

        alpha_arc = Arc(start_angle=0, angle=zRad, arc_center=ORIGIN)
        alpha_arc.add_tip(tip_length=0.15, tip_width=0.15)
        alpha_labels= MathTex(r"\alpha")
        alpha_labels.next_to(alpha_arc)
        alpha_labels.fix_orientation()

        animate = axes1.animate.apply_matrix(matrix=Rz)
        self.play(animate,Create(alpha_arc))
        self.play(Create(alpha_labels))
        self.wait()

        # 第二转
        y90= rotation_about_y(90 * DEGREES)
        circle_green = Circle(radius=3, color=GREEN, fill_opacity=0.1)
        circle_green.apply_matrix(matrix= Rz @ y90 @ Rz.T)
        self.play(Create(circle_green))


        start_point=np.array([-3.2,0,0])
        end_point=np.array([4,0,0])
        start_point= (Rz @ start_point.T).T
        end_point =  (Rz @ end_point.T).T
        arrow = Arrow(start=start_point, end=end_point, color=GREEN)
        self.add(arrow)

        beta_arc = Arc(start_angle=90*DEGREES, angle=40*DEGREES, arc_center=ORIGIN)
        beta_arc.add_tip(tip_length=0.15, tip_width=0.15)
        beta_label = MathTex(r"\beta")


        beta_arc.rotate(axis=RIGHT,angle=90*DEGREES,about_point=ORIGIN)
        beta_arc.rotate(axis=OUT, angle=90*DEGREES, about_point=ORIGIN)
        beta_label.next_to(beta_arc, OUT)
        beta_label.fix_orientation()

        animate = axes1.animate.apply_matrix(matrix=Rz @ Rx @ Rz.T)
        self.play(animate,Create(beta_arc))
        self.play(Create(beta_label))
        self.wait()

        # 第三转
        arrow_vector = arrow.get_vector()
        circle_red = Circle(radius=3, color=RED,fill_opacity=0.1)
        circle_red.apply_matrix(matrix=Rz @ Rx @ Rz.T)
        # circle_red.rotate(axis=arrow_vector, angle=30 * DEGREES, about_point=ORIGIN)
        self.play(Create(circle_red))


        gamma_arc = Arc(start_angle=30*DEGREES, angle=30 * DEGREES, arc_center=ORIGIN,radius=1.5)
        gamma_arc.add_tip(tip_length=0.15, tip_width=0.15)
        gamma_label = MathTex(r"\gamma")
        gamma_arc.apply_matrix(matrix=Rz @ Rx @ Rz.T)
        # gamma_arc.rotate(axis=arrow_vector, angle=30 * DEGREES, about_point=ORIGIN)
        gamma_label.next_to(gamma_arc, RIGHT+UP,buff=SMALL_BUFF)
        gamma_label.fix_orientation()


        animate = axes1.animate.apply_matrix(matrix=(Rz @ Rx) @ Rz @ (Rz @ Rx).T)
        self.play(animate,Create(gamma_arc))
        self.play(FadeIn(gamma_label))
        self.wait()

class Euler_zxy_in(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=115 * DEGREES)
        axis_config = {
            # "include_tip": False,
            "numbers_to_include": None,
            "include_ticks": False,
        }
        axes = ThreeDAxes(include_numbers=False,
                          x_range=[0, 3, 1],
                          y_range=[0, 3, 1],
                          z_range=[0, 3, 1],
                          x_length=3, y_length=3, z_length=3,
                          axis_config=axis_config,)

        axes.add(axes.get_axis_labels())
        axes.set_color(BLUE_C)
        axes.shift(ORIGIN - axes.c2p(0, 0, 0))
        self.play(Create(axes))
        zRad = 30 * DEGREES
        yRad = -45 * DEGREES
        xRad = 30 * DEGREES
        Rz = np.array([
            [np.cos(zRad), -np.sin(zRad), 0],
            [np.sin(zRad), np.cos(zRad), 0],
            [0, 0, 1]
        ]);
        Ry = np.array([
            [np.cos(yRad), 0, np.sin(yRad)],
            [0, 1, 0],
            [-np.sin(yRad), 0, np.cos(yRad)]
        ]);
        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(xRad), -np.sin(xRad)],
            [0, np.sin(xRad), np.cos(xRad)]
        ]);

        axes1 = ThreeDAxes(include_numbers=False,
                           x_range=[0, 3, 1],
                           y_range=[0, 3, 1],
                           z_range=[0, 3, 1],
                           x_length=3, y_length=3, z_length=3,
                           axis_config=axis_config )

        axes1.shift(ORIGIN - axes1.c2p(0, 0, 0))
        circle = Circle(radius=3, color=BLUE_C, fill_opacity=0.1)
        self.play(Create(circle))
        axes1.add(axes1.get_axis_labels())
        axes1.set_color(RED)
        self.play(Create(axes1))

        alpha_arc = Arc(start_angle=0, angle=zRad, arc_center=ORIGIN)
        alpha_arc.add_tip(tip_length=0.15, tip_width=0.15)
        alpha_labels= MathTex(r"\psi").scale(0.5)
        alpha_labels.next_to(alpha_arc)
        alpha_labels.fix_orientation()

        animate = axes1.animate.apply_matrix(matrix=Rz)
        self.play(animate,Create(alpha_arc))
        self.play(Create(alpha_labels))
        self.wait()

        # self.move_camera(phi=60 * DEGREES, theta=45 * DEGREES)
        self.move_camera(phi=60 * DEGREES, theta=0 * DEGREES)
        # 第二转
        # circle_green = Circle(radius=3, color=GREEN, fill_opacity=0.1)
        # circle_green.rotate(axis=RIGHT, angle=90 * DEGREES, about_point=ORIGIN)
        # circle_green.apply_matrix(matrix=Rz @ Ry)
        # self.play(Create(circle_green))


        start_point=np.array([-3.2,0,0])
        end_point=np.array([4,0,0])
        start_point= (Rz @ start_point.T).T
        end_point =  (Rz @ end_point.T).T
        arrow1 = Arrow(start=start_point, end=end_point, color=GREEN)
        dashed_arrow = DashedVMobject(arrow1, num_dashes=20, dashed_ratio=0.5)
        self.add(dashed_arrow)

        start_point2 = np.array([ 0,-3.2, 0])
        end_point2 = np.array([ 0,4, 0])
        start_point2 = (Rz @ start_point2.T).T
        end_point2 = (Rz @ end_point2.T).T
        arrow2 = Arrow(start=start_point2, end=end_point2, color=GREEN)


        beta_arc = Arc(start_angle=0, angle=-yRad, arc_center=ORIGIN)
        beta_arc.add_tip(tip_length=0.15, tip_width=0.15)
        beta_label = MathTex(r"\theta")


        beta_arc.rotate(axis=RIGHT,angle=90*DEGREES,about_point=ORIGIN)
        beta_arc.apply_matrix(matrix=Rz)
        # beta_arc.rotate(axis=OUT, angle=30*DEGREES, about_point=ORIGIN)
        beta_label.next_to(beta_arc, UR).scale(0.5)
        beta_label.fix_orientation()

        animate = axes1.animate.apply_matrix(matrix=Rz @ Ry @ Rz.T)
        self.play(animate,Create(beta_arc))
        self.play(Create(beta_label))
        self.wait()


        # 第三转

        circle_red = Circle(radius=3, color=RED,fill_opacity=0.1)
        circle_red.rotate(axis=UP, angle=90 * DEGREES, about_point=ORIGIN)
        circle_red.apply_matrix(matrix=Rz@Ry)
        self.play(Create(circle_red))
        self.add(arrow2)
        self.move_camera(phi=60 * DEGREES, theta=0 * DEGREES)
        self.move_camera(phi=60 * DEGREES, theta=45 * DEGREES)


        gamma_arc = Arc(start_angle=90*DEGREES, angle=xRad, arc_center=ORIGIN,radius=1)
        gamma_arc.rotate(axis=UP, angle=90 * DEGREES, about_point=ORIGIN)
        gamma_arc.apply_matrix(matrix=Rz @ Ry)

        gamma_arc.add_tip(tip_length=0.15, tip_width=0.15)
        gamma_label = MathTex(r"\varphi").scale(0.5)
        gamma_label.next_to(gamma_arc, RIGHT+OUT)
        gamma_label.fix_orientation()


        animate = axes1.animate.apply_matrix(matrix=(Rz @ Ry) @ Rx @ (Rz @ Ry).T)
        self.play(animate,Create(gamma_arc))
        self.play(FadeIn(gamma_label))
        self.wait()
        self.move_camera(phi=60 * DEGREES, theta=115 * DEGREES)
        self.wait()


# "#004000"
with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl","background_color" : "#000000"}):
    Euler_zxy_in().render()
    exit(1)
