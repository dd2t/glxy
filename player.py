from typing import List
from OpenGL.GL import *
from OpenGL.GLUT import *
from utils.cross_multiplication import cross_multiplication as cmult


class Player():

    def __init__(self, initial_position: List[float]) -> None:
        self.position = initial_position
        self.rotation = (0, 0, 0, 0)
    

    def play(self) -> None:
        glTranslate(*self.position)
        # glRotatef(*self.rotation)
    

    def keyboard_handler(self, key: str, mouse_x: int, mouse_y: int) -> None:
        if (key == b'\x1b'):
            glutLeaveMainLoop()


    def mouse_handler(self, x: int, y: int) -> None:
        window_length = 400
        window_height = 400
        velocity_limiter = 10

        mag = ((x - window_length)**2 + (y - window_height)**2)**(1/2)
        normalized_mouse = [-(x-window_length)/mag, (y-window_height)/mag, 0]
        self.position = [(axis + (n_mov / velocity_limiter)) for axis, n_mov in zip(self.position, normalized_mouse)]

        # omega = cmult(mag, 0, 1000, 0, 20)
        # for i in range(2):
        #     if normalized_mouse[i] == 0:
        #         normalized_mouse[i] = 0.001
        # self.rotation = (omega, normalized_mouse[0] / (normalized_mouse[0]**2)**(1/2), normalized_mouse[1] / (normalized_mouse[1]**2)**(1/2), 0)
        # print(mag)
