import matplotlib.pyplot as plt

def dda_line_with_grid(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    m = dy / dx if dx != 0 else float('inf')

    x_points, y_points = [], []

    # Case 1: |slope| <= 1 → step in x
    if abs(m) <= 1:
        if x1 > x2:  # ensure left to right
            x1, y1, x2, y2 = x2, y2, x1, y1
        x, y = x1, y1
        while x <= x2:
            x_points.append(round(x))
            y_points.append(round(y))
            x += 1
            y += m

    # Case 2: |slope| > 1 → step in y
    else:
        if y1 > y2:  # ensure bottom to top
            x1, y1, x2, y2 = x2, y2, x1, y1
        x, y = x1, y1
        while y <= y2:
            x_points.append(round(x))
            y_points.append(round(y))
            y += 1
            x += 1 / m

    # ---- Plotting ----
    plt.figure(figsize=(6,6))

    # Draw grid
    plt.grid(True, which='both')
    plt.xticks(range(min(x1, x2) - 2, max(x1, x2) + 3))
    plt.yticks(range(min(y1, y2) - 2, max(y1, y2) + 3))

    # Draw ideal line (red)
    plt.plot([x1, x2], [y1, y2], color='red')

    # Draw selected pixels (black dots)
    plt.scatter(x_points, y_points, color='black', s=50)

    plt.title("DDA Line Drawing (with Grid)")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


# ---- Example Run ----
dda_line_with_grid(2, 3, 12, 8)
