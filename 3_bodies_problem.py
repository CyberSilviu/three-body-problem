import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

# Gravitational constant
G = 1.0

# Masses
m1 = 1.0
m2 = 1.0
m3 = 1.0

# Initial conditions for figure-eight solution
r1_0 = np.array([-0.97000436, 0.24308753])
r3_0 = np.array([0.97000436, -0.24308753])
r2_0 = np.array([0.0, 0.0])
v1_0 = np.array([0.4662036850, 0.4323657300])
v3_0 = np.array([0.4662036850, 0.4323657300])
v2_0 = np.array([-0.93240737, -0.86473146])

# Time parameters
T = 20.0
dt = 0.04
num_steps = int(T / dt)

# Function to calculate the acceleration of each body
def calculate_acceleration(y, t):
    r1, v1, r2, v2, r3, v3 = np.split(y, 6)
    
    d12 = np.linalg.norm(r2 - r1) ** 3
    d23 = np.linalg.norm(r3 - r2) ** 3
    d31 = np.linalg.norm(r1 - r3) ** 3
    d13 = np.linalg.norm(r3 - r1) ** 3
    d21 = np.linalg.norm(r1 - r2) ** 3
    d32 = np.linalg.norm(r2 - r3) ** 3

    a1 = G * m2 * (r2 - r1) / d12 + G * m3 * (r3 - r1) / d13
    a2 = G * m3 * (r3 - r2) / d23 + G * m1 * (r1 - r2) / d21
    a3 = G * m1 * (r1 - r3) / d31 + G * m2 * (r2 - r3) / d32

    return np.concatenate([v1, a1, v2, a2, v3, a3])

# Initial conditions as a flattened array
initial_conditions = np.concatenate([r1_0, v1_0, r2_0, v2_0, r3_0, v3_0])

# Perform the numerical integration using odeint
solution = odeint(calculate_acceleration, initial_conditions, np.linspace(0, T, num_steps))

# Extract the positions of each body from the solution
r1 = solution[:, 0:2]
r2 = solution[:, 4:6]
r3 = solution[:, 8:10]

# Set up the plot
fig, ax = plt.subplots()
lines, = ax.plot([], [], 'o-', markersize=5)  # Change markersize and line style for the trail
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)


# Create separate line objects for each body
line1, = ax.plot([], [], 'o-', markersize=8, label='Body 1')
line2, = ax.plot([], [], 'o-', markersize=7, label='Body 2')
line3, = ax.plot([], [], 'o-', markersize=6, label='Body 3')

lines = [line1, line2, line3]

# Initialize trail data for each body
trail_length = 100  # Adjust the length of the trail
trail_data = np.zeros((trail_length, 3, 3))

# Copy initial positions into trail_data
trail_data[:, 0, :2] = r1_0
trail_data[:, 1, :2] = r2_0
trail_data[:, 2, :2] = r3_0

# Update function for the animation
def update(frame):
    for i, (body) in enumerate([r1, r2, r3]):
        # Update positions of the bodies
        lines[i].set_data(body[frame, 0], body[frame, 1])

        # Update trail data for each body
        trail_data[:-1, i, :] = trail_data[1:, i, :]  # Shift the trail data
        trail_data[-1, i, :2] = [body[frame, 0], body[frame, 1]]  # Add current position to trail

        # Update the trail lines for each body
        lines[i].set_data(trail_data[:, i, 0], trail_data[:, i, 1])

# Create the animation
animation = FuncAnimation(fig, update, frames=num_steps, interval=dt * 1000, blit=False, repeat=False)

# Add legend
ax.legend()

plt.show()

