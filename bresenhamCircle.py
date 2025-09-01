import matplotlib.pyplot as plt

def draw_circle(x_center, y_center, radius):
    x = 0
    y = radius
    d = 3 - 2 * radius  # Decision parameter

    points = []

    # Function to add symmetric points
    def add_circle_points(x_center, y_center, x, y, points):
        points.extend([
            (x_center + x, y_center + y),
            (x_center - x, y_center + y),
            (x_center + x, y_center - y),
            (x_center - x, y_center - y),
            (x_center + y, y_center + x),
            (x_center - y, y_center + x),
            (x_center + y, y_center - x),
            (x_center - y, y_center - x),
        ])

    # Add the initial points
    add_circle_points(x_center, y_center, x, y, points)

    # Bresenham’s algorithm
    while x < y:
        x += 1
        if d < 0:
            d = d + 4 * x + 6
        else:
            y -= 1
            d = d + 4 * (x - y) + 10
        add_circle_points(x_center, y_center, x, y, points)

    return points


# Plotting function
def plot_circles(radii):
    plt.figure(figsize=(8, 8))
    x_center, y_center = 0, 0

    for radius in radii:
        points = draw_circle(x_center, y_center, radius)
        x_vals, y_vals = zip(*points)  # Extract x and y values
        plt.scatter(x_vals, y_vals, s=1, label=f'Radius {radius}')  # Small dots for each point

    plt.axhline(0, color='black', linewidth=0.5)  # X-axis
    plt.axvline(0, color='black', linewidth=0.5)  # Y-axis
    plt.legend()
    plt.title("Circles Drawn Using Bresenham's Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axis('equal')  # Equal scaling
    plt.grid(True)
    plt.show()


# Draw circles with radii 5, 8, 12, and 20
radii = [5, 8, 12, 20]
plot_circles(radii)