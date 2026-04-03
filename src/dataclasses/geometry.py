"""
Optional geometry classes for complex spacecraft shapes.

Use this module if you want to define detailed spacecraft geometry
for more accurate physical modeling (drag, radiation, collisions, etc.)
"""

from dataclasses import dataclass, field
import numpy as np


@dataclass(frozen=True)
class BoxGeometry:
    """Simple box/cuboid geometry."""
    length: float  # m (along x-axis)
    width: float   # m (along y-axis)
    height: float  # m (along z-axis)
    center_of_mass: np.ndarray = field(
        default_factory=lambda: np.array([0.0, 0.0, 0.0])
    )
    
    def volume(self) -> float:
        """Calculate volume of the box."""
        return self.length * self.width * self.height


@dataclass(frozen=True)
class CylinderGeometry:
    """Cylindrical geometry (e.g., for fuel tanks, solar panels)."""
    radius: float  # m
    height: float  # m
    axis: str = 'z'  # Axis aligned with cylinder ('x', 'y', or 'z')
    center_of_mass: np.ndarray = field(
        default_factory=lambda: np.array([0.0, 0.0, 0.0])
    )
    
    def volume(self) -> float:
        """Calculate volume of the cylinder."""
        return np.pi * self.radius**2 * self.height


@dataclass(frozen=True)
class SphereGeometry:
    """Spherical geometry."""
    radius: float  # m
    center_of_mass: np.ndarray = field(
        default_factory=lambda: np.array([0.0, 0.0, 0.0])
    )
    
    def volume(self) -> float:
        """Calculate volume of the sphere."""
        return (4/3) * np.pi * self.radius**3


@dataclass(frozen=True)
class MeshGeometry:
    """Complex mesh geometry from file or vertices.
    
    Useful for detailed spacecraft shapes from CAD models.
    Represents the geometry as a triangular mesh.
    """
    vertices: np.ndarray  # N x 3 array of vertex coordinates (m)
    faces: np.ndarray     # M x 3 array of face indices (triangle mesh)
    center_of_mass: np.ndarray = field(
        default_factory=lambda: np.array([0.0, 0.0, 0.0])
    )
    
    def __post_init__(self):
        """Validate mesh geometry."""
        if self.vertices.shape[1] != 3:
            raise ValueError("Vertices must be N x 3 array.")
        if self.faces.shape[1] != 3:
            raise ValueError("Faces must be M x 3 array (triangular).")
    
    @staticmethod
    def from_stl_file(filepath: str):
        """Load mesh geometry from STL (stereolithography) file.
        
        Args:
            filepath: Path to .stl file
            
        Returns:
            MeshGeometry object
            
        Note: Requires numpy-stl or similar library
        """
        # TODO: Implement STL file loading
        raise NotImplementedError("STL loading not yet implemented.")


@dataclass(frozen=True)
class CompositeGeometry:
    """Composite geometry made of multiple primitive shapes.
    
    Useful for spacecraft with multiple components
    (e.g., main body + solar panels + antenna)
    """
    components: list = field(default_factory=list)  # List of geometry objects
    
    def total_volume(self) -> float:
        """Calculate total volume of all components."""
        total = 0.0
        for component in self.components:
            if hasattr(component, 'volume'):
                total += component.volume()
        return total


# ============================================================================
# Helper function to create geometry from spacecraft parameters
# ============================================================================

def create_default_geometry(dimensions: tuple) -> BoxGeometry:
    """Create a simple box geometry from dimensions tuple.
    
    Args:
        dimensions: (length, width, height) tuple in meters
        
    Returns:
        BoxGeometry object
    """
    return BoxGeometry(
        length=dimensions[0],
        width=dimensions[1],
        height=dimensions[2]
    )
