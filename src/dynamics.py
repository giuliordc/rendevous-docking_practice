# Implement Clohessy Whiltsher equations for relative motion in orbit
import numpy as np

# Create frozen Dataclass for the physical parameters of the system
from dataclasses import dataclass
@dataclass(frozen=True)
class PhysicalParameters:
    mu: float # Gravitational parameter of the central body
    n: float # Mean motion of the orbit
    r: float # Radius of the orbit

