# This is a geometry calculator that was made as I learn python.
# For now, it can only support 4, 2 dimensional shapes (square, rectangle, circle and triangle);
# and 4, 3 dimensional shapes (cube, cuboid, sphere and triangular prism).
# This is the very first project that I took very seriously.

import math

measure = input("Are you looking for the area, perimeter or volume? ").lower()

#Area

if measure == "area":
    shape = input("What shape do you wish to solve? ").lower()
    if shape == "square":
        unit = input("What unit of measurement is being asked? ").lower()
        if unit == "cm":
            side = float(input("What is the side length of the square? "))
            area = side**2
            print(f"The area of the {shape} is {round(area, 2)}{unit}².")
        elif unit == "km":
            side = float(input("What is the side length of the square? "))
            area = side**2
            print(f"The area of the {shape} is {round(area, 2)}{unit}².")
        elif unit == "m":
            side = float(input("What is the side length of the square? "))
            area = side**2
            print(f"The area of the {shape} is {round(area, 2)}{unit}².")
        else:
            print("Invalid")

    elif shape == "rectangle":
        unit = input("What unit of measurement is being asked? ").lower()
        if unit == "cm":
            length = float(input("What is the length of the rectangle? "))
            width = float(input("What is the width of the rectangle? "))
            area = length * width
            print(f"The area of the {shape} is {round(area, 2)}{unit}².")
        elif unit == "km":
            length = float(input("What is the length of the rectangle? "))
            width = float(input("What is the width of the rectangle? "))
            area = length * width
            print(f"The area of the {shape} is {round(area, 2)}{unit}².")
        elif unit == "m":
            length = float(input("What is the length of the rectangle? "))
            width = float(input("What is the width of the rectangle? "))
            area = length * width
            print(f"The area of the {shape} is {round(area, 2)}{unit}².")
        else:
            print("Invalid")

    elif shape == "circle":
        unit = input("What unit of measurement is being asked? ").lower()
        if unit == "cm":
            radius = float(input("What is the radius of the circle? "))
            area = math.pi * radius**2
            print(f"The area of the {shape} is {round(area, 2)}{unit}²")
        elif unit == "in":
            radius = float(input("What is the radius of the circle? "))
            area = math.pi * radius**2
            print(f"The area of the {shape} is {round(area, 2)}{unit}²")
        elif unit == "m":
            radius = float(input("What is the radius of the circle? "))
            area = math.pi * radius**2
            print(f"The area of the {shape} is {round(area, 2)}{unit}²")
        else:
            print("Invalid")

    elif shape == "triangle":
        unit = input("What unit of measurement is being asked? ").lower()
        if unit == "cm":
            base = float(input("What is the base of the triangle? "))
            height = float(input("What is the height of the triangle? "))
            area = base * height / 2
            print(f"The area of the {shape} is {round(area, 2)}{unit}²")
        elif unit == "m":
            base = float(input("What is the base of the triangle? "))
            height = float(input("What is the height of the triangle? "))
            area = base * height / 2
            print(f"The area of the {shape} is {round(area, 2)}{unit}²")
        elif unit == "in":
            base = float(input("What is the base of the triangle? "))
            height = float(input("What is the height of the triangle? "))
            area = base * height / 2
            print(f"The area of the {shape} is {round(area, 2)}{unit}²")
        else:
            print("Invalid")
    else:
        print("Invalid")

#Perimeter

elif measure == "perimeter":
    shape = input("What shape do you wish to solve? ").lower()
    if shape == "square":
        unit = input("What unit of measurement is being asked? ").lower()
        if unit == "cm":
            side = float(input("What is the side length of the square? "))
            perimeter = 4 * side
            print(f"The perimeter of the square is {round(perimeter, 2)}{unit}")
        elif unit == "km":
            side = float(input("What is the side length of the square? "))
            perimeter = 4 * side
            print(f"The perimeter of the square is {round(perimeter, 2)}{unit}")
        elif unit == "m":
            side = float(input("What is the side length of the square? "))
            perimeter = 4 * side
            print(f"The perimeter of the square is {round(perimeter, 2)}{unit}")
        else:
            print("Invalid")

    elif shape == "rectangle":
        unit = input("What unit of measurement is being asked? ").lower()
        if unit == "cm":
            length = float(input("What is the length of the rectangle? "))
            width = float(input("What is the width of the rectangle? "))
            perimeter = 2 * length + 2 * width
            print(f"The perimeter of the square is {round(perimeter, 2)}{unit}")
        elif unit == "km":
            length = float(input("What is the length of the rectangle? "))
            width = float(input("What is the width of the rectangle? "))
            perimeter = 2 * length + 2 * width
            print(f"The perimeter of the square is {round(perimeter, 2)}{unit}")
        elif unit == "m":
            length = float(input("What is the length of the rectangle? "))
            width = float(input("What is the width of the rectangle? "))
            perimeter = 2 * length + 2 * width
            print(f"The perimeter of the square is {round(perimeter, 2)}{unit}")
        else:
            print("Invalid")

    elif shape == "circle":
        unit = input("What unit of measurement is being asked? ").lower()
        if unit == "cm":
            radius = float(input("What is the radius of the circle? "))
            perimeter = 2 * math.pi * radius
            print(f"The perimeter of the {shape} is {round(perimeter, 2)}{unit}")
        elif unit == "in":
            radius = float(input("What is the radius of the circle? "))
            perimeter = 2 * math.pi * radius
            print(f"The perimeter of the {shape} is {round(perimeter, 2)}{unit}")
        elif unit == "m":
            radius = float(input("What is the radius of the circle? "))
            perimeter = 2 * math.pi * radius
            print(f"The perimeter of the {shape} is {round(perimeter, 2)}{unit}")
        else:
            print("Invalid")

    elif shape == "triangle":
        unit = input("What unit of measurement is being asked? ").lower()
        if unit == "cm":
            a = float(input("What is the measurement of the right side of the triangle? "))
            b = float(input("What is the measurement of the left side of the triangle? "))
            c = float(input("What is the measurement of the base of the triangle? "))
            perimeter = a + b + c
            print(f"The perimeter of the {shape} is {round(perimeter, 2)}{unit}")

        elif unit == "in":
            a = float(input("What is the measurement of the right side of the triangle? "))
            b = float(input("What is the measurement of the left side of the triangle? "))
            c = float(input("What is the measurement of the base of the triangle? "))
            perimeter = a + b + c
            print(f"The perimeter of the {shape} is {round(perimeter, 2)}{unit}")

        elif unit == "m":
            a = float(input("What is the measurement of the right side of the triangle? "))
            b = float(input("What is the measurement of the left side of the triangle? "))
            c = float(input("What is the measurement of the base of the triangle? "))
            perimeter = a + b + c
            print(f"The perimeter of the {shape} is {round(perimeter, 2)}{unit}")
        else:
            print("Invalid")
    else:
        print("Invalid")
