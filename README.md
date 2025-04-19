# Omnidirectional Pure Pursuit Mobile Robot Simulator

This project simulates an omnidirectional mobile robot that can move in any direction, using the Pure Pursuit algorithm to follow a defined path — all built with Python.

![Screenshot 2025-04-19 192722](https://github.com/user-attachments/assets/8e6d1791-8b49-4fb8-8cfc-c9691a5eed8b)


## Fitures
- Omnidirectional robot model (free movement in all directions)
- Pure Pursuit algorithm for target waypoint tracking
- Visualization using matplotlib GUI
- Animated robot motion along the path

## Locomotor Type: Omnidirectional Drive
- Forward/backward
- Sideways (strafe)
- Rotate (optional if implemented)
  
Typical locomotion is achieved using Mecanum wheels or omni-wheels, enabling full 2D translation regardless of orientation.

# Omnidirectional Robot Kinematics

## 1. Kinematic Equations: Omnidirectional Robot

Let:
- \( v_x \): Linear velocity in the X direction
- \( v_y \): Linear velocity in the Y direction
- \( \omega \): Angular velocity (rotation)
- \( r \): Wheel radius
- \( L, W \): Robot's length and width from center to wheels

For a 4-wheel omni/mecanum robot, the wheel velocities can be derived as:
![image](https://github.com/user-attachments/assets/f6ad9c1e-5e89-4e47-b47b-4bc583ca99fa)

Where:
- \( \omega_1 \): Front-left wheel
- \( \omega_2 \): Front-right wheel
- \( \omega_3 \): Rear-left wheel
- \( \omega_4 \): Rear-right wheel

For a non-rotating (pure translation) omnidirectional robot (only \( v_x \) and \( v_y \)), the equations simplify to:

![image](https://github.com/user-attachments/assets/81e2c8bb-43ae-4f6b-96a6-9c49e94e69a9)


## 2. Application in Pure Pursuit

In your simulator, compute the direction to the target (lookahead point):

![image](https://github.com/user-attachments/assets/e00d0d33-9d6c-4fe8-9d31-61cfa1e8c76b)



## Contributors
- (Main Idea) Achmad Yusuf
- Devan yusfa sukmadya
