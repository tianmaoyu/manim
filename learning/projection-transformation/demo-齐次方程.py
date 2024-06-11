from sympy import symbols, Eq, solve,linear_eq_to_matrix

# 定义符号
x, y, z = symbols('x y z')
a, b, c, d, e, f, g, h, i, j, k, l = symbols('a b c d e f g h i j k l')

# 定义非齐次线性方程组
eq1 = Eq(a*x + b*y + c*z, d)
eq2 = Eq(e*x + f*y + g*z, h)
eq3 = Eq(i*x + j*y + k*z, l)

# 转换为齐次方程组
homogeneous_eq1 = Eq(eq1.lhs - eq1.rhs, 0)
homogeneous_eq2 = Eq(eq2.lhs - eq2.rhs, 0)
homogeneous_eq3 = Eq(eq3.lhs - eq3.rhs, 0)

# 打印齐次方程组
print(homogeneous_eq1)
print(homogeneous_eq2)
print(homogeneous_eq3)

A, B=linear_eq_to_matrix([homogeneous_eq1,homogeneous_eq2,homogeneous_eq3],[x,y,z])
print("A =", A)
print("B =", B)