from manim import *
from manim.mobject.opengl.opengl_cylinder import OpenGLCylinder
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject, NumpyImage
from manim.mobject.opengl.opengl_shpere import OpenGLSphere
from manim.mobject.opengl.opengl_something import OpenGLCone, OpenGLLine3D, OpenGLArrow3D
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
import sympy as sp
from manim.typing import Image
from PIL import Image


#
class MultipleRelative001(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))
        self.play(Create(axes))

        axes1 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)

        axes1.add(axes1.get_axis_labels())
        axes1.set_color(YELLOW)
        self.play(Create(axes1))

        rad = -30 * DEGREES
        matrix_y = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
        self.play(ApplyMethod(axes1.apply_matrix, matrix_y))

        self.play(axes1.animate.shift([2, 2, 2]))

        self.move_camera(zoom=0.8, run_time=2)

        dot = Dot3D(point=[4, -4, 1], depth_test=False)

        arrow1 = OpenGLArrow3D(start=np.array([0, 0, 0]), end=[4, -4, 1], depth_test=False)

        arrow2 = OpenGLArrow3D(start=np.array([2, 2, 2]), end=[4, -4, 1], depth_test=False).set_color(YELLOW)

        self.play(Create(arrow1), Create(arrow2))
        self.play(Create(dot))

        labes = MathTex(r"P(4,-4,1)").scale(0.5)
        labes.shift([4, -4, 1])
        self.add_fixed_orientation_mobjects(labes)

        arrow_t = OpenGLArrow3D(start=np.array([0, 0, 0]), end=[2, 2, 2])
        self.play(Create(arrow_t))

        self.begin_ambient_camera_rotation(rate=0.1)

        self.wait(1)

        matrix = MathTex(r"""
        M
        =
        \begin{bmatrix}
        1 & 0& 0\\
        0 & 1& 0\\
        0 & 0& 1
        \end{bmatrix} """).scale(0.8)

        matrix2 = MathTex(r"""
        M =
        \begin{bmatrix} 
        cos(30) & -sin(30) &0 \\ 
        sin(30) & cos(30) &0\\
        0 & 0 &1
        \end{bmatrix} """).set_color(YELLOW).scale(0.55)

        self.add_fixed_in_frame_mobjects(matrix.to_corner(UL))

        self.add_fixed_in_frame_mobjects(matrix2.next_to(matrix, DOWN))

        self.wait(3)


class MultipleRelative001_1(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))
        self.play(Create(axes))

        axes1 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)

        axes1.add(axes1.get_axis_labels())
        axes1.set_color(YELLOW)
        self.play(Create(axes1))

        rad = -30 * DEGREES
        matrix_y = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
        self.play(ApplyMethod(axes1.apply_matrix, matrix_y))

        self.play(axes1.animate.shift([2, 2, 2]))

        self.move_camera(zoom=0.8, run_time=2)

        dot = Dot3D(point=[4, -4, 1], depth_test=False)

        arrow1 = OpenGLArrow3D(start=np.array([0, 0, 0]), end=[4, -4, 1], depth_test=False)

        arrow2 = OpenGLArrow3D(start=np.array([2, 2, 2]), end=[4, -4, 1], depth_test=False).set_color(YELLOW)

        self.play(Create(arrow1), Create(arrow2))
        self.play(Create(dot))

        labes = MathTex(r"P(4,-4,1)").scale(0.5)
        labes.shift([4, -4, 1])
        self.add_fixed_orientation_mobjects(labes)

        arrow_t = OpenGLArrow3D(start=np.array([0, 0, 0]), end=[2, 2, 2])
        self.play(Create(arrow_t))



        # matrix = MathTex(r"""
        # M
        # =
        # \begin{bmatrix}
        # 1 & 0& 0\\
        # 0 & 1& 0\\
        # 0 & 0& 1
        # \end{bmatrix} """).scale(0.8)
        #
        # matrix2 = MathTex(r"""
        # M =
        # \begin{bmatrix}
        # cos(30) & -sin(30) &0 \\
        # sin(30) & cos(30) &0\\
        # 0 & 0 &1
        # \end{bmatrix} """).set_color(YELLOW).scale(0.55)
        #
        # self.add_fixed_in_frame_mobjects(matrix.to_corner(UL))
        #
        # self.add_fixed_in_frame_mobjects(matrix2.next_to(matrix, DOWN))

        rad = -60 * DEGREES
        matrix_y1 = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])

        axes2 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)

        axes2.add(axes2.get_axis_labels())
        axes2.set_color(RED)
        self.play(Create(axes2))
        self.play(ApplyMethod(axes2.apply_matrix, matrix_y1))
        self.play(axes2.animate.shift([-2, -2, 2]))


        self.begin_ambient_camera_rotation(rate=0.1)

        self.wait(1)


