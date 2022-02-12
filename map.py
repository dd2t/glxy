from typing import List, Tuple
from OpenGL.GL import *
from OpenGL.GLUT import *
from primitives.shapes import circle as shape_circle
from utils.cross_multiplication import cross_multiplication as cm
from primitives.sphere import draw_sphere


class CylinderMap():

    def __init__(self, number_of_circles: int, big_radius: float, 
    vertexes_per_circle: int = 16, rotation_speed: float = 4.0) -> None:
    
        self.number_of_circles = number_of_circles
        self.big_radius = big_radius
        self.vertexes_per_circle = vertexes_per_circle
        # self.circles = None
        self.current_rotation_speed = 0
        self.rotation_speed = rotation_speed

        circles = list()
        # Create list of circles in the cylinder
        for i in range(number_of_circles):
            r = big_radius - (big_radius * i) / number_of_circles
            z_pos = (number_of_circles - i**2) + 4
            # if i == 0:
            #     print(z_pos)
            circles.append(shape_circle(r, z_pos, vertexes_per_circle))
        self.circles = circles


    def draw(self) -> None:
        glPushMatrix()
        glRotatef(self.current_rotation_speed, 0, 0, 1)
        
        number_of_circles = self.number_of_circles
        big_radius = self.big_radius
        vertexes_per_circle = self.vertexes_per_circle
        circles = self.circles

        # Draw first ring
        glBegin(GL_LINE_LOOP)
        for vertex in circles[-1][1:]:
            glVertex3fv(vertex)
        glEnd()
        
        # Draw a line from vertex i of circle i
        # to the verter i+1 of circle i+1
        for j in range(len(circles) -1):
            glBegin(GL_LINES)
            for i in range(1, len(circles[j]) -1):
                glVertex3fv(circles[j][i])
                glVertex3fv(circles[j+1][i+1])
            glEnd()

        # Draw ring that grow over time
        v_rings = self._velocity_rings()
        for ring in v_rings:
            glBegin(GL_LINE_LOOP)
            for vertex in ring[1:]:
                glVertex3fv(vertex)
            glEnd()

        # Enemy
        self.enemy()
        
        self.current_rotation_speed += self.rotation_speed
        glPopMatrix()

    
    def _velocity_rings(self) -> List[Tuple[float]]:
        rings = list()
        MOD = 2
        number_of_rings = self.number_of_circles

        # Get time
        current_time = int(glutGet(GLUT_ELAPSED_TIME)) / 600
        residue = current_time % MOD

        # Min and max
        r_min = self.circles[-1][1][0] - self.circles[-1][0][0]
        r_max = self.circles[0][1][0] - self.circles[0][0][0]
        z_min = self.circles[-1][0][2]
        z_max = self.circles[0][0][2]

        for i in range(1, 3):
            res = residue - (residue * i**(1/2)) / (number_of_rings // 2)

            # Circle that grows over time
            r = cm(res, 0, MOD - 1, r_min, r_max)
            z = cm(res, 0, MOD - 1, z_min, z_max)
            rings.append(shape_circle(r, z, self.vertexes_per_circle))

        return rings
    

    def enemy(self):
        MOD = 8
        number_of_rings = self.number_of_circles

        # Get time
        current_time = int(glutGet(GLUT_ELAPSED_TIME)) / 600
        residue = current_time % MOD

        # Min and max
        r_min = (self.circles[-1][1][0] - self.circles[-1][0][0]) / 8
        r_max = (self.circles[0][1][0] - self.circles[0][0][0]) / 8
        z_min = self.circles[-1][0][2]
        z_max = self.circles[0][0][2]

        res = residue

        # Circle that grows over time
        r = cm(res, 0, MOD - 1, r_min, r_max)
        z = cm(res, 0, MOD - 1, z_min, z_max)
        # rings.append(shape_circle(r, z, self.vertexes_per_circle))

        glPushMatrix()
        # glRotatef(self.current_rotation_speed, 0, 1, 0)
        draw_sphere(r, (0, 0, z), 24)
        glPopMatrix()
