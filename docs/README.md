# Autonomous Spacecraft Rendezvous and Docking (GNC Simulation)

## Overview

This project implements a high-fidelity simulation of an autonomous spacecraft rendezvous, proximity operations, and docking (RPOD) scenario in Earth orbit. The goal is to design and integrate a complete Guidance, Navigation, and Control (GNC) system that enables a chaser spacecraft to safely approach and dock with a target vehicle using noisy sensor measurements and constrained actuation.

The simulation models the full closed-loop system, including orbital relative motion, state estimation, trajectory generation, and feedback control, reflecting real spacecraft operations used in missions such as ISS docking and on-orbit servicing.

## Objectives
- Simulate relative motion between two spacecraft in orbit
- Estimate the chaser's state using noisy sensor data
- Generate safe and feasible approach trajectories
- Control the spacecraft to achieve precise docking conditions
- Evaluate performance under uncertainty and disturbances

The final objective is to satisfy docking requirements on:
- relative position
- relative velocity
- relative attitude and angular rate

These conditions are critical for successful docking operations.

## System Architecture

The project is structured into three main subsystems:

### 1. Guidance

The guidance module computes a feasible trajectory from the current state to the docking interface.

It includes:
- waypoint-based or corridor-constrained trajectory generation
- multi-phase approach strategy:
  - far-range rendezvous
  - proximity operations
  - final docking approach
- enforcement of safety constraints:
  - keep-out zones
  - approach corridor geometry
  - velocity limits

The goal of guidance is to generate the required trajectory (position and velocity profile) that leads the chaser to the docking point safely.

### 2. Navigation

The navigation module estimates the relative state of the spacecraft using simulated sensors.

It includes:
- sensor models (e.g., range, line-of-sight, IMU)
- measurement noise and bias
- state estimation using an Extended Kalman Filter (EKF)

The navigation system combines:
- a dynamics model
- noisy measurements

to estimate:
- relative position and velocity
- possibly attitude and angular rate

This estimated state is used by both guidance and control.

### 3. Control

The control module generates actuator commands to track the guidance trajectory.

It includes:
- translational control using:
  - LQR or PID
- attitude control using:
  - quaternion-based feedback control
- actuator modeling:
  - thruster force limits
  - control allocation

The control system computes forces and torques required to minimize tracking error and satisfy docking constraints.

## Dynamics Model

The simulation is based on relative orbital dynamics between two spacecraft:
- Hill / Clohessy-Wiltshire equations for relative motion
- rigid body dynamics for spacecraft attitude
- optional disturbances (e.g., environmental forces)

Relative motion is modeled as the motion of a chaser spacecraft with respect to a target in orbit, commonly described using linearized equations such as the Clohessy-Wiltshire model.

## Simulation Features
- 3D relative motion in orbital frame
- closed-loop GNC architecture
- noisy and imperfect sensor measurements
- constrained control inputs
- multi-phase mission logic:
  - rendezvous
  - hold point
  - approach
  - docking

## Outputs and Evaluation

The system performance is evaluated using:
- trajectory tracking error
- estimation error (truth vs EKF)
- control effort and fuel usage
- docking success criteria
- Monte Carlo simulations for robustness