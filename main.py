from OpenGL.GL import *
from OpenGL.GLUT import *
from glut import Glut
from map import CylinderMap
from player import Player

    
player_pos = [0, 0, 0]

# def mouse_handler(x, y):
#     mag = ((x - 400)**2 + (y - 400)**2)**(1/2)
#     normalized_mouse = (-(x-400)/mag, (y-400)/mag)
#     global player_pos
#     player_pos[0] +=  normalized_mouse[0] / 10
#     player_pos[1] +=  normalized_mouse[1] / 10
#     print(normalized_mouse)


# def process_normal_keys(key: str, mouse_x: int, mouse_y: int):
#     # print(str(key))
#     if (key == b'\x1b'):
#         glutLeaveMainLoop()


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
        # glTranslate(*player_pos)
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
        # glut.register_keyboard_handler(process_normal_keys)
        # glut.register_mouse_handler(mouse_handler)
        glut.register_keyboard_handler(self.player.keyboard_handler)
        glut.register_mouse_handler(self.player.mouse_handler)
        glut.run(self.display)


if __name__ == "__main__":
    glxy = Glxy()
    glxy.start()
