import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    """
    Calculates the next value in the logistic map sequence.
    """
    return r * x * (1 - x)

def orbit_diagram(r_min, r_max, num_r_steps, num_iterations, num_to_plot):
    """
    Generates and plots the orbit diagram for the logistic map.
    """
    r_values = np.linspace(r_min, r_max, num_r_steps)
    x_values = []
    r_plot_values = []

    for r in r_values:
        x = 0.5  # Initial condition
        # Iterate to let the system settle
        for _ in range(num_iterations - num_to_plot):
            x = logistic_map(r, x)
        # Collect the values to plot
        for _ in range(num_to_plot):
            x = logistic_map(r, x)
            x_values.append(x)
            r_plot_values.append(r)

    plt.figure(figsize=(12, 8))
    plt.plot(r_plot_values, x_values, ',b', alpha=0.25)
    plt.title("Orbit Diagram of the Logistic Map")
    plt.xlabel("r")
    plt.ylabel("x")
    plt.show()

# Parameters for the orbit diagram
orbit_diagram(2.4, 4.0, 10000, 1000, 200)