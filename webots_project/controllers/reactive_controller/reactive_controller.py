import numpy as np
from controller import Supervisor

robot = Supervisor()
timestep = int(robot.getBasicTimeStep())

# ==============================
# LIDAR SETUP
# ==============================

lidar = robot.getDevice("LDS-01")
lidar.enable(timestep)

resolution = lidar.getHorizontalResolution()
max_range = lidar.getMaxRange()

print("LiDAR enabled")
print("Resolution:", resolution)
print("Max range:", max_range)

# ==============================
# MOTORS
# ==============================

left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

BASE_SPEED = 4.0
TURN_SPEED = 2.5

# ==============================
# COVERAGE GRID
# ==============================

GRID_RESOLUTION = 0.1
WORLD_SIZE = 5.0
GRID_CELLS = int(WORLD_SIZE / GRID_RESOLUTION)

coverage_grid = np.zeros((GRID_CELLS, GRID_CELLS))

node = robot.getSelf()

def position_to_grid(x, y):
    i = int((x + WORLD_SIZE/2) / GRID_RESOLUTION)
    j = int((y + WORLD_SIZE/2) / GRID_RESOLUTION)
    if 0 <= i < GRID_CELLS and 0 <= j < GRID_CELLS:
        return i, j
    return None

# ==============================
# STATE MACHINE
# ==============================

STATE_FORWARD = 0
STATE_TURNING = 1

state = STATE_FORWARD

OBSTACLE_THRESHOLD = 0.45

step_count = 0

# ==============================
# MAIN LOOP
# ==============================

while robot.step(timestep) != -1:

    # ---- POSITION TRACKING ----
    position = node.getPosition()
    x, y = position[0], position[1]

    grid_index = position_to_grid(x, y)
    if grid_index is not None:
        coverage_grid[grid_index] = 1

    # ---- LIDAR PROCESSING ----
    ranges = lidar.getRangeImage()

    center = resolution // 2
    width = resolution // 12

    front_ranges = ranges[center - width : center + width]
    valid_ranges = [r for r in front_ranges if 0.01 < r < max_range]

    if len(valid_ranges) > 0:
        min_distance = min(valid_ranges)
    else:
        min_distance = max_range

    # ---- STATE TRANSITIONS ----

    if state == STATE_FORWARD:
        if min_distance < OBSTACLE_THRESHOLD:
            state = STATE_TURNING
            print("STATE → TURNING")

    elif state == STATE_TURNING:
        if min_distance > OBSTACLE_THRESHOLD:
            state = STATE_FORWARD
            print("STATE → FORWARD")

    # ---- MOTION CONTROL ----

    if state == STATE_FORWARD:
        left_motor.setVelocity(BASE_SPEED)
        right_motor.setVelocity(BASE_SPEED)

    elif state == STATE_TURNING:
        left_motor.setVelocity(TURN_SPEED)
        right_motor.setVelocity(-TURN_SPEED)

    # ---- COVERAGE PRINT ----

    step_count += 1
    if step_count % 40 == 0:
        covered = np.sum(coverage_grid)
        total = GRID_CELLS * GRID_CELLS
        percent = (covered / total) * 100
        print("Coverage:", round(percent, 2), "%")