# Example of using lambda functions in Python

# A simple lambda function that adds two numbers
add = lambda x, y: x + y

# Using the lambda function
result = add(5, 3)
print("5 + 3 =", result)

# Lambda function to square a number
square = lambda x: x ** 2
print("Square of 4:", square(4))

# Lambda function with map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)

# Lambda function with filter
even_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Even numbers:", even_numbers)

# Lambda to calculate simple interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (years): "))
simple_interest = lambda p, r, t: (p * r * t) / 100
print("Simple Interest:", simple_interest(principal, rate, time))

# Lambda to calculate volume of a cylinder
radius_cyl = float(input("Enter radius of cylinder: "))
height_cyl = float(input("Enter height of cylinder: "))
volume_cylinder = lambda r, h: 3.14159 * r ** 2 * h
print("Volume of Cylinder:", volume_cylinder(radius_cyl, height_cyl))

# Lambda to calculate volume of a pyramid
base_area = float(input("Enter base area of pyramid: "))
height_pyr = float(input("Enter height of pyramid: "))
volume_pyramid = lambda b, h: (b * h) / 3
print("Volume of Pyramid:", volume_pyramid(base_area, height_pyr))

# Lambda to calculate area of a rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area_rectangle = lambda l, w: l * w
print("Area of Rectangle:", area_rectangle(length, width))

# Lambda to calculate area of a circle
radius_circle = float(input("Enter radius of circle: "))
area_circle = lambda r: 3.14159 * r ** 2
print("Area of Circle:", area_circle(radius_circle))

# Lambda to calculate diameter of a circle
diameter = lambda r: 2 * r
print("Diameter of Circle:", diameter(radius_circle))

# Lambda to calculate area of a parallelogram
base_para = float(input("Enter base of parallelogram: "))
height_para = float(input("Enter height of parallelogram: "))
area_parallelogram = lambda b, h: b * h
print("Area of Parallelogram:", area_parallelogram(base_para, height_para))