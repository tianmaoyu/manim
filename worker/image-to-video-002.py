import datetime
import glob
import os
import random
import time
import typing

from manim import *
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np

from manim.typing import Image


class ImageToVideo(ThreeDScene):

    def construct(self):
        def update_func(mob: ImagePixelMobject, alpha: float):
            mob.rgbas[:,3]=alpha/2
            # mob.set_opacity(alpha)

        image = ImagePixelMobject("360-2048-1024.jpg")
        self.add(image.to_center())
        self.play(UpdateFromAlphaFunc(image, update_func), run_time=2, rate_func=linear)
        #
        # image2 = ImagePixelMobject("world-daytime.jpg")
        # self.add(image2.to_center())
        # self.play(UpdateFromAlphaFunc(image2, update_func), run_time=1, rate_func=linear)
        self.wait()


from PIL import Image

# "renderer": "opengl"
with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    ImageToVideo().render()
    exit(1)
