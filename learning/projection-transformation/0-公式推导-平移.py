


from sympy import symbols, Matrix

# 定义符号变量
x, y, z, x_o, y_o, z_o, a, b, c, d = symbols('x y z x_o y_o z_o a b c d')

# 定义矩阵
symbols_matrix = Matrix([
    [-d, 0, 0, 0],
    [0, -d, 0, 0],
    [0, 0, -d, 0],
    [a, b, c,  0]
])

transformation_matrix1 = Matrix([
    [1, 0, 0, -x_o],
    [0, 1, 0, -y_o],
    [0, 0, 1, -z_o],
    [0, 0, 0,  1]
])

transformation_matrix2 = Matrix([
    [1, 0, 0, x_o],
    [0, 1, 0, y_o],
    [0, 0, 1, z_o],
    [0, 0, 0,  1]
])


result_matrix= transformation_matrix1 * symbols_matrix*transformation_matrix2


symbols_p = Matrix([x, y, z, 1])

symbols_w = a*x - a*x_o + b*y - b*y_o + c*z - c*z_o

symbols_result = (1 / symbols_w) * symbols_matrix * symbols_p
# O： (1, 1, 2)
# 平面方程： 1x+2y+2z-2=0
# 点P (1,1,0)

matrix1= symbols_matrix.subs({a:1,b:2,c:2,d:-2,x_o:1,y_o:1,z_o:2,x:1,y:1,z:0})
print(matrix1)

point1= symbols_result.subs({a:1,b:2,c:2,d:-2,x_o:1,y_o:1,z_o:2,x:1,y:1,z:0})
print(point1)



