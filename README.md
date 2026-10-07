# IndustriQ

Industrial equipment monitoring and machine learning, starting with cement-plant motors and variable frequency drives (VFDs).

## Overview

IndustriQ is a Python project for exploring equipment behavior, detecting unusual operating conditions, and presenting useful information to maintenance personnel.

The first version focuses on a motor-driven fan in a cement plant. Development begins with a simulator, followed by equipment health rules, a simple machine learning model, and a front end for displaying results.

The goal is to understand whether equipment is behaving as expected for its operating conditions—and explain the measurements behind an alert.

## Project Status

Early development: requirements and project setup.

The features below are planned and will be implemented incrementally.

## Version 1 Scope

- Simulate timestamped motor and VFD readings.
- Model normal operation, starts, stops, and load changes.
- Introduce controlled abnormal conditions.
- Load and validate equipment data.
- Configure equipment-specific limits.
- Display equipment status with explanations.
- Plot current, frequency, and temperature trends.
- Train and evaluate a baseline machine learning model.
- Build a simple front end to explore results.

## Initial Signals

| Signal | Unit | Purpose |
| --- | --- | --- |
| Timestamp | Date/time | Track readings over time |
| Equipment ID | — | Identify the asset |
| Run state | — | Distinguish stopped and running operation |
| Motor current | A | Observe electrical load |
| VFD output frequency | Hz | Provide operating-speed context |
| Motor temperature | °C | Track thermal behavior |
| Load demand | % | Represent simulated operating demand |

The temperature measurement location and simulation assumptions will be documented before implementation.

## Simulation Scenarios

The simulator will begin with normal operation, then add:

- Increased mechanical resistance
- Reduced cooling
- Missing sensor readings
- Sensor spikes and stuck values

Injected conditions will be stored separately from model inputs so they can be used to evaluate detection performance.

Simulation results will demonstrate software behavior under defined assumptions. Real equipment data will be needed to evaluate practical performance.

## Development Roadmap

1. Define requirements and organize the repository.
2. Build a normal-operation simulator.
3. Explore and validate the generated data.
4. Add equipment health rules.
5. Introduce abnormal scenarios.
6. Train and evaluate a baseline model.
7. Build a front end for equipment status and trends.
8. Evaluate the pipeline with real measurements.

Each milestone will be tracked through Git commits.

## Future Direction

Potential extensions include:

- Multiple equipment types and configurations
- Historian data integration
- Process-variable context
- Vibration and motor-current waveform analysis
- Maintenance records and fault history
- Fault classification
- Energy-efficiency monitoring
- Remaining-useful-life estimation, where suitable data is available

## Learning Goals

This project combines industrial maintenance experience with practical software engineering and machine learning.

Key topics include Python, time-series analysis, feature engineering, model evaluation, data visualization, and application design.

## Author

John Sullins
