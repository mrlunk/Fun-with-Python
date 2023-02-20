# Pyton script by MrLunk

# project in the make... stand by :P 

from vpython import *

# Constants
G = 6.67430e-11  # gravitational constant
M = {"sun": 1.989e30, "earth": 5.972e24}  # masses of sun and earth
R = {"sun": 0, "earth": 1.496e11}  # distances from sun to earth

# Objects
sun = sphere(pos=vec(R["sun"], 0, 0), radius=6.96e8, texture=textures.sun)
earth = sphere(pos=vec(R["earth"], 0, 0), radius=6.37e6, texture=textures.earth)

# Velocities
v = {"earth": vec(0, 2.9783e4, 0)}

# Simulation loop
while True:
    # Calculate gravitational force on Earth
    r = earth.pos - sun.pos
    F = -G * M["sun"] * M["earth"] * r / mag(r)**3

    # Update Earth's velocity and position
    v["earth"] += F / M["earth"] * 86400
    earth.pos += v["earth"] * 86400

    # Update camera position and orientation
    scene.camera.pos = vec(2*R["earth"], 0, 0)
    scene.camera.axis = -earth.pos

    # Wait for user input
    rate(60)
