import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter, writers

fig, ax = plt.subplots()
ax.set_xlim(left=0, right=4)  # 设置 x 轴从 0 到 10
ax.set_ylim(bottom=0, top=4)   # 设置 y 轴从 0 到 5

p0 = (1, 1)
p1 = (3, 3)

plt.plot(*p0,'ro')
plt.plot(*p1,'ro')

def divide(num: int) -> [float]:
    list = [i / num for i in range(0, num + 1)]
    return list


def bezier_1(point1, point2, t):
    # 一 次bezier
    assert t >= 0 or t <= 1
    x = (1 - t) * point1[0] + t * point2[0]
    y = (1 - t) * point1[1] + t * point2[1]
    return (x, y)


list = divide(50)
print(len(list))
print(list)

def update(item):
    point = bezier_1(p0, p1, item)
    plt.plot(*point, 'bo',ms=2)

ani = FuncAnimation(fig, update, frames=list, interval=20)  # 每20毫秒更新一帧
ani.save("bezier_1.gif", writer=PillowWriter(fps=10))
# Writer = writers['ffmpeg']
# writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=1800)
# ani.save('animation.mp4', writer=writer)
plt.show()
