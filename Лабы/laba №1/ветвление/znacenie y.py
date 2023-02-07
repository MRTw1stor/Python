from math import sin, cos, log
z = float(input("Введите значение z: "))
if z >= 0:
    x = 2*z+1
else:
    x = log(z**2-z)
y = (sin(x)**2)+(cos(x**3)**5)+(log(x**(2/5)))
print("y=","%.3f"%y)