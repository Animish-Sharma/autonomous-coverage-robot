# Autonomous Coverage Robot

This repository contains the implementation and experimental artifacts for the IRPP course project **“Optimized Area Coverage for an Autonomous Mobile Robot.”**

Autonomous robots operating in unknown environments must efficiently explore the surroundings while avoiding obstacles and minimizing repeated visits to previously explored regions. This project investigates the **coverage problem** by implementing and evaluating multiple exploration strategies for a mobile robot in simulation.

The system is implemented using **ROS2** and simulated using **Webots** with a TurtleBot3 robot equipped with a **2D LiDAR sensor**. Three exploration strategies were developed and compared:

- Random exploration
- Zig-zag systematic coverage
- Frontier-based exploration

Coverage performance is evaluated using a grid-based coverage tracker that records visited cells and logs coverage statistics over time.

---

## What this repository contains

This repository includes:

- ROS2 controllers implementing the exploration strategies
- A Webots simulation world used for testing the robot
- Experimental results including coverage logs and plots
- The final project report

---

## Running the project

To run the exploration system locally, you need **ROS2** and **Webots** installed.

### 1. Clone the repository
```
git clone https://github.com/Animish-Sharma/autonomous-coverage-robot.git
cd autonomous-coverage-robot
```

### 2. Build the ROS2 workspace
```
cd ros2_ws
colcon build
```

### 3. Source the workspace
```
source install/setup.bash
```
or
```
source install/setup.zsh
```

### 4. Launch the simulation
```
ros2 launch coverage_webots project_launch.py
```

This will start the Webots simulation and run the exploration controller.

---

## Results

Coverage statistics and evaluation plots used in the project are available in the **results/** directory.

The final report describing the system design and experimental evaluation is included as **report.pdf**.

---

## Authors

[Shriya Kansal](https://github.com/Shr1yaK) 
[Animish Sharma](https://github.com/Animish-Sharma) 

IRPP – IIIT Hyderabad