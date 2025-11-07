import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([2, 3, 5, 7])

m, b = np.polyfit(x, y, 1)
print(f"Slope (m): {m}, Intercept (b): {b}")