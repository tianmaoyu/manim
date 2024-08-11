from typing import Sequence

from manim import *
from manim.mobject.opengl.opengl_mobject import OpenGLMobject
from manim.mobject.opengl.opengl_shpere import OpenGLSphere
from manim.mobject.opengl.opengl_surface import OpenGLSurface
import numpy as np

from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVGroup
from manim.typing import Point3D, Vector3D


class OpenGLCone(OpenGLSurface):
    """A circular cone.
    Can be defined using 2 parameters: its height, and its base radius.
    The polar angle, theta, can be calculated using arctan(base_radius /
    height) The spherical radius, r, is calculated using the pythagorean
    theorem.

    Parameters
    ----------
    base_radius
        The base radius from which the cone tapers.
    height
        The height measured from the plane formed by the base_radius to
        the apex of the cone.
    direction
        The direction of the apex.
    show_base
        Whether to show the base plane or not.
    v_range
        The azimuthal angle to start and end at.
    u_min
        The radius at the apex.
    checkerboard_colors
        Show checkerboard grid texture on the cone.

    Examples
    --------
    .. manim:: ExampleCone
        :save_last_frame:

        class ExampleCone(ThreeDScene):
            def construct(self):
                axes = ThreeDAxes()
                cone = Cone(direction=X_AXIS+Y_AXIS+2*Z_AXIS, resolution=8)
                self.set_camera_orientation(phi=5*PI/11, theta=PI/9)
                self.add(axes, cone)
    """

    def __init__(
        self,
        base_radius: float = 1,
        height: float = 1,
        direction: np.ndarray = Z_AXIS,
        show_base: bool = False,
        v_range: Sequence[float] = [0, TAU],
        u_min: float = 0,
        checkerboard_colors: bool = False,
        **kwargs,
    ) -> None:
        self.direction = direction
        self.theta = PI - np.arctan(base_radius / height)

        super().__init__(
            self.func,
            v_range=v_range,
            u_range=[u_min, np.sqrt(base_radius**2 + height**2)],
            checkerboard_colors=checkerboard_colors,
            **kwargs,
        )
        # used for rotations
        self._current_theta = 0
        self._current_phi = 0

        if show_base:
            self.base_circle = Circle(
                radius=base_radius,
                color=self.fill_color,
                fill_opacity=self.fill_opacity,
                stroke_width=0,
            )
            self.base_circle.shift(height * IN)
            self.add(self.base_circle)

        self._rotate_to_direction()

    def func(self, u: float, v: float) -> np.ndarray:
        """Converts from spherical coordinates to cartesian.

        Parameters
        ----------
        u
            The radius.
        v
            The azimuthal angle.

        Returns
        -------
        :class:`numpy.array`
            Points defining the :class:`Cone`.
        """
        r = u
        phi = v
        return np.array(
            [
                r * np.sin(self.theta) * np.cos(phi),
                r * np.sin(self.theta) * np.sin(phi),
                r * np.cos(self.theta),
            ],
        )

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
            else:
                phi = np.arctan(np.inf)
                if y < 0:
                    phi += PI
        else:
            phi = np.arctan(y / x)
        if x < 0:
            phi += PI

        # Undo old rotation (in reverse order)
        self.rotate(-self._current_phi, Z_AXIS, about_point=ORIGIN)
        self.rotate(-self._current_theta, Y_AXIS, about_point=ORIGIN)

        # Do new rotation
        self.rotate(theta, Y_AXIS, about_point=ORIGIN)
        self.rotate(phi, Z_AXIS, about_point=ORIGIN)

        # Store values
        self._current_theta = theta
        self._current_phi = phi

    def set_direction(self, direction: np.ndarray) -> None:
        """Changes the direction of the apex of the :class:`Cone`.

        Parameters
        ----------
        direction
            The direction of the apex.
        """
        self.direction = direction
        self._rotate_to_direction()

    def get_direction(self) -> np.ndarray:
        """Returns the current direction of the apex of the :class:`Cone`.

        Returns
        -------
        direction : :class:`numpy.array`
            The direction of the apex.
        """
        return self.direction


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
        resolution: Sequence[int] = (24, 24),
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


