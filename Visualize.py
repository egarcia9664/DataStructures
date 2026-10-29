"""
visualize.py -- the drawing layer.
 
a tiny drawing API that other code can call:
    
    draw_line(p, q)   record a line segment from point p to point q
    show(title)      display everything drawn so far
    clear()          forget everything drawn so far
 
draw_line() just collects segments; show() renders them all at once with
matplotlib, which is much faster than plotting each segment separately.
"""
 
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
 
Point = tuple[float, float]
 
_segments: list[tuple[Point, Point]] = []
 
def draw_triangle(a: Point, b: Point, c: Point) -> None:
    """Outline the triangle abc using draw_line()."""
    draw_line(a, b)
    draw_line(b, c)
    draw_line(c, a)

 
def draw_line(p: Point, q: Point) -> None:
    """Draw a line segment from point p to point q."""
    _segments.append((p, q))
 
 
def clear() -> None:
    """Remove all segments drawn so far."""
    _segments.clear()
 
 
def show(title: str = "") -> None:
    """Render every segment recorded by draw_line() in one window."""
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.add_collection(LineCollection(_segments, colors="tab:blue", linewidths=0.8))
    ax.set_aspect("equal")
    ax.autoscale_view()
    ax.axis("off")
    ax.set_title(title)
    plt.show()

def save(title: str = "", filename = "img.png") -> None:
    """Render every segment recorded by draw_line() in one window and save."""
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.add_collection(LineCollection(_segments, colors="tab:blue", linewidths=0.8))
    ax.set_aspect("equal")
    ax.autoscale_view()
    ax.axis("off")
    ax.set_title(title)
    plt.savefig(filename)
