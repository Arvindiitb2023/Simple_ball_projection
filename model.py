from PyQt6.QtOpenGLWidgets import QOpenGLWidget 
from PyQt6.QtCore import QTimer # Correct import for PyQt6
from OpenGL.GL import *
import math
class OpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(800,600)
        self.state = [0,6,0]

    def initializeGL(self):
            glClearColor(1, 1, 1, 1)  # White background
            glEnable(GL_LINE_SMOOTH)  # Anti-aliasing
    def resizeGL(self, w, h):
        """ Adjust viewport and projection """
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-3, 3, -2, 2, -1, 1)  # Set coordinate system
        glMatrixMode(GL_MODELVIEW)
    def paintGL(self):
         
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        # glTranslatef(0, -self.state[0], 0)
        glPushMatrix()  # Save the current transformation state
        glTranslatef(self.state[0], self.state[1], 0)
        self.draw_circle(-3, 0, 0.1, 100)
        glPopMatrix()
        
        glColor3f(0, 0, 0)
        glBegin(GL_LINES)
        glVertex2f(-3, -0.1)
        glVertex2f(3, -0.1)
        glEnd()

    
    def draw_circle(self, cx, cy, radius, num_segments):
        """Draw a filled circle using GL_TRIANGLE_FAN"""
        # glTranslatef(0, self.state[0], 0)
        glColor3f(1.0, 0.0, 0.0)  # Set color to red
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(cx, cy)  # Center of the circle
        for i in range(num_segments + 1):
            angle = 2.0 * math.pi * i / num_segments
            x = cx + math.cos(angle) * radius
            y = cy + math.sin(angle) * radius
            glVertex2f(x, y)
        glEnd()