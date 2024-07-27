import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Define the function
def f(x):
    return x ** 2

# Integration limits
a = 0
b = 2

# Monte Carlo method for calculating the integral
N = 100000  # Number of random points
x_random = np.random.uniform(a, b, N)
y_random = f(x_random)
integral_mc = (b - a) * np.mean(y_random)

# Calculate the integral using the quad function
integral_quad, error = spi.quad(f, a, b)

# Create the plot
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Plot the function
ax.plot(x, y, 'r', linewidth=2)

# Fill the area under the curve
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Set up the plot
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Add integration limits and title to the plot
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Integration Plot of f(x) = x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()

# Output the results
print("Integral using Monte Carlo method: ", integral_mc)
print("Integral using quad: ", integral_quad)
print("Error of Monte Carlo method: ", abs(integral_mc - integral_quad))

# Analytical value of the integral
integral_analytical = (2 ** 3) / 3
print("Analytical value of the integral: ", integral_analytical)
print("Error of Monte Carlo method from analytical value: ", abs(integral_mc - integral_analytical))


