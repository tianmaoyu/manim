from manim import *
from manim.mobject.geometry.tips import ArrowTriangleFilledTipSmall

from manim.mobject.opengl.opengl_something import OpenGLCone, OpenGLLine3D, OpenGLArrow3D
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np


class VariableExample(ThreeDScene):

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
                          axis_config=axis_config, )

        axes.add(axes.get_axis_labels())
        axes.set_color(BLUE_C)
        axes.shift(ORIGIN - axes.c2p(0, 0, 0))
        self.play(Create(axes))

        point_label = MathTex(r"P(2,2,2)").to_corner(UL)
        self.add_fixed_in_frame_mobjects(point_label)

        num_x = Integer(number=1)
        num_y = Integer(number=1)
        num_z = Integer(number=1)

        # self.add(num_x,num_y.next_to(num_x),num_z.next_to(num_y))
        # group=OpenGLPMobject(num_x,num_y,num_z).arrange(direction=RIGHT)
        # self.add(group)
        tracker_x = ValueTracker(0)
        tracker_y = ValueTracker(0)
        tracker_z = ValueTracker(0)
        num_x.add_updater(lambda m: m.set_value(tracker_x.get_value()))
        num_y.add_updater(lambda m: m.set_value(tracker_y.get_value()))
        num_z.add_updater(lambda m: m.set_value(tracker_z.get_value()))
        animate_x= tracker_x.animate.set_value(10)
        animate_y = tracker_y.animate.set_value(10)
        animate_z = tracker_z.animate.set_value(10)
        self.play(animate_x,animate_y,animate_z)






# "#004000"
with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl","background_color" : "#000000"}):
    VariableExample().render()
    exit(1)