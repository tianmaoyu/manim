import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter, writers

fig, ax = plt.subplots(1,2)
# ax.set_xlim(left=-2, right=10)  # 设置 x 轴从 0 到 10
# ax.set_ylim(bottom=-2, top=10)  # 设置 y 轴从 0 到 5

A1 = (1, 1)
B1 = (3, 3)
C1 = (5, 1)

A2 = (4, 3)
B2 = (2, 4)
C2 = (3, 6)

points1 = [A1, B1, C1]
points2 = [A2, B2, C2]

label = 1
for point in points1:
    plt.plot(*point, 'bo')
    plt.text(*point, label)
    label = label + 1

label = 1
for point in points2:
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
    point1 = bezier_n(points1, ratio)
    ax[1].plot(*point1, 'bo', ms=2)
    point2 = bezier_n(points2, ratio)
    ax[1].plot(*point2, 'ro', ms=2)

    point3 = bezier_n(points3, ratio)
    ax[1].plot(*point3, 'go', ms=2)

    point4 = bezier_n(point_all, ratio)
    ax[0].plot(*point4, 'ro', ms=2)
    print(f'ratio :{ratio} point:{point}')

# 计算 点A  以点 o 为对称的 点 A‘
def compute_point(point,pointo):
    x=2*pointo[0]-point[0]
    y=2*pointo[1]-point[1]
    return (x,y);


p1=compute_point(B1,C1)
plt.plot(*p1, 'bo')

p2=compute_point(B2,A2)
plt.plot(*p2, 'ro')

points3= [C1,p1,p2,A2]

point_all=points1+[p1,p2]+points2
ax[0].plot(*zip(*point_all), 'o')

ani = FuncAnimation(fig, update, frames=ratio_list(25), interval=20)  # 每20毫秒更新一帧
ani.save("bezier_多段.gif", writer=PillowWriter(fps=10))

plt.show()