import matplotlib.pyplot as plt


def f(x):
    return x ** 2


def df(x):
    return 2 * x


def euler_method(f_prime, x0, y0, h, num_steps):

    x = [x0]  # Initialize the list of time values with the initial value t0
    y = [y0]  # Initialize the list of solution values with the initial value y0

    for i in range(num_steps):
        x_i = x[i]  # Get the current time
        y_i = y[i]  # Get the current solution value

        # Compute the next solution value using Euler's method
        y_next = y_i + h * f_prime(x_i)

        # Compute the next time value
        x_next = x_i + h

        # Add the next time and solution values to the lists
        x.append(x_next)
        y.append(y_next)

    return x, y


x_initial = 1
y_initial = 1
size_step = 0.2
n = 5

x_values, y_values = euler_method(df, x_initial, y_initial, size_step, n)

# Getting the error
y_euler = y_values[-1]
y_accurate = f(x_values[-1])

print("x values:", x_values)
print("y values:", y_values)
print(f"Error = {y_accurate-y_euler}")

x_real = [1, 1.1, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
y_real = [num ** 2 for num in x_values]


# Plot the first curve in blue
plt.plot(x_values, y_values, color='red', label="Approximation with Euler's method")

# Plot the second curve in red
plt.plot(x_values, y_real, color='blue', label='Accurate curve')

# Add a legend and labels for the x and y-axis
plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
plt.title("Plot with h = 0.2")

# Show the plot
plt.show()
