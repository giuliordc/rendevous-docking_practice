"""
Data classe for chaser spacecraft state.

These classes store the actual data that changes during simulation,
unlike the parameters which are fixed.
"""

from dataclasses import dataclass, field
import numpy as np


@dataclass
class RelativeState:
    """Current relative state of chaser spacecraft in target's LVLH frame."""
    time: float = 0.0  # seconds
    position: np.ndarray = field(default_factory=lambda: np.zeros(3))  # [x, y, z] in meters
    velocity: np.ndarray = field(default_factory=lambda: np.zeros(3))  # [vx, vy, vz] in m/s
    attitude: np.ndarray = field(default_factory=lambda: np.array([1.0, 0.0, 0.0, 0.0]))  # quaternion [w, x, y, z]
    angular_velocity: np.ndarray = field(default_factory=lambda: np.zeros(3))  # [ωx, ωy, ωz] in rad/s

    def __post_init__(self):
        """Validate state dimensions."""
        if self.position.shape != (3,):
            raise ValueError("Position must be 3D vector.")
        if self.velocity.shape != (3,):
            raise ValueError("Velocity must be 3D vector.")
        if self.attitude.shape != (4,):
            raise ValueError("Attitude must be quaternion (4 elements).")
        if self.angular_velocity.shape != (3,):
            raise ValueError("Angular velocity must be 3D vector.")

    @property
    def state_vector(self) -> np.ndarray:
        """Return full state vector [pos, vel, att, ang_vel]."""
        return np.concatenate([self.position, self.velocity, self.attitude, self.angular_velocity])

    @classmethod
    def from_vector(cls, state_vector: np.ndarray, time: float = 0.0) -> 'RelativeState':
        """Create RelativeState from state vector."""
        if len(state_vector) != 13:
            raise ValueError("State vector must be 13 elements: [pos(3), vel(3), att(4), ang_vel(3)]")
        return cls(
            time=time,
            position=state_vector[0:3],
            velocity=state_vector[3:6],
            attitude=state_vector[6:10],
            angular_velocity=state_vector[10:13]
        )
