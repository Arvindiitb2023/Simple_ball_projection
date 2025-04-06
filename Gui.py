from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtOpenGLWidgets import QOpenGLWidget  # Correct import for PyQt6
import sys
from OpenGL.GL import *
from PyQt6.QtCore import QThread, pyqtSignal, Qt
import numpy as np
from model import OpenGLWidget
from motion import BallMotion

class SimulationThread(QThread):
    update_signal = pyqtSignal(object)
    def __init__(self,motion , object):
        super().__init__()
        self.object = object
        self.motion = motion
        self.running = True  # Control flag
    def run(self):
        while self.running:
            new_state = self.motion.projectile(self.object.state)
            self.update_signal.emit(new_state)
            self.msleep(50)
    def stop(self):
        self.running = False



class InvertedPendulam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.object = OpenGLWidget(self)
        
        container = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.object)
        container.setLayout(main_layout) 
        self.setCentralWidget(container)
        theta = np.pi/3
        vel_x = 5*np.cos(theta)
        vel_y = 5*np.sin(theta)
        self.state = [0,0,vel_x ,vel_y]
        self.intial()
        self.motion = BallMotion()
        self.simulation_thread = SimulationThread(self.motion, self.object)
        self.simulation_thread.update_signal.connect(self.update_motion)
    def intial(self):
        self.object.state = self.state
        self.object.update()
    def update_motion(self,new_state):
        self.object.state = new_state
        self.object.update()
    def keyPressEvent(self, event):
        key = event.key()
        if key == 87:
            if not self.simulation_thread.isRunning():
                self.simulation_thread.start()   
        self.object.update()
    




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InvertedPendulam()
    window.show()
    sys.exit(app.exec())  