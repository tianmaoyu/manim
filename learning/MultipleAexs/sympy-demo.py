from sympy import Matrix, symbols,latex
# 定义符号变量
x, y, z = symbols('x y z')
# 定义矩阵
matrix = Matrix([
    [1, 0, 0,-x],
    [0, 1, 0,-y],
    [0, 0, 1,-z],
    [0, 0, 0,1]
])

# 计算矩阵的逆
inverse_matrix = matrix.inv()
latex(inverse_matrix)
inverse_matrix = inverse_matrix.inv()
latex(inverse_matrix)
