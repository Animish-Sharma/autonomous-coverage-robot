import numpy as np
from controller import Supervisor

robot = Supervisor()
timestep = int(robot.getBasicTimeStep())

# ==============================
# LIDAR
# ==============================

lidar = robot.getDevice("LDS-01")
lidar.enable(timestep)

resolution = lidar.getHorizontalResolution()
max_range = lidar.getMaxRange()

print("Directional Controller Enabled")
print("Resolution:", resolution)

# ==============================
# MOTORS
# ==============================

left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

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
turn_direction = 1  # +1 = left, -1 = right

ENTER_THRESHOLD = 0.45
EXIT_THRESHOLD = 0.65

clear_counter = 0
CLEAR_REQUIRED = 8

step_count = 0

# ==============================
# MAIN LOOP
# ==============================

while robot.step(timestep) != -1:

    # ---- Position Tracking ----
    position = node.getPosition()
    x, y = position[0], position[1]

    grid_index = position_to_grid(x, y)
    if grid_index is not None:
        coverage_grid[grid_index] = 1

    # ---- LIDAR PROCESSING ----
    ranges = lidar.getRangeImage()

    # Define sectors
    center = resolution // 2
    front_width = resolution // 8
    side_width = resolution // 6

    # Front sector
    front = ranges[center - front_width : center + front_width]

    # Left sector
    left = ranges[center + front_width : center + front_width + side_width]

    # Right sector
    right = ranges[center - front_width - side_width : center - front_width]

    # Filter invalid values
    front_valid = [r for r in front if 0.01 < r < max_range]
    left_valid  = [r for r in left  if 0.01 < r < max_range]
    right_valid = [r for r in right if 0.01 < r < max_range]

    front_min = min(front_valid) if front_valid else max_range
    left_avg  = np.mean(left_valid) if left_valid else max_range
    right_avg = np.mean(right_valid) if right_valid else max_range

    # ==============================
    # STATE TRANSITIONS
    # ==============================

    if state == STATE_FORWARD:
        if front_min < ENTER_THRESHOLD:
            state = STATE_TURNING
            clear_counter = 0

            # Choose direction toward more open side
            if left_avg > right_avg:
                turn_direction = 1   # turn left
                print("Obstacle Ahead → Turning LEFT")
            else:
                turn_direction = -1  # turn right
                print("Obstacle Ahead → Turning RIGHT")

    elif state == STATE_TURNING:

        if front_min > EXIT_THRESHOLD:
            clear_counter += 1
        else:
            clear_counter = 0

        if clear_counter > CLEAR_REQUIRED:
            state = STATE_FORWARD
            print("Path Clear → Forward")

    # ==============================
    # MOTOR CONTROL
    # ==============================

    if state == STATE_FORWARD:
        left_motor.setVelocity(BASE_SPEED)
        right_motor.setVelocity(BASE_SPEED)

    else:  # TURNING
        left_motor.setVelocity(TURN_SPEED * turn_direction)
        right_motor.setVelocity(-TURN_SPEED * turn_direction)

    # ==============================
    # COVERAGE REPORT
    # ==============================

    step_count += 1
    if step_count % 40 == 0:
        covered = np.sum(coverage_grid)
        total = GRID_CELLS * GRID_CELLS
        percent = (covered / total) * 100
        print("Coverage:", round(percent, 2), "%")