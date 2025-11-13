# Assignment 4: Analysis of the Logistic Map

This project explores the dynamics of the logistic map, a classic example of how chaotic behavior can arise from a simple nonlinear equation. The scripts provided generate the orbit diagram, demonstrate the concept of self-similarity, and numerically approximate the first Feigenbaum constant.

This repository was created for the "Nonlinear Dynamics" course assignment.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [How to Run](#how-to-run)
- [Code Overview](#code-overview)
- [Expected Output](#expected-output)
- [References](#references)

## Features
- **Orbit Diagram Generation**: Visualizes the long-term behavior of the logistic map for a range of growth rate parameters (`r`).
- **Self-Similarity Demonstration**: Includes a script to zoom into a specific region of the orbit diagram, revealing its fractal nature.
- **Feigenbaum Constant Approximation**: Numerically calculates an approximation of the first Feigenbaum constant (δ ≈ 4.669), a universal value in chaos theory.

## Requirements
- Python 3.x
- `numpy`
- `matplotlib`

## Code Overview

The Python script (`orbit.py`) is organized into several functions:

-   `logistic_map(r, x)`: Computes the next value (`x_n+1`) in the logistic map sequence for a given `r` and `x_n`.
-   `orbit_diagram(...)`: Generates and plots the main orbit diagram. It iterates through a range of `r` values, discards initial transient values, and plots the subsequent points of the attractor.
-   `zoomed_orbit_diagram(...)`: A variation of the orbit diagram function that allows plotting a specific, zoomed-in region of the map to demonstrate self-similarity.
-   `find_bifurcation_points(...)`: A numerical function that iterates through `r` values to find the points where period-doubling bifurcations occur.
-   `approximate_feigenbaum_delta(...)`: Takes the list of bifurcation points and uses them to calculate the ratio of successive bifurcation intervals, providing an approximation of the Feigenbaum constant δ.

## Expected Output

When the script is run, you should expect:
1.  A plot window showing the **Orbit Diagram of the Logistic Map**, illustrating the period-doubling route to chaos.
2.  A second plot window showing a **Zoomed-in Orbit Diagram**, which highlights the self-similar, fractal structure of the map.
3.  A message printed in your terminal with the numerically approximated value of the first Feigenbaum constant:
    ```
    Bifurcation points found at r = [2.99096102 3.44595372 3.54273045 3.56388948]
    Calculated ratios (deltas): [np.float64(4.701467737468822), np.float64(4.573780873970964)]

    Approximated Feigenbaum constant (δ): 4.637624305719893
    ```

## References
This work is based on the concepts described in the field of nonlinear dynamics and chaos theory.
-   Strogatz, S. H. (2015).