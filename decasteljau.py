import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb


def de_casteljau(control_points, t):
    n = len(control_points) - 1
    points = [point[:] for point in control_points]  # Copy of control points
    for r in range(1, n + 1):
        for i in range(n - r + 1):
            points[i] = [(1 - t) * points[i][0] + t * points[i + 1][0],
                         (1 - t) * points[i][1] + t * points[i + 1][1]]
    return points[0]

# Usage example
control_points = np.array([[0, 0], [1, 3], [2, -3], [6, 4]])
t = 0.5
point_on_curve = de_casteljau(control_points, t)
print("Point on curve at t =", t, ":", point_on_curve)
