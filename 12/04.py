# 24bit119

# Que-4

import math

class RegularShape:
    def __init__(self):
        self.shape = None
        self.dimensions = {}

    def accept_data(self):
        self.shape = input("Enter the shape (square, rectangle, circle, triangle): ").lower()
        
        if self.shape == "square":
            self.dimensions['side'] = float(input("Enter the length of one side: "))
        elif self.shape == "rectangle":
            self.dimensions['length'] = float(input("Enter the length: "))
            self.dimensions['width'] = float(input("Enter the width: "))
        elif self.shape == "circle":
            self.dimensions['radius'] = float(input("Enter the radius: "))
        elif self.shape == "triangle":
            self.dimensions['side'] = float(input("Enter the length of one side (equilateral triangle): "))
        else:
            print("Unsupported shape!")

    def calculate_perimeter(self):
        if self.shape == "square":
            return 4 * self.dimensions['side']
        elif self.shape == "rectangle":
            return 2 * (self.dimensions['length'] + self.dimensions['width'])
        elif self.shape == "circle":
            return 2 * math.pi * self.dimensions['radius']
        elif self.shape == "triangle":
            return 3 * self.dimensions['side']
        else:
            return None

    def calculate_area(self):
        if self.shape == "square":
            return self.dimensions['side'] ** 2
        elif self.shape == "rectangle":
            return self.dimensions['length'] * self.dimensions['width']
        elif self.shape == "circle":
            return math.pi * (self.dimensions['radius'] ** 2)
        elif self.shape == "triangle":
            return (math.sqrt(3) / 4) * (self.dimensions['side'] ** 2)
        else:
            return None

shape = RegularShape()
shape.accept_data()

perimeter = shape.calculate_perimeter()
area = shape.calculate_area()

if perimeter is not None and area is not None:
    print(f"The perimeter/circumference of the {shape.shape} is: {perimeter:.2f}")
    print(f"The area of the {shape.shape} is: {area:.2f}")
else:
    print("Could not calculate for the given shape.")