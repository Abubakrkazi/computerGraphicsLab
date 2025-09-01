import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    x_points = []
    y_points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 > x1 else -1  # Step direction for x
    sy = 1 if y2 > y1 else -1  # Step direction for y

    x, y = x1, y1

    if dx > dy:
        d = 2 * dy - dx
        while x != x2:
            x_points.append(x)
            y_points.append(y)
            if d < 0:
                d += 2 * dy
            else:
                y += sy
                d += 2 * (dy - dx)
            x += sx
    else:
        d = 2 * dx - dy
        while y != y2:
            x_points.append(x)
            y_points.append(y)
            if d < 0:
                d += 2 * dx
            else:
                x += sx
                d += 2 * (dx - dy)
            y += sy

    x_points.append(x2)
    y_points.append(y2)

    # Plot
    plt.figure(figsize=(6, 6))
    plt.plot(x_points, y_points, 'bo')  # blue dots
    plt.plot([x1, x2], [y1, y2], 'r--')  # red reference line
    for i in range(len(x_points)):
        plt.gca().add_patch(plt.Rectangle((x_points[i] - 0.5, y_points[i] - 0.5), 1, 1, color='yellow', alpha=0.3))
    plt.grid(True)
    plt.gca().set_aspect('equal')
    plt.title("Bresenham’s Line Algorithm (Negative Slope)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
# Example: Positive slope
bresenham_line(0, 0, 8, 5)