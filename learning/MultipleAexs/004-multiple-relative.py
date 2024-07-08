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


# 相机 一步动画--- 改正确
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


        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=matrix_init@Rz@Ry@Rx@matrix_init.T)
        self.play(animate)

        self.begin_ambient_camera_rotation(rate=0.2)

        self.wait(1)


# 相机 北东地 分布动画 --改正确
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

        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=Ry)
        self.play(animate)

        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=Rz)
        self.play(animate)

        # animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=Rx)
        # self.play(animate)

        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=matrix_init)
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


        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=Rx)
        self.play(animate)

        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=Ry)
        self.play(animate)

        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix=Rz)
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

        animate = group.animate.apply_matrix(about_point=[2, 2, 2], matrix= matrix_init@Rz@Ry@Rx)
        self.play(animate)
        self.begin_ambient_camera_rotation(rate=-0.2)
        self.wait(1)


class Prove_ZYX_Rotate_Matrix(ThreeDScene):
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

# 绕x,y,z旋转 并且带有一个 平移- 正对  M R M^-1 形式
class Prove_ZYX_and_move_Rotate_Matrix(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)
        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        self.add(axes)

        axes1 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)

        axes1.add(axes1.get_axis_labels())
        axes1.set_color(YELLOW)
        self.play(Create(axes1))
        self.wait()

        T_matrix=np.array([
            [1, 0, 0,2],
            [0, 1, 0,2],
            [0, 0, 1,0],
            [0, 0, 0,1]
        ]);
        T_matrix_inv= np.linalg.inv(T_matrix)

        yawRad = 45 * DEGREES
        pitchRad = 45 * DEGREES
        rollRad = 45 * DEGREES
        Rz = np.array([
            [np.cos(yawRad), -np.sin(yawRad), 0,0],
            [np.sin(yawRad), np.cos(yawRad), 0,0],
            [0, 0, 1,0],
            [0, 0, 0, 1]
        ]);

        Ry = np.array([
            [np.cos(pitchRad), 0, np.sin(pitchRad),0],
            [0, 1, 0,0],
            [-np.sin(pitchRad), 0, np.cos(pitchRad),0],
            [0, 0, 0, 1]
        ]);

        Rx = np.array([
            [1, 0, 0,0],
            [0, np.cos(rollRad), -np.sin(rollRad),0],
            [0, np.sin(rollRad), np.cos(rollRad),0],
            [0, 0, 0, 1]
        ]);


        for mob in axes1.family_members_with_points():
            # mob.points
            # 将points转换为齐次坐标
            homogenous_points = np.hstack((mob.points, np.ones((mob.points.shape[0], 1))))
            # 应用变换矩阵T
            transformed_points = T_matrix@homogenous_points.T
            # 更新mobject的points属性
            mob.points = transformed_points.T[:, :3]

        M0 = T_matrix
        self.wait()

        for mob in axes1.family_members_with_points():
            homogenous_points = np.hstack((mob.points, np.ones((mob.points.shape[0], 1))))
            transformed_points = M0 @ Rz @ np.linalg.inv(M0) @homogenous_points.T
            mob.points = transformed_points.T[:, :3]
        self.wait()
        M1 = T_matrix@Rz

        for mob in axes1.family_members_with_points():
            homogenous_points = np.hstack((mob.points, np.ones((mob.points.shape[0], 1))))

            transformed_points = M1 @ Ry @ np.linalg.inv(M1) @ homogenous_points.T
            mob.points = transformed_points.T[:, :3]
        self.wait()

        M2 = T_matrix@Rz@Ry
        for mob in axes1.family_members_with_points():
            homogenous_points = np.hstack((mob.points, np.ones((mob.points.shape[0], 1))))
            transformed_points = M2 @ Rx @ np.linalg.inv(M2) @ homogenous_points.T
            mob.points = transformed_points.T[:, :3]
        self.wait()
        M3 = T_matrix @ Rz @ Ry @ Rx





with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl"}):
    Prove_ZYX_and_move_Rotate_Matrix().render()
    exit(1)
