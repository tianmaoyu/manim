import numpy as np
import matplotlib.pyplot as plt

from sympy import symbols, Function,expand,collect



arr=np.array([[3,4,2],[2,3,1]])
arr2=np.array([[8,6,2],[3,4,2]])


points=np.append(arr,arr2,axis=0)
new_points=[]
for point in points:
    z=point[2]
    new_point = []
    new_point.append(point[0]/ z)
    new_point.append(point[1]/ z)
    new_point.append(1)
    new_points.append(new_point)

print(all)
# test=all[:, 2]
# all=all.T/ all[:,2]

# 定义符号
A, B, C, x, y = symbols('A B C x y')



# # 定义方程
# eq1 =  ((2 * B * (A * x + B * y + C)) / (A ** 2 + B ** 2)) - x
# eq2 = ((2 * A * (A * x + B * y + C)) / (A ** 2 + B ** 2)) - y
#
# # 收集并简化同类项
# eq1_simplified = collect(eq1, x)
# eq2_simplified = collect(eq2, y)
#
# print(eq1_simplified)
# print(eq2_simplified)
# 定义符号


eq1=((2*B*(A*x+B*y+C))/(A**2+B**2)) - x
str=expand(eq1)

x_indices, y_indices = np.indices((255, 255))
points = np.dstack([x_indices, y_indices, np.zeros((255, 255))]).reshape(-1, 3)
# 创建一个 256x256 的灰度图像
image = np.zeros((256, 256), np.uint8)

# 用随机数填充图像
image = np.random.randint(0, 256, (256, 256))

# 使用 matplotlib 库显示图像
plt.imshow(image, cmap='gray')
plt.show()