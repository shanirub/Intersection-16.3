import matplotlib.pyplot as plt


# for two points (x1, y1) (x2, y2) returns a and b from equation y=ax+b
def find_equation(x1, y1, x2, y2) -> tuple[float, float]:
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1
    return a, b


def are_parallel(a1, a2) -> bool:
    return a1 == a2


def find_intersection(x1, y1, x2, y2, x3, y3, x4, y4) -> tuple[float, float]:
    a1, b1 = find_equation(x1, y1, x2, y2)
    a2, b2 = find_equation(x3, y3, x4, y4)

    if are_parallel(a1, a2):     # check to see if parallel
        raise ValueError

    intersection_x = (b2 - b1) / (a1 - a2)

    if x1 <= intersection_x <= x2 and x3 <= intersection_x <= x4:
        intersection_y = intersection_x * a1 + b1
        return intersection_x, intersection_y

    raise ValueError


if __name__ == '__main__':
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    x3 = int(input("x3: "))
    y3 = int(input("y3: "))
    x4 = int(input("x4: "))
    y4 = int(input("y4: "))

    x_values = ([x1, x2], [x3, x4])
    y_values = ([y1, y2], [y3, y4])

    plt.plot(x_values[0], y_values[0], label="line 1")
    plt.plot(x_values[1], y_values[1], label="line 2")

    try:
        a = find_intersection(x1, y1, x2, y2, x3, y3, x4, y4)
        print("point of intersection: (" + str(a[0]) + ", " + str(a[1]) + ")")
    except ValueError:
        print(" no intersection (either the lines are parallel, or the intersection point is outside the x range)")

    plt.show()