class MultipleRelative001_2(ThreeDScene):
    def construct(self):
        self.next_section(skip_animations=False)
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))
        self.play(Create(axes))

        axes1 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)

        axes1.add(axes1.get_axis_labels())
        axes1.set_color(YELLOW)
        self.play(Create(axes1))

        rad = -30 * DEGREES
        matrix_y = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
        self.play(ApplyMethod(axes1.apply_matrix, matrix_y))

        self.play(axes1.animate.shift([2, 2, 2]))

        self.move_camera(zoom=0.8, run_time=2)

        dot = Dot3D(point=[4, -4, 1], depth_test=False)

        arrow1 = OpenGLArrow3D(start=np.array([0, 0, 0]), end=[4, -4, 1], depth_test=False)

        arrow2 = OpenGLArrow3D(start=np.array([2, 2, 2]), end=[4, -4, 1], depth_test=False).set_color(YELLOW)

        self.play(Create(arrow1), Create(arrow2))
        self.play(Create(dot))

        labes = MathTex(r"P(4,-4,1)").scale(0.5)
        labes.shift([4, -4, 1])
        self.add_fixed_orientation_mobjects(labes)

        arrow_t = OpenGLArrow3D(start=np.array([0, 0, 0]), end=[2, 2, 2])
        self.play(Create(arrow_t))



        rad = -60 * DEGREES
        matrix_y1 = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
        pitchRad=36.7*DEGREES
        matrix_z = np.array([
            [np.cos(pitchRad), 0, np.sin(pitchRad)],
            [0, 1, 0],
            [-np.sin(pitchRad), 0, np.cos(pitchRad)]
        ]);

        axes2 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)

        axes2.add(axes2.get_axis_labels())
        axes2.set_color(RED)
        self.play(Create(axes2))
        self.play(ApplyMethod(axes2.apply_matrix, matrix_y1@matrix_z))
        self.play(axes2.animate.move_to([-2, -2, 2]))
        self.wait(1)
        self.next_section(skip_animations=False)

        animate = axes1.animate.apply_matrix(about_point=axes1.get_center(), matrix=matrix_y.T)
        self.play(animate)
        self.wait(1)
        animate = axes1.animate.apply_matrix(about_point=axes1.get_center(), matrix=matrix_y1@matrix_z)
        self.play(animate)
        self.wait(1)
        self.play(axes1.animate.move_to([-2, -2, 2]))

        self.begin_ambient_camera_rotation(rate=0.1)

        self.wait(1)
