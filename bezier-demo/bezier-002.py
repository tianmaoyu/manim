import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter, writers

fig, ax = plt.subplots()
ax.set_xlim(left=0, right=5)  # 设置 x 轴从 0 到 10
ax.set_ylim(bottom=0, top=5)   # 设置 y 轴从 0 到 5

A = (1, 1)
B = (3, 3)
C = (5, 1)

plt.plot(*A, 'ro')
plt.text(*A, "A")
plt.plot(*B, 'ro')
plt.text(*B, "B")
plt.plot(*C, 'ro')
plt.text(*C, "C")

def divide(num: int) -> [float]:
    list = [i / num for i in range(0, num + 1)]
    return list


def bezier_1(point1, point2, t):
    # 一 次bezier
    assert t >= 0 or t <= 1
    x = (1 - t) * point1[0] + t * point2[0]
    y = (1 - t) * point1[1] + t * point2[1]
    return (x, y)


def update(t):
    D = bezier_1(A, B, t)
    E = bezier_1(B, C, t)
    F = bezier_1(D, E, t)
    plt.plot(*F, 'bo',ms=2)

ani = FuncAnimation(fig, update, frames=divide(25), interval=20)  # 每20毫秒更新一帧
ani.save("bezier_2.gif", writer=PillowWriter(fps=10))
plt.show()
