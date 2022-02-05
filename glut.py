from typing import List, Tuple, Callable
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Glut():

    def __init__(self, argv: List[str], window_name: str, window_size: Tuple[int, int],
    z_translation: int) -> None:
        self.argv = argv
        self.window_name = window_name
        self.window_size = window_size
        self.z_translation = z_translation


    def run(self, draw: Callable[[None], None]) -> None:
        glutInit(self.argv)

        # Create a double-buffer RGBA window. (Single-buffering is possible)
        # So is creating an index-mode windows.)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH | GLUT_MULTISAMPLE)

        # Create a window, setting its title
        glutInitWindowSize(*self.window_size)
        glutCreateWindow(self.window_name)

        # Sets the display callback. You can set other callbacks for keyboard and
        # mouse events.
        glutDisplayFunc(draw)

        glEnable(GL_MULTISAMPLE)
        glEnable(GL_DEPTH_TEST)
        perspective_ratio = float(self.window_size[0]/self.window_size[1])
        gluPerspective(45, perspective_ratio, 1, 1000)
        glTranslatef(0, 0, -self.z_translation)
        glutTimerFunc(50, self.timer, 1)

        # Run the GLUT main loop untiç the user closes the window.
        glutMainLoop()

    def timer(self, i) -> None:
        glutPostRedisplay()
        glutTimerFunc(50, self.timer, 1)
