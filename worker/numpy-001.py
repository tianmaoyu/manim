import numpy as np

coordinates = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 每一行代表一个坐标[x, y, z]
def transform_coordinate(item):
    return item-1
current_points= np.vectorize(transform_coordinate)(coordinates)

print(current_points)

# # 直接按行操作，同样达到上述效果
# transformed_coordinates_efficient = coordinates.copy()
# print(transformed_coordinates_efficient)
# transformed_coordinates_efficient[:, 0] += 1  # 增加每行的第一个元素（x坐标）
# transformed_coordinates_efficient[:, 1] -= 1  # 减少每行的第二个元素（y坐标）
# transformed_coordinates_efficient[:, 2] *= 2  # 将每行的第三个元素（z坐标）乘以2
#
# print(transformed_coordinates_efficient)


# 定义一个处理每行坐标的函数，比如：将每行的x坐标增加1，y坐标减去1，z坐标乘以2
def transform_row(row):
    return np.array([row[0] + 1, row[1] - 1, row[2] * 2])

# 使用numpy的apply_along_axis函数，对每一行应用变换
transformed_coordinates = np.apply_along_axis(transform_row, axis=1, arr=coordinates)

# 输出转换后的坐标
print(transformed_coordinates)