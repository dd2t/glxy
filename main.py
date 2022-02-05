import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from glut import Glut
from map import CylinderMap

    
omega = 0
def display() -> None:
    # Clear the color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Instances
    map = CylinderMap(8, 10, 16)

    # ... render stuff in here
    # It will go to an off-screen frame buffer
    glPushMatrix()
    global omega
    # glTranslatef(4, 0, 0)
    # glRotatef(40, 1, 0, 0)
    glRotatef(omega, 0, 0, 1)
    map.draw()
    omega += 4
    glPopMatrix()

    # Copy the off-screen buffer to screen
    glutSwapBuffers()


def main() -> None:
    glut = Glut(sys.argv, "GLXY", (800, 800), 20)
    glut.run(display)


if __name__ == "__main__":
    main()
