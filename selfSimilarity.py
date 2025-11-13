import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    return r * x * (1 - x)

def zoomed_orbit_diagram(r_min, r_max, x_min, x_max, num_r_steps, num_iterations, num_to_plot):
    """
    Generates and plots a zoomed-in orbit diagram.
    """
    r_values = np.linspace(r_min, r_max, num_r_steps)
    x_values = []
    r_plot_values = []

    for r in r_values:
        x = 0.5
        for _ in range(num_iterations - num_to_plot):
            x = logistic_map(r, x)
        for _ in range(num_to_plot):
            x = logistic_map(r, x)
            if x > x_min and x < x_max:
                x_values.append(x)
                r_plot_values.append(r)

    plt.figure(figsize=(12, 8))
    plt.plot(r_plot_values, x_values, ',b', alpha=0.25)
    plt.title("Zoomed-in Orbit Diagram")
    plt.xlabel("r")
    plt.ylabel("x")
    plt.show()

# Parameters for the zoomed-in view
zoomed_orbit_diagram(3.5, 3.6, 0.3, 0.6, 5000, 1000, 200)