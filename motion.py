import numpy as np

class BallMotion:
    def __init__(self):
        self.g = -9.81
        self.restitution = 0.8
        self.floor_y = 0
        self.time_step = 0.01
         
    def ball_dynamic(self, state):
        position, velocity, time = state
        # Update velocity due to gravity
        new_velocity = velocity + self.g * self.time_step
        # Calculate new position
        new_position = position + new_velocity * self.time_step
        
        # Check for collision with floor
        if new_position <= self.floor_y:
            # Calculate time of collision
            dt_collision = (self.floor_y - position) / new_velocity if new_velocity < 0 else 0
            # Ensure dt_collision is within the current time step
            if dt_collision > 0 and dt_collision <= self.time_step:
                # Update velocity at collision (perfect reflection)
                new_velocity = -velocity * self.restitution
                # Place exactly at boundary to prevent penetration
                new_position = self.floor_y
                # Prevent extremely small velocities (solves "sticking" problem)
                if abs(new_velocity) < 0.01:
                    new_velocity = 0
        return [new_position, new_velocity, time + self.time_step]
    def projectile(self,state):
        position_x , position_y, vel_x ,vel_y = state
        y_vel = vel_y + self.g*self.time_step
        x_vel = vel_x
        new_position_y = position_y + y_vel * self.time_step
        new_position_x = position_x + vel_x*self.time_step

        if new_position_y <= self.floor_y:
            # Calculate time of collision
            dt_collision = (self.floor_y - position_y) / y_vel if y_vel < 0 else 0
            # Ensure dt_collision is within the current time step
            if dt_collision > 0 and dt_collision <= self.time_step:
                # Update velocity at collision (perfect reflection)
                y_vel = -vel_y * self.restitution
                # Place exactly at boundary to prevent penetration
                new_position_y = self.floor_y
                # Prevent extremely small velocities (solves "sticking" problem)
                if abs(y_vel) < 0.01:
                    y_vel = 0


        return [new_position_x,new_position_y ,x_vel ,y_vel]


        