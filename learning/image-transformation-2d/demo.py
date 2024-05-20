import numpy as np
import matplotlib.pyplot as plt



x_indices, y_indices = np.indices((255, 255))
points = np.dstack([x_indices, y_indices, np.zeros((255, 255))]).reshape(-1, 3)
# 创建一个 256x256 的灰度图像
image = np.zeros((256, 256), np.uint8)

# 用随机数填充图像
image = np.random.randint(0, 256, (256, 256))

# 使用 matplotlib 库显示图像
plt.imshow(image, cmap='gray')
plt.show()