import sys
from math import sqrt

from visualize import Point, clear, show, draw_triangle, save

def midpoint(p: Point, q: Point) -> Point:
    """Return the midpoint between two points."""
    x = (p[0] + q[0]) / 2
    y = (p[1] + q[1]) / 2
    return (x, y)

def sierpinski(a: Point, b: Point, c: Point, depth: int) -> None:
    """
    Recursively draw a Sierpinski triangle.
    """

    if depth == 0:
        draw_triangle(a, b, c)
        return

    ab = midpoint(a, b)
    bc = midpoint(b, c)
    ca = midpoint(c, a)

    # Bottom-left triangle
    sierpinski(a, ab, ca, depth - 1)

    # Bottom-right triangle
    sierpinski(ab, b, bc, depth - 1)

    # Top triangle
    sierpinski(ca, bc, c, depth - 1)

if __name__ == "__main__":
    depth = int(sys.argv[1]) if len(sys.argv) > 1 else 5

    side = 1.0
    a = (0.0, 0.0)
    b = (side, 0.0)
    c = (side / 2, side * sqrt(3) / 2)

    clear()
    sierpinski(a, b, c, depth)
    show(f"Sierpinski triangle, depth {depth}")
    save(f"Sierpinski triangle, depth {depth}", f"triangle_{depth}.png")
