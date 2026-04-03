"""
Spacecraft physical parameters and properties.
"""

from dataclasses import dataclass, field
import numpy as np
from .geometry import BoxGeometry


@dataclass(frozen=True)
class SpacecraftParametersTarget:
    """Physical properties of the target spacecraft."""
    mass: float = 2000.0  # kg (typical satellite mass)
    area: float = 10.0    # m² (cross-sectional area)
    drag_coefficient: float = 2.5  # typical value for satellite
    moment_of_inertia: np.ndarray = field(
        default_factory=lambda: np.diag([8000, 8000, 10000])  # 3x3 inertia tensor (kg⋅m²)
    )
    dimensions: tuple = (2.0, 2.0, 3.0)  # (length, width, height) in meters
    emission_coefficient: float = 0.8    # thermal emissivity
    absorption_coefficient: float = 0.3  # solar absorptivity
    
    def __post_init__(self):
        """Validate parameters."""
        if self.mass <= 0:
            raise ValueError("Mass must be positive.")
        if self.moment_of_inertia.shape != (3, 3):
            raise ValueError("Moment of inertia must be a 3x3 matrix.")
        if not all(d > 0 for d in self.dimensions):
            raise ValueError("All dimensions must be positive.")


@dataclass(frozen=True)
class SpacecraftParametersTargetWithGeometry(SpacecraftParametersTarget):
    """Target spacecraft with detailed geometry."""
    geometry: BoxGeometry = field(
        default_factory=lambda: BoxGeometry(2.0, 2.0, 3.0)
    )


@dataclass(frozen=True)
class SpacecraftParametersChaser:
    """Physical properties of the chaser spacecraft."""
    mass: float = 1500.0  # kg (chaser slightly lighter)
    area: float = 8.0     # m² (cross-sectional area)
    drag_coefficient: float = 2.5  # typical value for satellite
    moment_of_inertia: np.ndarray = field(
        default_factory=lambda: np.diag([6000, 6000, 7500])  # 3x3 inertia tensor (kg⋅m²)
    )
    dimensions: tuple = (1.8, 1.8, 2.5)  # (length, width, height) in meters
    emission_coefficient: float = 0.8    # thermal emissivity
    absorption_coefficient: float = 0.3  # solar absorptivity
    
    def __post_init__(self):
        """Validate parameters."""
        if self.mass <= 0:
            raise ValueError("Mass must be positive.")
        if self.moment_of_inertia.shape != (3, 3):
            raise ValueError("Moment of inertia must be a 3x3 matrix.")
        if not all(d > 0 for d in self.dimensions):
            raise ValueError("All dimensions must be positive.")


@dataclass(frozen=True)
class SpacecraftParametersChaserWithGeometry(SpacecraftParametersChaser):
    """Chaser spacecraft with detailed geometry."""
    geometry: BoxGeometry = field(
        default_factory=lambda: BoxGeometry(1.8, 1.8, 2.5)
    )