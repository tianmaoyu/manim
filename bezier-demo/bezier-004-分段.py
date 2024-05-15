import numpy as np
import matplotlib.pyplot as plt

# 定义一个函数，用于计算三阶贝塞尔曲线上的点
def bezier_curve(t, points):
    if len(points)<4 :
        return
    P0, P1, P2, P3 = points
    return (1 - t) ** 3 * P0 + 3 * (1 - t) ** 2 * t * P1 + 3 * (1 - t) * t ** 2 * P2 + t ** 3 * P3


A = [1, 1]
B = [3, 3]
C = [5, 1]
D = [3, 6]
E =[ 2,4]
F =[5,4]
G =[4,3]
control_points =  np.array([A, B, C, D,E,F,G ])

# # 假设我们有一系列n个控制点，我们将它们分段为三阶贝塞尔曲线
# control_points = np.array([
#     [x0, y0], [x1, y1], [x2, y2], ..., [xn-2, yn-2], [xn-1, yn-1], [xn, yn]  # 这里应填充实际坐标
# ])
def ratio_list(num: int) -> [float]:
    list = [i / num for i in range(0, num + 1)]
    return list
# 分段处理
segments = [control_points[i:i+4] for i in range(0, len(control_points), 3)]

# 计算每个分段上的一系列点，并合并成一个数组
all_curve_points = []
for segment in segments:
    t_values = ratio_list(20)  # 根据需要调整采样点的数量

    curve_segment = [bezier_curve(ti, segment) for ti in t_values]
    all_curve_points.extend(curve_segment)

# 将所有曲线点绘制成一条连续曲线
curve_x = [p[0] for p in all_curve_points if p is not None]
curve_y = [p[1] for p in all_curve_points if p is not None]

fig, ax = plt.subplots()
ax.set_xlim(left=0, right=7)  # 设置 x 轴从 0 到 10
ax.set_ylim(bottom=0, top=7)  # 设置 y 轴从 0 到 5


plt.plot(curve_x, curve_y, 'r-',ms=2)
plt.gca().autoscale_view()  # 自动调整视图范围以包含所有数据
plt.grid(True)
plt.show()