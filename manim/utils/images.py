"""Image manipulation utilities."""

from __future__ import annotations

__all__ = [
    "get_full_raster_image_path",
    "drag_pixels",
    "invert_image",
    "change_to_rgba_array",
    "image_to_points_and_rgbas",
]

from pathlib import Path

import numpy as np
from PIL import Image

from .. import config
from ..utils.file_ops import seek_full_path_from_defaults


def get_full_raster_image_path(image_file_name: str) -> Path:
    return seek_full_path_from_defaults(
        image_file_name,
        default_dir=config.get_dir("assets_dir"),
        extensions=[".jpg", ".jpeg", ".png", ".gif", ".ico"],
    )


def get_full_vector_image_path(image_file_name: str) -> Path:
    return seek_full_path_from_defaults(
        image_file_name,
        default_dir=config.get_dir("assets_dir"),
        extensions=[".svg"],
    )


def drag_pixels(frames: list[np.array]) -> list[np.array]:
    curr = frames[0]
    new_frames = []
    for frame in frames:
        curr += (curr == 0) * np.array(frame)
        new_frames.append(np.array(curr))
    return new_frames


def invert_image(image: np.array) -> Image:
    arr = np.array(image)
    arr = (255 * np.ones(arr.shape)).astype(arr.dtype) - arr
    return Image.fromarray(arr)


def change_to_rgba_array(image, dtype="uint8"):
    """Converts an RGB array into RGBA with the alpha value opacity maxed."""
    pa = image
    if len(pa.shape) == 2:
        pa = pa.reshape(list(pa.shape) + [1])
    if pa.shape[2] == 1:
        pa = pa.repeat(3, axis=2)
    if pa.shape[2] == 3:
        alphas = 255 * np.ones(
            list(pa.shape[:2]) + [1],
            dtype=dtype,
        )
        pa = np.append(pa, alphas, axis=2)
    return pa


def image_to_points_and_rgbas(image: np.ndarray):
    """
    把图片数据 转 成 对应 的 points  和 rgbs
    """
    height, width = image.shape[:2]
    # 单个像素的长度 这是参考  OpenGLImageMobject 中图片长度得的固定值
    pixel_width = 4 / height
    y_indices, x_indices = np.mgrid[0:height, 0:width]
    points = np.zeros((height * width, 3))
    points[:, 0] = x_indices.flatten()  # x坐标
    points[:, 1] = y_indices.flatten()  # y坐标
    # 创建一个颜色数组，每个颜色是一个(r, g, b, a)四元组
    rgbas = image.reshape(-1, 4)


    # 图像反转，平移到中间
    points = points * pixel_width * [1, -1, 1] +np.array([-width / 2,height / 2,0])*pixel_width
    # 颜色的处理 / 255
    rgbas = rgbas / 255
    return points, rgbas
