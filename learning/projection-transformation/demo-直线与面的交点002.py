from sympy import symbols, simplify


# 定义常量
a, b, c, d, xo, yo, zo = symbols('a b c d xo yo zo', constant=True)

# 定义自变量
x, y, z = symbols('x y z', real=True)

# 定义因变量

# 定义符号


# 定义方程组
x_prime = xo + (x - xo) * ((-a*xo - b*yo - c*zo - d) / (a*(x - xo) + b*(y - yo) + c*(z - zo)))
y_prime = yo + (y - yo) * ((-a*xo - b*yo - c*zo - d) / (a*(x - xo) + b*(y - yo) + c*(z - zo)))
z_prime = zo + (z - zo) * ((-a*xo - b*yo - c*zo - d) / (a*(x - xo) + b*(y - yo) + c*(z - zo)))


# x_prime, y_prime, z_prime = symbols('x_prime y_prime z_prime', function=True)

# 打印原始方程组
print("x' =", x_prime)
print("y' =", y_prime)
print("z' =", z_prime)

# 如果需要尝试简化表达式（尽管这可能不会对方程有太大改变，因为它们已经是展开形式）
x_prime_simplified = simplify(x_prime)
y_prime_simplified = simplify(y_prime)
z_prime_simplified = simplify(z_prime)

print("\n简化后的方程组：")
print("x' =", x_prime_simplified)
print("y' =", y_prime_simplified)
print("z' =", z_prime_simplified)