# 相机 一步动画--- 错误的
class MultipleRelative002(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))
        self.play(Create(axes))

        axes1 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)

        labels = axes1.get_axis_labels(x_label=MarkupText("北").scale(0.5), y_label=MarkupText("东").scale(0.5),
                                       z_label=MarkupText("地").scale(0.5))
        axes1.add(labels)
        axes1.set_color(YELLOW)

        def uv_func(u, v):
            x = 1
            y = u
            z = v
            return [x, y, z]

        planSurface = OpenGLSurface(uv_func=uv_func, u_range=[-0.4, 0.4], v_range=[-0.3, 0.3],
                                    depth_test=False).set_color(RED).set_opacity(0.5)

        self.play(Create(planSurface))
        self.play(Create(axes1))

        group = Group()
        group.add(planSurface, axes1)

        rad = -30 * DEGREES
        matrix_init = np.array([
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, -1]
        ])
        self.play(ApplyMethod(group.apply_matrix, matrix_init))

        self.play(group.animate.shift([2, 2, 2]))

        self.move_camera(zoom=0.75, run_time=2)

        yawRad = -34.3 * DEGREES
        pitchRad = -47.4 * DEGREES
        # pitchRad = -45 * DEGREES
        rollRad = 0.0
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


        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=matrix_init.T@ Ry@Rz@matrix_init.T)
        self.play(animate)


        self.begin_ambient_camera_rotation(rate=0.2)

        self.wait(1)

# 相机 一步动画--- 改正确
class MultipleRelative0022(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))
        self.play(Create(axes))

        axes1 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)

        labels = axes1.get_axis_labels(x_label=MarkupText("北").scale(0.5), y_label=MarkupText("东").scale(0.5),
                                       z_label=MarkupText("地").scale(0.5))
        axes1.add(labels)
        axes1.set_color(YELLOW)

        def uv_func(u, v):
            x = 1
            y = u
            z = v
            return [x, y, z]

        planSurface = OpenGLSurface(uv_func=uv_func, u_range=[-0.4, 0.4], v_range=[-0.3, 0.3],
                                    depth_test=False).set_color(RED).set_opacity(0.5)

        self.play(Create(planSurface))
        self.play(Create(axes1))

        group = Group()
        group.add(planSurface, axes1)

        rad = -30 * DEGREES
        matrix_init = np.array([
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, -1]
        ])
        self.play(ApplyMethod(group.apply_matrix, matrix_init))

        self.play(group.animate.shift([2, 2, 2]))

        self.move_camera(zoom=0.75, run_time=2)

        yawRad = -34.3 * DEGREES
        pitchRad = -47.4 * DEGREES
        # pitchRad = -45 * DEGREES
        rollRad = 0.0
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


        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=matrix_init.T@ Ry@Rz@matrix_init.T)
        self.play(animate)


        self.begin_ambient_camera_rotation(rate=0.2)

        self.wait(1)
# 相机 北东地 分布动画 --错的
class MultipleRelative003(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))
        self.play(Create(axes))

        axes1 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)
        labels= axes1.get_axis_labels(x_label=MarkupText("北").scale(0.5), y_label=MarkupText("东").scale(0.5),
                              z_label=MarkupText("地").scale(0.5))
        axes1.add(labels)
        axes1.set_color(YELLOW)

        def uv_func(u, v):
            x = 1
            y = u
            z = v
            return [x, y, z]

        planSurface = OpenGLSurface(uv_func=uv_func, u_range=[-0.4, 0.4], v_range=[-0.3, 0.3],
                                    depth_test=False).set_color(RED).set_opacity(0.5)

        self.play(Create(planSurface))
        self.play(Create(axes1))

        group = Group()
        group.add(planSurface, axes1)


        matrix_init = np.array([
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, -1]
        ])
        self.play(ApplyMethod(group.apply_matrix, matrix_init))

        self.play(group.animate.shift([2, 2, 2]))

        self.move_camera(zoom=0.75, run_time=2)

        yawRad = -34.3 * DEGREES
        pitchRad = -47.4 * DEGREES
        # pitchRad = -45 * DEGREES
        rollRad = 0.0
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



        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=Rz)
        self.play(animate)

        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=Ry)
        self.play(animate)

        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=Rx)
        self.play(animate)

        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=matrix_init)
        self.play(animate)

