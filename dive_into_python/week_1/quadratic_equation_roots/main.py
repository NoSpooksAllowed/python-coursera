import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

d = b ** 2 - 4 * a * c

x1 = (-b + math.sqrt(d)) / (2 * a)
x2 = (-b - math.sqrt(d)) / (2 * a)

print(int(x1))
print(int(x2))
