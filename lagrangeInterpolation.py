import numpy
import numpy as np
import matplotlib.pyplot as plt


def displayLagrangePolynomial(x_values, y_values):
    # Calculating values of polynomial
    x_dense = np.linspace(min(x_values), max(x_values), 500)
    y_dense = np.array([calculateLagrangeInterpolation(x_values, y_values, xi) for xi in x_dense])

    # Show polynomial and given points on plot
    plt.plot(x_dense, y_dense, label="Lagrange Polynomial", color="red")
    plt.scatter(x_values, y_values, color="blue", label="Points")

    plt.title('Lagrange Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


# Calculate Polynomial via Lagrange Interpolation, inputting all the points and the x value you want to calculate
def calculateLagrangeInterpolation(x_values, y_values, x):
    n = len(x_values)

    # Result Polynomial
    P = 0

    # Iterate through number of points. Every iteration one Lagrange polynomial Li is added to the result Polynomial P
    for i in range(n):
        xi = x_values[i]
        yi = y_values[i]

        # Construct Lagrange polynomial Li for given points
        Li = 1
        for j in range(n):
            xj = x_values[j]
            if j != i:
                Li *= (x - xj) / (xi - x_values[j])

        # Add Lagrange polynomial Li * yi to the result Polynomial P
        P += yi * Li

    return P


if __name__ == "__main__":
    # Define the points you want the Lagrange interpolation algorithm to use for the polynomial
    # Input points as [[x1, y1], [x2, y2]]
    points = [[1, 4], [3, -3], [7, 21], [8, 4], [11, -13]]

    x_values = []
    y_values = []

    for point in points:
        x_values.append(point[0])
        y_values.append(point[1])

    x_values = numpy.asarray(x_values)
    y_values = numpy.asarray(y_values)

    displayLagrangePolynomial(x_values, y_values)
