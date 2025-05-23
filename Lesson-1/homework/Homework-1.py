# Homework based on the covered material

# 1) Perimeter and area of a square
side = float(input("Enter the side length of the square: "))
perimeter = 4 * side
area = side ** 2
print("Square perimeter =", perimeter)
print("Square area =", area, "\n")

# 2) Circumference of a circle given its diameter
diameter = float(input("Enter the diameter of the circle: "))
pi = 3.14  # approximate value of π
radius = diameter / 2
circumference = 2 * pi * radius
print("Circle circumference =", circumference, "\n")

# 3) Arithmetic mean of two numbers
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
mean = (a + b) / 2
print("Arithmetic mean of a and b =", mean, "\n")

# 4) Sum, product, and squares of each number
sum_ab = a + b
product_ab = a * b
square_a = a ** 2
square_b = b ** 2
print("Sum of a and b =", sum_ab)
print("Product of a and b =", product_ab)
print("Square of a =", square_a)
print("Square of b =", square_b)
