"""
Trajectory data classes for storing motion history.
"""

from dataclasses import dataclass, field
import numpy as np
from .relative_state import RelativeState


@dataclass
class Trajectory:
    """Complete trajectory history of spacecraft motion."""
    times: list = field(default_factory=list)  # List of time points
    positions: list = field(default_factory=list)  # List of position vectors
    velocities: list = field(default_factory=list)  # List of velocity vectors
    attitudes: list = field(default_factory=list)  # List of attitude quaternions
    angular_velocities: list = field(default_factory=list)  # List of angular velocity vectors

    def append_state(self, state: RelativeState):
        """Add a state to the trajectory."""
        self.times.append(state.time)
        self.positions.append(state.position.copy())
        self.velocities.append(state.velocity.copy())
        self.attitudes.append(state.attitude.copy())
        self.angular_velocities.append(state.angular_velocity.copy())

    def get_state_at_time(self, time: float) -> RelativeState:
        """Get interpolated state at a specific time."""
        # Simple nearest neighbor for now - could add interpolation later
        idx = np.argmin(np.abs(np.array(self.times) - time))
        return RelativeState(
            time=self.times[idx],
            position=self.positions[idx],
            velocity=self.velocities[idx],
            attitude=self.attitudes[idx],
            angular_velocity=self.angular_velocities[idx]
        )

    @property
    def duration(self) -> float:
        """Total duration of trajectory."""
        if not self.times:
            return 0.0
        return self.times[-1] - self.times[0]

    @property
    def length(self) -> int:
        """Number of points in trajectory."""
        return len(self.times)

    def to_arrays(self):
        """Convert lists to numpy arrays for efficient computation."""
        return {
            'times': np.array(self.times),
            'positions': np.array(self.positions),
            'velocities': np.array(self.velocities),
            'attitudes': np.array(self.attitudes),
            'angular_velocities': np.array(self.angular_velocities)
        }