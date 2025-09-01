import matplotlib.pyplot as plt

def midpoint_circle(x_center, y_center, radius):
    x = 0
    y = radius
    d = 1 - radius   # Initial decision parameter

    points = []

    # Function to add all 8 symmetric points
    def add_points(xc, yc, x, y):
        return [
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x),
        ]

    points.extend(add_points(x_center, y_center, x, y))

    while x < y:
        x += 1
        if d < 0:
            d = d + 2 * x + 1
        else:
            y -= 1
            d = d + 2 * (x - y) + 1

        points.extend(add_points(x_center, y_center, x, y))

    return points


def plot_circle(x_center, y_center, radius):
    points = midpoint_circle(x_center, y_center, radius)
    x_vals, y_vals = zip(*points)

    plt.figure(figsize=(6, 6))
    plt.scatter(x_vals, y_vals, s=20, color="blue")

    # Draw axes
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)

    plt.title(f"Mid-Point Circle Drawing Algorithm (r = {radius})")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axis("equal")
    plt.grid(True)
    plt.show()


# ---- Example Run ----
if __name__ == "__main__":
    x_center = int(input("Enter circle center X: "))
    y_center = int(input("Enter circle center Y: "))
    radius = int(input("Enter radius: "))

    plot_circle(x_center, y_center, radius)