#Volume

elif measure == "volume":
    shape = input("What shape do you wish to solve? ").lower()
    if shape == "cube":
        unit = input("What unit of measurement is being asked? ").lower()
        if unit == "cm":
            side = float(input("What is the side of the cube? "))
            volume = side**3
            print(f"The volume of the {shape} is {round(volume, 2)}{unit}³")
        elif unit == "m":
            side = float(input("What is the side of the cube? "))
            volume = side**3
            print(f"The volume of the {shape} is {round(volume, 2)}{unit}³")
        elif unit == "in":
            side = float(input("What is the side of the cube? "))
            volume = side**3
            print(f"The volume of the {shape} is {round(volume, 2)}{unit}³")
        else:
            print("Invalid")

    elif shape == "cuboid":
        unit = input("What unit of measurement is being asked? ").lower()
        if unit == "cm":
            length = float(input("What is the length of the cuboid? "))
            breadth = float(input("What is the breadth of the cuboid? "))
            height = float(input("What is the height of the  cuboid? "))
            volume = length * breadth * height
            print(f"The volume of the {shape} is {round(volume, 2)}{unit}³")
        elif unit == "m":
            length = float(input("What is the length of the cuboid? "))
            breadth = float(input("What is the breadth of the cuboid? "))
            height = float(input("What is the height of the  cuboid? "))
            volume = length * breadth * height
            print(f"The volume of the {shape} is {round(volume, 2)}{unit}³")
        elif unit == "in":
            length = float(input("What is the length of the cuboid? "))
            breadth = float(input("What is the breadth of the cuboid? "))
            height = float(input("What is the height of the  cuboid? "))
            volume = length * breadth * height
            print(f"The volume of the {shape} is {round(volume, 2)}{unit}³")
        else:
            print("Invalid")

    elif shape == "sphere":
        unit = input("What unit of measurement is being asked? ").lower()
        if unit == "cm":
            radius = float(input("What is the radius of the sphere? "))
            volume = 4 * math.pi * radius**3 / 3
            print(f"The volume of the {shape} is {round(volume, 2)}{unit}³")
        elif unit == "m":
            radius = float(input("What is the radius of the sphere? "))
            volume = 4 * math.pi * radius**3 / 3
            print(f"The volume of the {shape} is {round(volume, 2)}{unit}³")
        elif unit == "in":
            radius = float(input("What is the radius of the sphere? "))
            volume = 4 * math.pi * radius**3 / 3
            print(f"The volume of the {shape} is {round(volume, 2)}{unit}³")
        else:
            print("Invalid")

    elif shape == "triangular prism":
        unit = input("What unit of measurement is being asked? ").lower()
        if unit == "cm":
            base = float(input("What is the base of the triangular prism? "))
            height = float(input("What is the height of the triangular prism? "))
            length = float(input("What is the length of the triangular prism? "))
            volume = base * height * length / 2
            print(f"The volume of the {shape} is {round(volume, 2)}{unit}³")
        elif unit == "m":
            base = float(input("What is the base of the triangular prism? "))
            height = float(input("What is the height of the triangular prism? "))
            length = float(input("What is the length of the triangular prism? "))
            volume = base * height * length / 2
            print(f"The volume of the {shape} is {round(volume, 2)}{unit}³")
        elif unit == "in":
            base = float(input("What is the base of the triangular prism? "))
            height = float(input("What is the height of the triangular prism? "))
            length = float(input("What is the length of the triangular prism? "))
            volume = base * height * length / 2
            print(f"The volume of the {shape} is {round(volume, 2)}{unit}³")
        else:
            print("Invalid")
    else:
        print("Invalid")

else:
    print("Invalid")
