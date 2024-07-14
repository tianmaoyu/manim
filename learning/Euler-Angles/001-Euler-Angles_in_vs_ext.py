from manim import *
from manim.mobject.geometry.tips import ArrowTriangleFilledTipSmall

from manim.mobject.opengl.opengl_something import OpenGLCone, OpenGLLine3D, OpenGLArrow3D
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np




class Euler_zxy_in_vector(ThreeDScene):
    def init_label (self,point):
        x,y,z=point
        self.num_x = DecimalNumber(number=x)
        self.num_y = DecimalNumber(number=y)
        self.num_z = DecimalNumber(number=z)

        self.tracker_x = ValueTracker(x)
        self.tracker_y = ValueTracker(y)
        self.tracker_z = ValueTracker(z)

        self.num_x.add_updater(lambda m: m.set_value(self.tracker_x.get_value()))
        self.num_y.add_updater(lambda m: m.set_value(self.tracker_y.get_value()))
        self.num_z.add_updater(lambda m: m.set_value(self.tracker_z.get_value()))

    def get_label_animate(self,point):
        animate_x= self.tracker_x.animate.set_value(10)
        animate_y = self.tracker_y.animate.set_value(10)
        animate_z = self.tracker_z.animate.set_value(10)
        return animate_x,animate_y,animate_z


    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=115 * DEGREES)
        # point_label = (MathTex(r"P(2,2,2)")
        #                .next_to(mobject_or_point=[2,2,2],direction=RIGHT)
        #                .fix_orientation())
        # point_label.scale(0.5)

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
        xRad = 60 * DEGREES
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
        axes1.set_color(RED).set_opacity(0.5)

        vector = OpenGLArrow3D(start=ORIGIN, end=[2, 2, 2], color=YELLOW)

        self.play(Create(axes1),Create(vector))

        # self.play(ReplacementTransform(point_label,MathTex(r"P(5,5,5)").to_corner(UL).fix_in_frame()))
        self.wait()

        # 一
        alpha_arc = Arc(start_angle=0, angle=zRad, arc_center=ORIGIN)
        alpha_arc.add_tip(tip_length=0.15, tip_width=0.15)
        alpha_labels= MathTex(r"\psi")
        alpha_labels.next_to(alpha_arc)
        alpha_labels.fix_orientation()

        animate = axes1.animate.apply_matrix(matrix=Rz)
        animate_vector = vector.animate.apply_matrix(matrix=Rz)

        self.play(animate,animate_vector,Create(alpha_arc),run_time=2)
        self.play(FadeIn(alpha_labels))
        self.wait()
        # 二

        start_point=np.array([-3.2,0,0])
        end_point=np.array([4,0,0])
        start_point= (Rz @ start_point.T).T
        end_point =  (Rz @ end_point.T).T
        arrow1 = Arrow(start=start_point, end=end_point, color=GREEN).set_opacity(0.5)
        dashed_arrow = DashedVMobject(arrow1, num_dashes=20, dashed_ratio=0.5)
        self.add(dashed_arrow)

        start_point2 = np.array([ 0,-3.2, 0])
        end_point2 = np.array([ 0,4, 0])
        start_point2 = (Rz @ start_point2.T).T
        end_point2 = (Rz @ end_point2.T).T
        arrow2 = Arrow(start=start_point2, end=end_point2, color=GREEN).set_opacity(0.5)


        beta_arc = Arc(start_angle=0, angle=-yRad, arc_center=ORIGIN)
        beta_arc.add_tip(tip_length=0.15, tip_width=0.15)
        beta_label = MathTex(r"\theta")


        beta_arc.rotate(axis=RIGHT,angle=90*DEGREES,about_point=ORIGIN)
        beta_arc.apply_matrix(matrix=Rz)
        beta_label.next_to(beta_arc, UR+OUT)
        beta_label.fix_orientation()

        animate = axes1.animate.apply_matrix(matrix=Rz @ Ry @ Rz.T)
        animate_vector = vector.animate.apply_matrix(matrix=Rz @ Ry @ Rz.T)
        self.play(animate,animate_vector,Create(beta_arc),run_time=2)
        self.play(FadeIn(beta_label))
        self.wait()


        # 第三转
        circle_red = Circle(radius=3,stroke_width=1, color=RED,fill_opacity=0.1)
        circle_red.rotate(axis=UP, angle=90 * DEGREES, about_point=ORIGIN)
        circle_red.apply_matrix(matrix=Rz@Ry)
        self.play(Create(circle_red))
        self.add(arrow2)



        gamma_arc = Arc(start_angle=90*DEGREES, angle=xRad, arc_center=ORIGIN,radius=1)
        gamma_arc.rotate(axis=UP, angle=90 * DEGREES, about_point=ORIGIN)
        gamma_arc.apply_matrix(matrix=Rz @ Ry)

        gamma_arc.add_tip(tip_length=0.15, tip_width=0.15)
        gamma_label = MathTex(r"\varphi")
        gamma_label.next_to(gamma_arc, UP)
        gamma_label.fix_orientation()


        animate = axes1.animate.apply_matrix(matrix=(Rz @ Ry) @ Rx @ (Rz @ Ry).T)
        animate_vector = vector.animate.apply_matrix(matrix=(Rz @ Ry) @ Rx @ (Rz @ Ry).T)
        self.play(animate,animate_vector,Create(gamma_arc),run_time=2)
        self.play(FadeIn(gamma_label))
        self.wait()
        # 最后
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(14)

