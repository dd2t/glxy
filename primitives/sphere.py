from typing import Tuple
from primitives.shapes import circle
from OpenGL.GL import *


def draw_sphere(radius: float, position: Tuple[float, float, float], number_of_circles: int) -> None:
    for i in range(number_of_circles):
        angle = (360 * i) / number_of_circles
        c = circle(radius)

        glPushMatrix()
        glTranslatef(*position)
        glRotatef(angle, 0, 1, 0)

        glBegin(GL_LINE_LOOP)
        for vertex in c[1:]:
            glVertex3fv(vertex)
        glEnd()

        glPopMatrix()
    