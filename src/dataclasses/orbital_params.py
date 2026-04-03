"""
Orbital parameters for the spacecraft simulation.
"""

from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class OrbitalParametersTarget:
    """Orbital parameters for the target spacecraft."""
    mu: float = 3.986004418e14  # Earth's gravitational parameter (m³/s²)
    altitude: float = 400e3      # Orbit altitude (m)
    eccentricity: float = 0.0    # Orbital eccentricity
    inclination: float = np.deg2rad(51.6)  # Inclination (radians)
    
    @property
    def semi_major_axis(self) -> float:
        """Compute semi-major axis from altitude."""
        R_earth = 6.371e6  # Earth radius (m)
        return R_earth + self.altitude
    
    @property
    def mean_motion(self) -> float:
        """Compute orbital mean motion n = sqrt(mu / a³)."""
        return np.sqrt(self.mu / self.semi_major_axis**3)


@dataclass(frozen=True)
class OrbitalParametersChaser:
    """Orbital parameters for the chaser spacecraft."""
    mu: float = 3.986004418e14  # Earth's gravitational parameter (m³/s²)
    altitude: float = 400e3      # Orbit altitude (m)
    eccentricity: float = 0.0    # Orbital eccentricity
    inclination: float = np.deg2rad(51.6)  # Inclination (radians)
    
    @property
    def semi_major_axis(self) -> float:
        """Compute semi-major axis from altitude."""
        R_earth = 6.371e6  # Earth radius (m)
        return R_earth + self.altitude
    
    @property
    def mean_motion(self) -> float:
        """Compute orbital mean motion n = sqrt(mu / a³)."""
        return np.sqrt(self.mu / self.semi_major_axis**3)


@dataclass(frozen=True)
class InitialOrbitChaser:
    """Initial orbital parameters for the chaser spacecraft."""
    altitude: float = 400e3      # Initial orbit altitude (m)
    eccentricity: float = 0.0    # Orbital eccentricity
    inclination: float = np.deg2rad(51.6)  # Inclination (radians)
    true_anomaly: float = 0.0    # Initial true anomaly (radians)