# 注意 绕Y 旋转的角是负 角，未了更维基百科，保持一致
class Euler_xyz_ext_vector(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)
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
        zRad = 60 * DEGREES
        yRad = -45 * DEGREES
        xRad = 30 * DEGREES

        zRad = 30 * DEGREES
        yRad = -45 * DEGREES
        xRad= 60 * DEGREES

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
        axes1.set_color(RED).set_opacity(0.5)

        vector_= np.array([2, 2, 2])
        # vector_=(Rx@ Ry@ Rz@ vector_.T).T

        vector = OpenGLArrow3D(start=ORIGIN, end=vector_, color=YELLOW)


        self.play(Create(axes1),Create(vector))


        circle_red = Circle(radius=3, color=RED,stroke_width=1, fill_opacity=0.1)
        circle_red.rotate(axis=UP, angle=90 * DEGREES, about_point=ORIGIN)
        self.play(Create(circle_red))

        # 第三次转

        gamma_arc = Arc(start_angle=90 * DEGREES, angle=xRad, arc_center=ORIGIN, radius=1)
        gamma_arc.add_tip(tip_length=0.15, tip_width=0.15)
        gamma_arc.rotate(axis=UP, angle=90 * DEGREES, about_point=ORIGIN)

        gamma_label = MathTex(r"\varphi")
        gamma_label.next_to(gamma_arc, UP)
        gamma_label.fix_orientation()

        arrow = Arrow(start=ORIGIN, end=[0, 4, 0], stroke_width=3, color=GREEN, tip_shape=ArrowTriangleFilledTipSmall)
        dashed_arrow = DashedVMobject(arrow, num_dashes=20, dashed_ratio=0.5)
        arrow_animate = dashed_arrow.animate.apply_matrix(matrix=Rx).set_opacity(0.5)

        animate = axes1.animate.apply_matrix(matrix=Rx)
        circle_red_animate = circle_red.animate.apply_matrix(matrix=Rx)
        vector_animate = vector.animate.apply_matrix(matrix=Rx)
        self.play(animate, circle_red_animate,vector_animate, arrow_animate, Create(gamma_arc), run_time=2)

        self.play(FadeIn(gamma_label))
        self.wait()

        # 第二转

        # beta_arc = Arc(start_angle=90 * DEGREES, angle=-yRad, arc_center=ORIGIN)
        # beta_arc.add_tip(tip_length=0.15, tip_width=0.15)
        # beta_arc.rotate(axis=RIGHT, angle=90 * DEGREES, about_point=ORIGIN)
        beta_arc = Arc(start_angle=0, angle=-yRad, arc_center=ORIGIN)
        beta_arc.add_tip(tip_length=0.15, tip_width=0.15)
        beta_arc.rotate(axis=RIGHT, angle=90 * DEGREES, about_point=ORIGIN)

        beta_label = MathTex(r"\theta")
        beta_label.next_to(beta_arc, OUT)
        beta_label.fix_orientation()

        arrow = Arrow(start=ORIGIN, end=[4, 0, 0], stroke_width=3, color=GREEN, tip_shape=ArrowTriangleFilledTipSmall)
        dashed_arrow = DashedVMobject(arrow, num_dashes=20, dashed_ratio=0.5)
        animate_arrow = dashed_arrow.animate.apply_matrix(matrix=Ry).set_opacity(0.5)

        animate = axes1.animate.apply_matrix(matrix=Ry)
        animate_red = circle_red.animate.apply_matrix(matrix=Ry)
        vector_animate = vector.animate.apply_matrix(matrix=Ry)
        self.play(animate, animate_red,vector_animate, Create(beta_arc), animate_arrow, run_time=2)
        self.play(FadeIn(beta_label))
        self.wait()

        # 第一转
        alpha_arc = Arc(start_angle=0, angle=zRad, arc_center=ORIGIN)
        alpha_arc.add_tip(tip_length=0.15, tip_width=0.15)

        alpha_labels= MathTex(r"\psi")
        alpha_labels.next_to(alpha_arc)
        alpha_labels.fix_orientation()

        arrow = Arrow(start=ORIGIN, end=[4, 0, 0], stroke_width=3, color=GREEN, tip_shape=ArrowTriangleFilledTipSmall)
        dashed_arrow = DashedVMobject(arrow, num_dashes=20, dashed_ratio=0.5)
        arrow_animate=dashed_arrow.animate.apply_matrix(matrix=Rz).set_opacity(0.5)

        animate = axes1.animate.apply_matrix(matrix=Rz)
        animate_red= circle_red.animate.apply_matrix(matrix=Rz)
        vector_animate = vector.animate.apply_matrix(matrix=Rz)

        self.play(animate,animate_red,vector_animate,Create(alpha_arc),arrow_animate,run_time=2)
        self.play(FadeIn(alpha_labels))
        self.wait()

        # 最后
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(14)
# "#004000"
with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl","background_color" : "#000000"}):
    Euler_zxy_in_vector().render()
    exit(1)