# 相机 北东地 分布动画 --改正确
class MultipleRelative0032(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))
        self.play(Create(axes))

        axes1 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)
        labels= axes1.get_axis_labels(x_label=MarkupText("北 X").scale(0.5), y_label=MarkupText("东 Y").scale(0.5),
                              z_label=MarkupText("地 -Z").scale(0.5))
        axes1.add(labels)
        axes1.set_color(YELLOW)

        def uv_func(u, v):
            x = 1
            y = u
            z = v
            return [x, y, z]

        planSurface = OpenGLSurface(uv_func=uv_func, u_range=[-0.4, 0.4], v_range=[-0.3, 0.3],
                                    depth_test=False).set_color(RED).set_opacity(0.5)

        self.play(Create(planSurface))
        self.play(Create(axes1))

        group = Group()
        group.add(planSurface, axes1)


        matrix_init = np.array([
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, -1]
        ])
        self.play(ApplyMethod(group.apply_matrix, matrix_init))

        self.play(group.animate.shift([2, 2, 2]))

        self.move_camera(zoom=0.75, run_time=2)

        yawRad = -34.3 * DEGREES
        pitchRad = -47.4 * DEGREES
        # pitchRad = -45 * DEGREES
        rollRad = 0.0
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


        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=matrix_init.T)
        self.play(animate)


        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=Rz)
        self.play(animate)

        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=Ry)
        self.play(animate)

        # animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=Rx)
        # self.play(animate)

        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=matrix_init.T)
        self.play(animate)


# 相机 北东地  先不旋转- 最后一步转 -分部
class MultipleRelative004(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))
        self.play(Create(axes))

        axes1 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)

        axes1.add(axes1.get_axis_labels(x_label=MarkupText("北").scale(0.5), y_label=MarkupText("东").scale(0.5),
                                        z_label=MarkupText("地").scale(0.5)))
        axes1.set_color(YELLOW)

        def uv_func(u, v):
            x = 1
            y = u
            z = v
            return [x, y, z]

        planSurface = OpenGLSurface(uv_func=uv_func, u_range=[-0.4, 0.4], v_range=[-0.3, 0.3],
                                    depth_test=False).set_color(RED).set_opacity(0.5)

        self.play(Create(planSurface))
        self.play(Create(axes1))

        group = Group()
        group.add(planSurface, axes1)


        matrix_init = np.array([
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, -1]
        ])
        # self.play(ApplyMethod(group.apply_matrix, matrix_init))

        self.play(group.animate.shift([2, 2, 2]))

        self.move_camera(zoom=0.75, run_time=2)

        yawRad = -34.3 * DEGREES
        pitchRad = -47.4 * DEGREES
        rollRad = 0.0
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



        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=Rz)
        self.play(animate)

        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=Ry)
        self.play(animate)

        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=Rx)
        self.play(animate)

        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=matrix_init)
        self.play(animate)

# 相机 北东地  先不旋转- 一步转
class MultipleRelative005(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))
        self.play(Create(axes))

        axes1 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)

        axes1.add(axes1.get_axis_labels(x_label=MarkupText("北").scale(0.5), y_label=MarkupText("东").scale(0.5),
                                        z_label=MarkupText("地").scale(0.5)))
        axes1.set_color(YELLOW)

        def uv_func(u, v):
            x = 1
            y = u
            z = v
            return [x, y, z]

        planSurface = OpenGLSurface(uv_func=uv_func, u_range=[-0.4, 0.4], v_range=[-0.3, 0.3],
                                    depth_test=False).set_color(RED).set_opacity(0.5)

        self.play(Create(planSurface))
        self.play(Create(axes1))

        group = Group()
        group.add(planSurface, axes1)

        matrix_init = np.array([
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, -1]
        ])

        self.play(group.animate.shift([2, 2, 2]))

        self.move_camera(zoom=0.75, run_time=2)

        yawRad = -34.3 * DEGREES
        pitchRad = -47.4 * DEGREES
        rollRad = 0.0
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

        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix= matrix_init@Rx@Ry@Rz)
        self.play(animate)
        self.begin_ambient_camera_rotation(rate=-0.2)
        self.wait(1)



with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl"}):
    MultipleRelative001_2().render()
    # MultipleAexs002().render()
    exit(1)
