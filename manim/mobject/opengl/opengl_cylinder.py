from typing import Sequence

from manim import *
from manim.mobject.opengl.opengl_surface import OpenGLSurface
import numpy as np

from manim.typing import Point3D


class OpenGLCylinder(OpenGLSurface):
    """A cylinder, defined by its height, radius and direction,

    Parameters
    ----------
    radius
        The radius of the cylinder.
    height
        The height of the cylinder.
    direction
        The direction of the central axis of the cylinder.
    v_range
        The height along the height axis (given by direction) to start and end on.
    show_ends
        Whether to show the end caps or not.
    resolution
        The number of samples taken of the :class:`Cylinder`. A tuple can be used
        to define different resolutions for ``u`` and ``v`` respectively.

    Examples
    --------
    .. manim:: ExampleCylinder
        :save_last_frame:

        class ExampleCylinder(ThreeDScene):
            def construct(self):
                axes = ThreeDAxes()
                cylinder = Cylinder(radius=2, height=3)
                self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
                self.add(axes, cylinder)
    """

    def __init__(
        self,
        radius: float = 1,
        height: float = 2,
        direction: np.ndarray = Z_AXIS,
        v_range: Sequence[float] = [0, TAU],
        show_ends: bool = True,
        resolution: Sequence[int] = (101, 51),
        **kwargs,
    ) -> None:
        self._height = height
        self.radius = radius

        super().__init__(
            self.func,
            resolution=resolution,
            u_range=[-self._height / 2, self._height / 2],
            v_range=v_range,
            **kwargs,
        )
        if show_ends:
            self.add_bases()
        self._current_phi = 0
        self._current_theta = 0
        self.set_direction(direction)

    def func(self, u: float, v: float) -> np.ndarray:
        """Converts from cylindrical coordinates to cartesian.

        Parameters
        ----------
        u
            The height.
        v
            The azimuthal angle.

        Returns
        -------
        :class:`numpy.ndarray`
            Points defining the :class:`Cylinder`.
        """
        height = u
        phi = v
        r = self.radius
        return np.array([r * np.cos(phi), r * np.sin(phi), height])

    def add_bases(self) -> None:
        """Adds the end caps of the cylinder."""
        if config.renderer == RendererType.OPENGL:
            color = self.color
            opacity = self.opacity
        elif config.renderer == RendererType.CAIRO:
            color = self.fill_color
            opacity = self.fill_opacity

        self.base_top = Circle(
            radius=self.radius,
            color=color,
            fill_opacity=opacity,
            shade_in_3d=True,
            stroke_width=0,
        )
        self.base_top.shift(self.u_range[1] * IN)
        self.base_bottom = Circle(
            radius=self.radius,
            color=color,
            fill_opacity=opacity,
            shade_in_3d=True,
            stroke_width=0,
        )
        self.base_bottom.shift(self.u_range[0] * IN)
        self.add(self.base_top, self.base_bottom)

    def _rotate_to_direction(self) -> None:
        x, y, z = self.direction

        r = np.sqrt(x**2 + y**2 + z**2)
        if r > 0:
            theta = np.arccos(z / r)
        else:
            theta = 0

        if x == 0:
            if y == 0:  # along the z axis
                phi = 0
            else:  # along the x axis
                phi = np.arctan(np.inf)
                if y < 0:
                    phi += PI
        else:
            phi = np.arctan(y / x)
        if x < 0:
            phi += PI

        # undo old rotation (in reverse direction)
        self.rotate(-self._current_phi, Z_AXIS, about_point=ORIGIN)
        self.rotate(-self._current_theta, Y_AXIS, about_point=ORIGIN)

        # do new rotation
        self.rotate(theta, Y_AXIS, about_point=ORIGIN)
        self.rotate(phi, Z_AXIS, about_point=ORIGIN)

        # store new values
        self._current_theta = theta
        self._current_phi = phi

    def set_direction(self, direction: np.ndarray) -> None:
        """Sets the direction of the central axis of the :class:`Cylinder`.

        Parameters
        ----------
        direction : :class:`numpy.array`
            The direction of the central axis of the :class:`Cylinder`.
        """
        # if get_norm(direction) is get_norm(self.direction):
        #     pass
        self.direction = direction
        self._rotate_to_direction()

    def get_direction(self) -> np.ndarray:
        """Returns the direction of the central axis of the :class:`Cylinder`.

        Returns
        -------
        direction : :class:`numpy.array`
            The direction of the central axis of the :class:`Cylinder`.
        """
        return self.direction