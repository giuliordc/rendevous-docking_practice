"""
Simulation data container for storing complete simulation results.
"""

from dataclasses import dataclass, field
from .trajectory import Trajectory


@dataclass
class SimulationData:
    """Container for all simulation data."""
    target_trajectory: Trajectory = field(default_factory=Trajectory)
    chaser_trajectory: Trajectory = field(default_factory=Trajectory)
    control_history: list = field(default_factory=list)  # Control inputs over time
    sensor_measurements: list = field(default_factory=list)  # Sensor data over time
    estimation_errors: list = field(default_factory=list)  # Navigation errors over time

    def save_to_file(self, filepath: str):
        """Save simulation data to file (JSON or pickle)."""
        # TODO: Implement data saving
        pass

    @classmethod
    def load_from_file(cls, filepath: str) -> 'SimulationData':
        """Load simulation data from file."""
        # TODO: Implement data loading
        pass