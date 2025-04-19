import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set awal posisi dan lintasan
path = np.array([
    [0, 0],
    [1, 2],
    [3, 4],
    [6, 5],
    [8, 8]
])

lookahead_distance = 1.0
robot_pos = np.array([0.0, 0.0])
robot_path = [robot_pos.copy()]
target_index = 0
robot_speed = 0.1

def find_lookahead_point(robot_pos, path, lookahead_distance):
    for i in range(len(path) - 1):
        start = path[i]
        end = path[i + 1]
        d = end - start
        f = start - robot_pos
        a = np.dot(d, d)
        b = 2 * np.dot(f, d)
        c = np.dot(f, f) - lookahead_distance ** 2
        discriminant = b ** 2 - 4 * a * c
        if discriminant >= 0:
            discriminant = np.sqrt(discriminant)
            t1 = (-b - discriminant) / (2 * a)
            t2 = (-b + discriminant) / (2 * a)
            if 0 <= t2 <= 1:
                return start + t2 * d
    return path[-1]

def update(frame):
    global robot_pos
    lookahead_point = find_lookahead_point(robot_pos, path, lookahead_distance)
    direction = lookahead_point - robot_pos
    distance = np.linalg.norm(direction)
    if distance < 0.01:
        return
    direction /= distance
    robot_pos[:] += direction * robot_speed
    robot_path.append(robot_pos.copy())

    ax.clear()
    ax.plot(path[:, 0], path[:, 1], 'r--', label="Path")
    ax.plot(*zip(*robot_path), 'b-', label="Robot Path")
    ax.plot(robot_pos[0], robot_pos[1], 'go', label="Robot")
    ax.plot(lookahead_point[0], lookahead_point[1], 'mo', label="Lookahead")
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.legend()
    ax.set_title("Omnidirectional Robot Pure Pursuit")

fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, interval=100)
plt.show()
