from typing import Sequence

from manim import *
from manim.mobject.opengl.opengl_surface import OpenGLSurface
import numpy as np

from manim.typing import Point3D


class OpenGLSphere(OpenGLSurface):
    """A three-dimensional sphere.

    Parameters
    ----------
    center
        Center of the :class:`Sphere`.
    radius
        The radius of the :class:`Sphere`.
    resolution
        The number of samples taken of the :class:`Sphere`. A tuple can be used
        to define different resolutions for ``u`` and ``v`` respectively.
    u_range
        The range of the ``u`` variable: ``(u_min, u_max)``.
    v_range
        The range of the ``v`` variable: ``(v_min, v_max)``.

    Examples
    --------

    .. manim:: ExampleSphere
        :save_last_frame:

        class ExampleSphere(ThreeDScene):
            def construct(self):
                self.set_camera_orientation(phi=PI / 6, theta=PI / 6)
                sphere1 = Sphere(
                    center=(3, 0, 0),
                    radius=1,
                    resolution=(20, 20),
                    u_range=[0.001, PI - 0.001],
                    v_range=[0, TAU]
                )
                sphere1.set_color(RED)
                self.add(sphere1)
                sphere2 = Sphere(center=(-1, -3, 0), radius=2, resolution=(18, 18))
                sphere2.set_color(GREEN)
                self.add(sphere2)
                sphere3 = Sphere(center=(-1, 2, 0), radius=2, resolution=(16, 16))
                sphere3.set_color(BLUE)
                self.add(sphere3)
    """

    def __init__(
            self,
            center: Point3D = ORIGIN,
            radius: float = 1,
            resolution: Sequence[int] | None = None,
            u_range: Sequence[float] = (0, TAU),
            v_range: Sequence[float] = (0, PI),
            **kwargs,
    ) -> None:
        default_resolution = (101, 51)
        resolution = resolution if resolution is not None else default_resolution
        self.radius = radius

        super().__init__(
            self.func,
            resolution=resolution,
            u_range=u_range,
            v_range=v_range,
            **kwargs,
        )

        self.shift(center)

    def func(self, u: float, v: float) -> np.ndarray:
        """The z values defining the :class:`Sphere` being plotted.

        Returns
        -------
        :class:`numpy.array`
            The z values defining the :class:`Sphere`.
        """
        return self.radius * np.array(
            [np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), -np.cos(v)],
        )
