from sympy import *
from sympy.geometry import Ray, Plane

# 定义射线和平面
# 射线定义为起点和方向向量，例如射线从点(1, 2, 3)出发，指向向量(1, 9, 4)
ray = Line(Point3D(1, 2, 3), Point3D(2, 11, 7) - Point3D(1, 2, 3))

# 平面定义为一点和法向量，例如过点(0, 0, 0)，法向量为(1, 1, 1)
plane = Plane(Point3D(0, 0, 0), normal_vector=(1, 1, 1))

# 计算交点
intersection_point = ray.intersection(plane)

print(intersection_point)