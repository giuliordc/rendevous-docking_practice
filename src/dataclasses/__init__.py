"""
Dataclasses for the spacecraft rendezvous and docking simulation.

This package contains all data class definitions used throughout the project:
- orbital_params.py: Orbital parameters for target and chaser spacecraft
- spacecraft_params.py: Spacecraft physical properties
- geometry.py: Geometric shapes and models
- relative_state.py: Individual state representation
- trajectory.py: Trajectory history data
- simulation.py: Complete simulation data container
"""

from .orbital_params import (
    OrbitalParametersTarget,
    OrbitalParametersChaser,
    InitialOrbitChaser
)

from .spacecraft_params import (
    SpacecraftParametersTarget,
    SpacecraftParametersTargetWithGeometry,
    SpacecraftParametersChaser,
    SpacecraftParametersChaserWithGeometry
)

from .geometry import (
    BoxGeometry,
    CylinderGeometry,
    SphereGeometry,
    MeshGeometry,
    CompositeGeometry,
    create_default_geometry
)

from .relative_state import RelativeState
from .trajectory import Trajectory
from .simulation import SimulationData

__all__ = [
    # Orbital Parameters
    'OrbitalParametersTarget',
    'OrbitalParametersChaser',
    'InitialOrbitChaser',
    
    # Spacecraft Parameters
    'SpacecraftParametersTarget',
    'SpacecraftParametersTargetWithGeometry',
    'SpacecraftParametersChaser',
    'SpacecraftParametersChaserWithGeometry',
    
    # Geometry
    'BoxGeometry',
    'CylinderGeometry',
    'SphereGeometry',
    'MeshGeometry',
    'CompositeGeometry',
    'create_default_geometry',
    
    # State and Trajectory
    'RelativeState',
    'Trajectory',
    'SimulationData'
]