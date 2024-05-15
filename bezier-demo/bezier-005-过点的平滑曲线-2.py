import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter, writers

fig, ax = plt.subplots(1)
ax.set_xlim(left=-2, right=10)
ax.set_ylim(bottom=-2, top=10)

A = (1, 1)
B = (3, 3)
C = (5, 2)
D = (6, 6)

points1 = [A, B, C,D]

label = 1
for point in points1:
    plt.plot(*point, 'bo')
    plt.text(*point, label)
    label = label + 1


def ratio_list(num: int) -> [float]:
    list = [i / num for i in range(0, num + 1)]
    return list


def bezier(start, end, ratio):
    # 一 次bezier
    assert ratio >= 0 or ratio <= 1
    x = (1 - ratio) * start[0] + ratio * end[0]
    y = (1 - ratio) * start[1] + ratio * end[1]
    return (x, y)


def bezier_n(points, t):
    # 递归 n 次贝塞尔曲线
    if len(points) == 1:
        return points[0]

    new_points = []
    for i in range(len(points) - 1):
        start = points[i]
        end = points[i + 1]
        point = bezier(start, end, t)
        new_points.append(point)

    return bezier_n(new_points, t)


def update(ratio):
    point1 = bezier_n(points1, ratio)
    ax.plot(*point1, 'bo', ms=1)
    point2 = bezier_n(points2, ratio)
    ax.plot(*point2, 'bo', ms=1)


# 计算两点的中点
def mid_point(point1, point2):
    x = (point1[0] + point2[0]) / 2
    y = (point1[1] + point2[1]) / 2
    return (x, y)


def draw_ling(line):
    x_values = np.linspace(-0, 6, 100)

    def linear_function(x):
        return line[0] * x + line[1]

    y_values = linear_function(x_values)
    str = f'y={line[0]}x+{line[1]}'
    plt.plot(x_values, y_values)


a = mid_point(A, B)
b = mid_point(B, C)
print(f'a={a} b={b}')
ax.plot(*a, 'ro')
ax.plot(*b, 'ro')

# y=ax+b
# 斜率 ab
k = (b[1] - a[1]) / (b[0] - a[0])
# 截距
intercept_1 = a[1] - k * a[0]
print(f'k={k}  intercept_ab={intercept_1}')
intercept_2 = B[1] - k * B[0]
print(f'intercept_2={intercept_2} ')

line1 = (k, intercept_1)
draw_ling(line1)

line2 = (k, intercept_2)
draw_ling(line2)


# 现在得到 直线方程 f(x)=0.25x+ 2.25
# 现在过 a,做直线 方程 的垂线 教一点 e
# 过b 做直线方程的垂线 交一点  f

# 得到垂线方程
def get_vertical_line(line, point):
    k_temp = -1 / line[0];
    intercept_temp = point[1] - k_temp * point[0]
    return (k_temp, intercept_temp)


line3 = get_vertical_line(line1, a)
print(line3)
draw_ling(line3)


def get_intersection_point(line1, line2):
    x = (line1[1] - line2[1]) / (line2[0] - line1[0])
    y = line2[0] * x + line2[1]
    return (x, y)


# 计算 点A  以点 o 为对称的 点 A‘
def compute_point(point, pointo):
    x = 2 * pointo[0] - point[0]
    y = 2 * pointo[1] - point[1]
    return (x, y);


f = get_intersection_point(line3, line2)
ax.plot(*f, 'go')

line4 = get_vertical_line(line1, b)
draw_ling(line4)
e = get_intersection_point(line4, line2)
ax.plot(*e, 'go')

points1 = [A, f, B]
points2 = [B, e, C]
ani = FuncAnimation(fig, update, frames=ratio_list(25), interval=20)  # 每20毫秒更新一帧
ani.save("bezier_过点.gif", writer=PillowWriter(fps=10))

plt.show()
