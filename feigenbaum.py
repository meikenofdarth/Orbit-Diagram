import numpy as np

def logistic_map(r, x):
    return r * x * (1 - x)

def get_period(r):
    """
    Calculates the period of the logistic map for a given r.
    Returns -1 if the system is chaotic or the period is too long.
    """
    # Use a consistent initial condition
    x = 0.5
    # Settle onto the attractor
    for _ in range(1000):
        x = logistic_map(r, x)

    # Find the period by checking for a cycle
    x_on_attractor = x
    max_period_to_check = 2**10  # e.g., 1024
    for i in range(1, max_period_to_check + 1):
        x = logistic_map(r, x)
        # Check if we returned to the starting point (using tolerance)
        if np.isclose(x, x_on_attractor):
            return i
    
    # If no cycle is found, assume it's chaotic
    return -1

def find_bifurcation_points_fast(r_min, r_max, num_r_steps):
    """
    Finds bifurcation points using a faster period-checking method.
    """
    r_values = np.linspace(r_min, r_max, num_r_steps)
    bifurcation_points = []
    last_period = 1

    for r in r_values:
        current_period = get_period(r)

        # A period doubling event has occurred
        if current_period == 2 * last_period:
            bifurcation_points.append(r)
            last_period = current_period
            # We don't need to find more than a few points to get a good estimate
            if last_period >= 16: 
                break
                
    return np.array(bifurcation_points)

# --- This function remains the same ---
def approximate_feigenbaum_delta(bifurcation_points):
    """Approximates the first Feigenbaum constant."""
    deltas = []
    # Need at least 3 bifurcation points to calculate one delta value
    if len(bifurcation_points) < 3:
        print("Not enough bifurcation points found to calculate delta.")
        return None
    
    print(f"Bifurcation points found at r = {bifurcation_points}")
    
    # Calculate delta from the ratios of successive intervals
    for i in range(2, len(bifurcation_points)):
        delta = (bifurcation_points[i-1] - bifurcation_points[i-2]) / (bifurcation_points[i] - bifurcation_points[i-1])
        deltas.append(delta)
    
    print(f"Calculated ratios (deltas): {deltas}")
    return np.mean(deltas)

# --- Run the faster code ---
# We can use fewer steps now because each step is faster
bifurcation_points = find_bifurcation_points_fast(2.9, 3.57, 50000)
delta_approximation = approximate_feigenbaum_delta(bifurcation_points)

if delta_approximation is not None:
    print(f"\nApproximated Feigenbaum constant (δ): {delta_approximation}")