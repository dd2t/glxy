from math import sin, cos, pi as PI
from typing import Tuple, List
from utils.cross_multiplication import cross_multiplication as cmap


def circle(radius: float, z_axis: float = 0, number_of_vertexes: int = 16) -> List[Tuple[float, float, float]]:
    N = number_of_vertexes
    r = radius
    # Center of the circle is the first element
    vertexes = [(0, 0, z_axis)]

    for i in range(N+1):
        theta = cmap(i, 0, N, 0, 2*PI)
        x = r * cos(theta)
        y = r * sin(theta)
        vertexes.append((x, y, z_axis))

    return vertexes
