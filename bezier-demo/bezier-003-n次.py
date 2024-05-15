import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter, writers

fig, ax = plt.subplots()
ax.set_xlim(left=0, right=7)  # 设置 x 轴从 0 到 10
ax.set_ylim(bottom=0, top=7)  # 设置 y 轴从 0 到 5

A = (1, 1)
B = (3, 3)
C = (5, 1)
D = (3, 6)
points = [A, B, C, D]

label = 1
for point in points:
    plt.plot(*point, 'ro')
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
    point = bezier_n(points, ratio)
    print(f'ratio :{ratio} point:{point}')
    plt.plot(*point, 'bo', ms=2)


ani = FuncAnimation(fig, update, frames=ratio_list(25), interval=20)  # 每20毫秒更新一帧
ani.save("bezier_n.gif", writer=PillowWriter(fps=10))
plt.show()