class OpenGLLine3D(OpenGLCylinder):
    """A cylindrical line, for use in ThreeDScene.

    Parameters
    ----------
    start
        The start point of the line.
    end
        The end point of the line.
    thickness
        The thickness of the line.
    color
        The color of the line.

    Examples
    --------
    .. manim:: ExampleLine3D
        :save_last_frame:

        class ExampleLine3D(ThreeDScene):
            def construct(self):
                axes = ThreeDAxes()
                line = Line3D(start=np.array([0, 0, 0]), end=np.array([2, 2, 2]))
                self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
                self.add(axes, line)
    """

    def __init__(
        self,
        start: np.ndarray = LEFT,
        end: np.ndarray = RIGHT,
        thickness: float = 0.02,
        color: ParsableManimColor | None = None,
        **kwargs,
    ):
        self.thickness = thickness
        self.set_start_and_end_attrs(start, end, **kwargs)
        if color is not None:
            self.set_color(color)

    def set_start_and_end_attrs(
        self, start: np.ndarray, end: np.ndarray, **kwargs
    ) -> None:
        """Sets the start and end points of the line.

        If either ``start`` or ``end`` are :class:`Mobjects <.Mobject>`,
        this gives their centers.

        Parameters
        ----------
        start
            Starting point or :class:`Mobject`.
        end
            Ending point or :class:`Mobject`.
        """
        rough_start = self.pointify(start)
        rough_end = self.pointify(end)
        self.vect = rough_end - rough_start
        self.length = np.linalg.norm(self.vect)
        self.direction = normalize(self.vect)
        # Now that we know the direction between them,
        # we can the appropriate boundary point from
        # start and end, if they're mobjects
        self.start = self.pointify(start, self.direction)
        self.end = self.pointify(end, -self.direction)
        super().__init__(
            height=np.linalg.norm(self.vect),
            radius=self.thickness,
            direction=self.direction,
            **kwargs,
        )
        self.shift((self.start + self.end) / 2)

    def pointify(
        self,
        mob_or_point: Mobject | Point3D,
        direction: Vector3D = None,
    ) -> np.ndarray:
        """Gets a point representing the center of the :class:`Mobjects <.Mobject>`.

        Parameters
        ----------
        mob_or_point
            :class:`Mobjects <.Mobject>` or point whose center should be returned.
        direction
            If an edge of a :class:`Mobjects <.Mobject>` should be returned, the direction of the edge.

        Returns
        -------
        :class:`numpy.array`
            Center of the :class:`Mobjects <.Mobject>` or point, or edge if direction is given.
        """
        if isinstance(mob_or_point, (Mobject, OpenGLMobject)):
            mob = mob_or_point
            if direction is None:
                return mob.get_center()
            else:
                return mob.get_boundary_point(direction)
        return np.array(mob_or_point)

    def get_start(self) -> np.ndarray:
        """Returns the starting point of the :class:`Line3D`.

        Returns
        -------
        start : :class:`numpy.array`
            Starting point of the :class:`Line3D`.
        """
        return self.start

    def get_end(self) -> np.ndarray:
        """Returns the ending point of the :class:`Line3D`.

        Returns
        -------
        end : :class:`numpy.array`
            Ending point of the :class:`Line3D`.
        """
        return self.end

    @classmethod
    def parallel_to(
        cls,
        line: Line3D,
        point: Vector3D = ORIGIN,
        length: float = 5,
        **kwargs,
    ) -> Line3D:
        """Returns a line parallel to another line going through
        a given point.

        Parameters
        ----------
        line
            The line to be parallel to.
        point
            The point to pass through.
        length
            Length of the parallel line.
        kwargs
            Additional parameters to be passed to the class.

        Returns
        -------
        :class:`Line3D`
            Line parallel to ``line``.

        Examples
        --------
        .. manim:: ParallelLineExample
            :save_last_frame:

            class ParallelLineExample(ThreeDScene):
                def construct(self):
                    self.set_camera_orientation(PI / 3, -PI / 4)
                    ax = ThreeDAxes((-5, 5), (-5, 5), (-5, 5), 10, 10, 10)
                    line1 = Line3D(RIGHT * 2, UP + OUT, color=RED)
                    line2 = Line3D.parallel_to(line1, color=YELLOW)
                    self.add(ax, line1, line2)
        """
        point = np.array(point)
        vect = normalize(line.vect)
        return cls(
            point + vect * length / 2,
            point - vect * length / 2,
            **kwargs,
        )

    @classmethod
    def perpendicular_to(
        cls,
        line: Line3D,
        point: Vector3D = ORIGIN,
        length: float = 5,
        **kwargs,
    ) -> Line3D:
        """Returns a line perpendicular to another line going through
        a given point.

        Parameters
        ----------
        line
            The line to be perpendicular to.
        point
            The point to pass through.
        length
            Length of the perpendicular line.
        kwargs
            Additional parameters to be passed to the class.

        Returns
        -------
        :class:`Line3D`
            Line perpendicular to ``line``.

        Examples
        --------
        .. manim:: PerpLineExample
            :save_last_frame:

            class PerpLineExample(ThreeDScene):
                def construct(self):
                    self.set_camera_orientation(PI / 3, -PI / 4)
                    ax = ThreeDAxes((-5, 5), (-5, 5), (-5, 5), 10, 10, 10)
                    line1 = Line3D(RIGHT * 2, UP + OUT, color=RED)
                    line2 = Line3D.perpendicular_to(line1, color=BLUE)
                    self.add(ax, line1, line2)
        """
        point = np.array(point)

        norm = np.cross(line.vect, point - line.start)
        if all(np.linalg.norm(norm) == np.zeros(3)):
            raise ValueError("Could not find the perpendicular.")

        start, end = perpendicular_bisector([line.start, line.end], norm)
        vect = normalize(end - start)
        return cls(
            point + vect * length / 2,
            point - vect * length / 2,
            **kwargs,
        )


