from typing import List, Tuple, Callable
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


class Glut():

    def __init__(self, window_name: str, window_size: Tuple[int, int],
    z_translation: int) -> None:
        self.argv = sys.argv
        self.window_name = window_name
        self.window_size = window_size
        self.z_translation = z_translation
        self.normal_keyboard_handler = None
        self.mouse_handler = None


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
        if self.normal_keyboard_handler is not None:
            glutKeyboardFunc(self.normal_keyboard_handler)
        if self.mouse_handler is not None:
            glutPassiveMotionFunc(self.mouse_handler)

        glEnable(GL_MULTISAMPLE)
        glEnable(GL_DEPTH_TEST)
        perspective_ratio = float(self.window_size[0]/self.window_size[1])
        gluPerspective(45, perspective_ratio, 1, 1000)
        glTranslatef(0, 0, -self.z_translation)
        glutTimerFunc(50, self._timer, 1)

        # Run the GLUT main loop untiç the user closes the window.
        glutMainLoop()


    def _timer(self, i) -> None:
        glutPostRedisplay()
        glutTimerFunc(50, self._timer, 1)
    

    def register_keyboard_handler(self, handler: Callable[[str, int, int], None]) -> None:
        self.normal_keyboard_handler = handler
    
    def register_mouse_handler(self, handler: Callable[[str, str, int, int], None]) -> None:
        self.mouse_handler = handler
        # glutMouseFunc(mouse)
