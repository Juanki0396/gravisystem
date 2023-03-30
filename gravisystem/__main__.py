from __future__ import annotations
from dataclasses import dataclass

import math

GRAV_CONSTANT = 6.6743e-11 # m³kg⁻¹s⁻²

@dataclass
class Vector:
    x: float
    y: float

    def __add__(self, vec: Vector) -> Vector:
        return Vector(self.x + vec.x, self.y + vec.y) 

    def __sub__(self, vec: Vector) -> Vector:
        return Vector(self.x - vec.x, self.y - vec.y) 

    def dot(self, vec: Vector) -> float:
        """Compute the scalar product"""
        return self.x * vec.x + self.y * vec.y

    def scalar_mult(self, n: float) -> Vector:
        """Multiplies the vector by a scalar and return a new vector"""
        return Vector(self.x * n, self.y * n)

    def modulus(self) -> float:
        """Compute the modulus of the vector"""
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self) -> Vector:
        """Create a new normalize vector"""
        mod = self.modulus()
        return Vector(self.x/mod, self.y/mod)

@dataclass
class Body:
    mass: int
    pos: Vector
    vel: Vector

def force_btw_bodies(b1: Body, b2: Body) -> Vector:
    """Compute gravitation force between 2 bodies"""
    mod = GRAV_CONSTANT * (b1.mass * b2.mass) / ((b1.pos - b2.pos).modulus())**2
    return (b2.pos - b1.pos).normalize().scalar_mult(mod)

# TODO: Compute the total force on a body 
# TODO: Compute the acceleration from total force
# TODO: Update velocity and position with Euler method


planet = Body(mass=1, pos=Vector(1,2), vel=Vector(1,2))
planet2 = Body(mass=1, pos=Vector(1,4), vel=Vector(1,2))
print(force_btw_bodies(planet, planet2))

    

