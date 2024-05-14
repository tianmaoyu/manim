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
    config["output_file"] = "output.mp4"

    config["disable_caching"] = True

    def __init__(self, image_paths: [str], **kwargs):
        super().__init__(**kwargs)
        self.image_paths = image_paths

    def construct(self):
        # 135倍  manim 默认是 长 14 高 8  如果换成像素 以单位 对应 135个像素
        self.camera.frame_height = 3000 / 135
        self.camera.frame_width = 4000 / 135


        images = [ImageMobject(path) for path in self.image_paths]

        def update_func(mob: ImageMobject, alpha: float):
            mob.set_opacity(alpha)

        for index, image in enumerate(images):
            self.play(UpdateFromAlphaFunc(image, update_func), run_time=1, rate_func=linear)

        self.wait()


from PIL import Image

# "renderer": "opengl"
with tempconfig({"preview": True, "disable_caching": True}):
    directory = "D:/Users/15590/PycharmProjects/fastApi-demo/配置image"
    image_paths = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        image_paths.append(file_path)
    config["video_dir"] = "./temp/video2"

    ImageToVideo(image_paths=image_paths).render()
    exit(1)
