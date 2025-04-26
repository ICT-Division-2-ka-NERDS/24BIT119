# 24bit119

# Que-3

import math

class Solid:
    def __init__(self, solid_type, **dimensions):
        self.solid_type = solid_type.lower()
        self.dimensions = dimensions

    def surface_area(self):
        if self.solid_type == 'sphere':
            radius = self.dimensions.get('radius')
            if radius is None:
                raise ValueError("Sphere requires 'radius' as dimension")
            return 4 * math.pi * radius**2
        
        elif self.solid_type == 'cylinder':
            radius = self.dimensions.get('radius')
            height = self.dimensions.get('height')
            if radius is None or height is None:
                raise ValueError("Cylinder requires 'radius' and 'height' as dimensions")
            return 2 * math.pi * radius * (radius + height)
        
        elif self.solid_type == 'cuboid':
            length = self.dimensions.get('length')
            width = self.dimensions.get('width')
            height = self.dimensions.get('height')
            if length is None or width is None or height is None:
                raise ValueError("Cuboid requires 'length', 'width', and 'height' as dimensions")
            return 2 * (length * width + length * height + width * height)
        
        else:
            raise ValueError(f"Unsupported solid type: {self.solid_type}")

    def volume(self):
        if self.solid_type == 'sphere':
            radius = self.dimensions.get('radius')
            if radius is None:
                raise ValueError("Sphere requires 'radius' as dimension")
            return (4/3) * math.pi * radius**3
        
        elif self.solid_type == 'cylinder':
            radius = self.dimensions.get('radius')
            height = self.dimensions.get('height')
            if radius is None or height is None:
                raise ValueError("Cylinder requires 'radius' and 'height' as dimensions")
            return math.pi * radius**2 * height
        
        elif self.solid_type == 'cuboid':
            length = self.dimensions.get('length')
            width = self.dimensions.get('width')
            height = self.dimensions.get('height')
            if length is None or width is None or height is None:
                raise ValueError("Cuboid requires 'length', 'width', and 'height' as dimensions")
            return length * width * height
        
        else:
            raise ValueError(f"Unsupported solid type: {self.solid_type}")

sphere = Solid('sphere', radius=5)
print(f"Sphere Surface Area: {sphere.surface_area():.2f}")
print(f"Sphere Volume: {sphere.volume():.2f}")

cylinder = Solid('cylinder', radius=3, height=7)
print(f"\nCylinder Surface Area: {cylinder.surface_area():.2f}")
print(f"Cylinder Volume: {cylinder.volume():.2f}")

cuboid = Solid('cuboid', length=4, width=6, height=8)
print(f"\nCuboid Surface Area: {cuboid.surface_area():.2f}")
print(f"Cuboid Volume: {cuboid.volume():.2f}")