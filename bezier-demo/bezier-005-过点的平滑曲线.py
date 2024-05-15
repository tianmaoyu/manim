import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter, writers

fig, ax = plt.subplots(1, 2)
ax[1].set_xlim(left=-2, right=6)
ax[1].set_ylim(bottom=-2, top=6)
ax[0].set_xlim(left=-2, right=6)
ax[0].set_ylim(bottom=-2, top=6)

A = (1, 1)
B = (3, 3)
C = (5, 2)
D = (4, 3)
E = (2, 4)
F = (3, 6)

points1 = [A, B, C]

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
    ax[1].plot(*point1, 'bo', ms=2)

#计算两点的中点
def mid_point(point1, point2):
    x = (point1[0] + point2[0]) / 2
    y = (point1[1] + point2[1]) / 2
    return (x, y)


a=mid_point(A,B)
b=mid_point(B,C)
print(f'a={a} b={b}')
ax[1].plot(*a, 'ro', ms=2)
ax[1].plot(*b, 'ro', ms=2)

# y=ax+b
# 斜率 ab
k=(b[1]-a[1])/(b[0]-a[0])
# 截距
intercept_1 = a[1] - k * a[0]
print(f'k={k}  intercept_ab={intercept_1}')
intercept_2 = B[1] - k * B[0]
print(f'intercept_2={intercept_2} ')

line1=(k,intercept_1)
line2=(k,intercept_2)
#现在得到 直线方程 f(x)=0.25x+ 2.25
#现在过 a,做直线 方程 的垂线 教一点 e
#过b 做直线方程的垂线 交一点  f

#得到垂线方程
def get_vertical_line(k,intercept,point):
    k_temp=- 1/k;
    intercept_temp=point[1]-k_temp*point[0]
    return (k_temp,intercept_temp)


k3,intercept3=get_vertical_line(k,intercept_2,a)
line3=(k3,intercept3)

def get_intersection_point(line1,line2):
    x=(line1[1]-line2[1])/(line2[0]-line1[0])
    y=line2[0]*x+line2[1]
    return (x,y)

# 计算 点A  以点 o 为对称的 点 A‘
def compute_point(point, pointo):
    x = 2 * pointo[0] - point[0]
    y = 2 * pointo[1] - point[1]
    return (x, y);

f=get_intersection_point(line3,line2)
print(f)
ax[1].plot(*f, 'go')

# ani = FuncAnimation(fig, update, frames=ratio_list(25), interval=20)  # 每20毫秒更新一帧
# ani.save("bezier_多段——3.gif", writer=PillowWriter(fps=10))

plt.show()
