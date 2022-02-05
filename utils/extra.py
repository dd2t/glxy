from OpenGL.GL import *
from OpenGL.GLUT import *
from primitives.shapes import circle as shape_circle

def draw_cylinder():
    circle1 = shape_circle(0.1)[1:]
    circle2 = shape_circle(10, 4)[1:]

    glBegin(GL_LINE_LOOP)
    for vertex in circle1:
        glVertex3fv(vertex)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for vertex in circle2:
        glVertex3fv(vertex)
    glEnd()

    glBegin(GL_LINES)
    for i in range(-len(circle1), -1):
        glVertex3fv(circle1[i])
        glVertex3fv(circle2[i+1])
    glEnd()
