# Project Structure

This document outlines the folder structure for the Autonomous Spacecraft Rendezvous and Docking simulation project.

## Root Directory
- `README.md`: Project overview and documentation
- `requirements.txt`: Python dependencies
- `.gitignore`: Files to ignore in Git
- `venv/`: Virtual environment (ignored by Git)

## Folders

### `dataclasses/`
Data class definitions (separated from logic for better organization):
- `orbital_params.py`: Orbital parameters for target and chaser spacecraft (OrbitalParametersTarget, OrbitalParametersChaser, InitialOrbitChaser)
- `spacecraft_params.py`: Spacecraft physical properties (SpacecraftParametersTarget/Chaser classes)
- `geometry.py`: Geometric shapes (BoxGeometry, CylinderGeometry, etc.)
- `relative_state.py`: Individual state representation (RelativeState)
- `trajectory.py`: Trajectory history data (Trajectory)
- `simulation.py`: Complete simulation data container (SimulationData)
- `__init__.py`: Package initialization with convenient imports

### `simulations/`
Main simulation scripts and scenarios:
- `basic_rendezvous.py`: Simple rendezvous simulation
- `full_docking.py`: Complete docking scenario
- `monte_carlo.py`: Robustness testing with Monte Carlo

### `utils/`
Utility functions and helpers:
- `plotting.py`: Visualization and plotting functions
- `math_utils.py`: Mathematical utilities (quaternions, rotations)
- `data_io.py`: Data loading and saving

### `tests/`
Unit tests and validation:
- `test_dynamics.py`: Tests for dynamics module
- `test_navigation.py`: Tests for navigation/estimation
- `test_control.py`: Tests for control algorithms

### `data/`
Input data and configuration files:
- `orbital_params.json`: Orbital parameters and initial conditions
- `sensor_config.yaml`: Sensor model configurations
- `scenarios/`: Pre-defined simulation scenarios

### `results/`
Output files and results:
- `plots/`: Generated plots and visualizations
- `logs/`: Simulation logs and data
- `reports/`: Analysis reports and metrics

### `docs/`
Additional documentation:
- `api_reference.md`: Module and function documentation
- `equations.md`: Mathematical formulations
- `user_guide.md`: How to run simulations