class OpenGLArrow3D(OpenGLLine3D):
    """An arrow made out of a cylindrical line and a conical tip.

    Parameters
    ----------
    start
        The start position of the arrow.
    end
        The end position of the arrow.
    thickness
        The thickness of the arrow.
    height
        The height of the conical tip.
    base_radius
        The base radius of the conical tip.
    color
        The color of the arrow.

    Examples
    --------
    .. manim:: ExampleArrow3D
        :save_last_frame:

        class ExampleArrow3D(ThreeDScene):
            def construct(self):
                axes = ThreeDAxes()
                arrow = Arrow3D(
                    start=np.array([0, 0, 0]),
                    end=np.array([2, 2, 2]),
                    resolution=8
                )
                self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
                self.add(axes, arrow)
    """

    def __init__(
        self,
        start: np.ndarray = LEFT,
        end: np.ndarray = RIGHT,
        thickness: float = 0.02,
        height: float = 0.3,
        base_radius: float = 0.08,
        color: ParsableManimColor = WHITE,
        **kwargs,
    ) -> None:
        super().__init__(
            start=start, end=end, thickness=thickness, color=color, **kwargs
        )

        self.length = np.linalg.norm(self.vect)
        self.set_start_and_end_attrs(
            self.start,
            self.end - height * self.direction,
            **kwargs,
        )

        self.cone = OpenGLCone(
            direction=self.direction, base_radius=base_radius, height=height, **kwargs
        )
        self.cone.shift(end)
        self.add(self.cone)
        self.set_color(color)

class OpenGLDot3D(OpenGLSphere):
    """A spherical dot.

    Parameters
    ----------
    point
        The location of the dot.
    radius
        The radius of the dot.
    color
        The color of the :class:`Dot3D`.
    resolution
        The number of samples taken of the :class:`Dot3D`. A tuple can be
        used to define different resolutions for ``u`` and ``v`` respectively.

    Examples
    --------

    .. manim:: Dot3DExample
        :save_last_frame:

        class Dot3DExample(ThreeDScene):
            def construct(self):
                self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

                axes = ThreeDAxes()
                dot_1 = Dot3D(point=axes.coords_to_point(0, 0, 1), color=RED)
                dot_2 = Dot3D(point=axes.coords_to_point(2, 0, 0), radius=0.1, color=BLUE)
                dot_3 = Dot3D(point=[0, 0, 0], radius=0.1, color=ORANGE)
                self.add(axes, dot_1, dot_2,dot_3)
    """

    def __init__(
        self,
        point: list | np.ndarray = ORIGIN,
        radius: float = DEFAULT_DOT_RADIUS,
        color: ParsableManimColor = WHITE,
        resolution: tuple[int, int] = (8, 8),
        **kwargs,
    ) -> None:
        super().__init__(center=point, radius=radius, resolution=resolution, **kwargs)
        self.set_color(color)



class OpenGLCube(OpenGLVGroup):
    """A three-dimensional cube.

    Parameters
    ----------
    side_length
        Length of each side of the :class:`Cube`.
    fill_opacity
        The opacity of the :class:`Cube`, from 0 being fully transparent to 1 being
        fully opaque. Defaults to 0.75.
    fill_color
        The color of the :class:`Cube`.
    stroke_width
        The width of the stroke surrounding each face of the :class:`Cube`.

    Examples
    --------

    .. manim:: CubeExample
        :save_last_frame:

        class CubeExample(ThreeDScene):
            def construct(self):
                self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

                axes = ThreeDAxes()
                cube = Cube(side_length=3, fill_opacity=0.7, fill_color=BLUE)
                self.add(cube)
    """

    def __init__(
        self,
        side_length: float = 2,
        fill_opacity: float = 0.75,
        fill_color: ParsableManimColor = BLUE,
        stroke_width: float = 0,
        **kwargs,
    ) -> None:
        self.side_length = side_length
        super().__init__(
            fill_color=fill_color,
            fill_opacity=fill_opacity,
            stroke_width=stroke_width,
            **kwargs,
        )

    def generate_points(self) -> None:
        """Creates the sides of the :class:`Cube`."""
        for vect in IN, OUT, LEFT, RIGHT, UP, DOWN:
            face = Square(
                side_length=self.side_length,
                shade_in_3d=True,
            )
            face.flip()
            face.shift(self.side_length * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))

            self.add(face)

    init_points = generate_points
