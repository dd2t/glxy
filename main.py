from OpenGL.GL import *
from OpenGL.GLUT import *
from glut import Glut
from map import CylinderMap
from player import Player


class Glxy():
    def __init__(self) -> None:
        self.player = Player(initial_position = [0, 0, 0])
        self.map = CylinderMap(
            number_of_circles = 12, 
            big_radius = 16, 
            vertexes_per_circle = 16,
            rotation_speed = 4.0
        )
        self.window_size = (800, 800)
        self.window_name = "GLXY"
        self.z_translation = 18
    

    def display(self) -> None:
        # Clear the color and depth buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # ... render stuff in here
        glPushMatrix()
        self.player.play()
        self.map.draw()
        glPopMatrix()

        # Copy the off-screen buffer to screen
        glutSwapBuffers()
    

    def start(self) -> None:
        glut = Glut(
            self.window_name, 
            self.window_size, 
            self.z_translation
        )
        glut.register_keyboard_handler(self.player.keyboard_handler)
        glut.register_mouse_handler(self.player.mouse_handler)
        glut.run(self.display)


if __name__ == "__main__":
    glxy = Glxy()
    glxy.start()
