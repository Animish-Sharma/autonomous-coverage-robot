import math
import random
import numpy as np

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry, OccupancyGrid


class CoverageController(Node):

    def __init__(self):

        super().__init__('coverage_controller')

        # subscribers
        self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.create_subscription(OccupancyGrid, '/map', self.map_callback, 10)

        # publisher
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        # robot pose
        self.robot_x = 0.0
        self.robot_y = 0.0
        self.robot_yaw = 0.0

        # lidar
        self.front_distance = float("inf")

        # map
        self.map = None

        # frontier goal
        self.goal = None

        # parameters
        self.obstacle_threshold = 0.35
        self.goal_reached_dist = 0.4

        self.timer = self.create_timer(0.1, self.control_loop)

    # ------------------------
    # LIDAR
    # ------------------------

    def scan_callback(self, msg):

        ranges = msg.ranges
        center = len(ranges) // 2

        front = ranges[center-20:center+20]

        valid = []

        for r in front:

            if math.isnan(r):
                continue

            if math.isinf(r):
                continue

            if r < 0.05:
                continue

            valid.append(r)

        if valid:
            self.front_distance = min(valid)
        else:
            self.front_distance = float("inf")

    # ------------------------
    # ODOM
    # ------------------------

    def odom_callback(self, msg):

        pose = msg.pose.pose

        self.robot_x = pose.position.x
        self.robot_y = pose.position.y

        q = pose.orientation

        siny = 2 * (q.w*q.z + q.x*q.y)
        cosy = 1 - 2 * (q.y*q.y + q.z*q.z)

        self.robot_yaw = math.atan2(siny, cosy)

    # ------------------------
    # MAP
    # ------------------------

    def map_callback(self, msg):

        self.map = msg

        if self.goal is None:

            frontiers = self.detect_frontiers(msg)

            if frontiers:

                self.goal = self.select_frontier(frontiers)

                if self.goal:
                    self.get_logger().info(
                        f"New frontier goal: {self.goal}"
                    )

    # ------------------------
    # FRONTIER DETECTION
    # ------------------------

    def detect_frontiers(self, map_msg):

        width = map_msg.info.width
        height = map_msg.info.height

        grid = np.array(map_msg.data).reshape((height, width))

        frontiers = []

        for y in range(1, height-1):
            for x in range(1, width-1):

                if grid[y, x] == 0:

                    neighbors = [
                        grid[y+1, x],
                        grid[y-1, x],
                        grid[y, x+1],
                        grid[y, x-1]
                    ]

                    if -1 in neighbors:
                        frontiers.append((x, y))

        return frontiers

    # ------------------------
    # FRONTIER SELECTION
    # ------------------------

    def select_frontier(self, frontiers):

        resolution = self.map.info.resolution
        origin = self.map.info.origin.position

        best = None
        best_dist = float("inf")

        for f in frontiers:

            wx = origin.x + f[0]*resolution
            wy = origin.y + f[1]*resolution

            dx = wx - self.robot_x
            dy = wy - self.robot_y

            dist = math.sqrt(dx*dx + dy*dy)

            if dist < 1.0:
                continue

            if dist < best_dist:
                best_dist = dist
                best = (wx, wy)

        return best

    # ------------------------
    # CONTROL LOOP
    # ------------------------

    def control_loop(self):

        cmd = Twist()

        # obstacle avoidance
        if self.front_distance < self.obstacle_threshold:

            cmd.angular.z = 0.6
            cmd.linear.x = 0.0

            self.cmd_pub.publish(cmd)
            return

        # if no goal
        if self.goal is None:

            cmd.linear.x = 0.2
            cmd.angular.z = random.uniform(-0.3, 0.3)

            self.cmd_pub.publish(cmd)
            return

        gx, gy = self.goal

        dx = gx - self.robot_x
        dy = gy - self.robot_y

        dist = math.sqrt(dx*dx + dy*dy)

        # reached goal
        if dist < self.goal_reached_dist:

            self.get_logger().info("Frontier reached")

            self.goal = None
            return

        target_angle = math.atan2(dy, dx)

        angle_error = target_angle - self.robot_yaw
        angle_error = math.atan2(
            math.sin(angle_error),
            math.cos(angle_error)
        )

        # rotate
        if abs(angle_error) > 0.2:

            cmd.angular.z = 0.5 * angle_error
            cmd.linear.x = 0.0

        # move forward
        else:

            cmd.linear.x = 0.3
            cmd.angular.z = 0.0

        self.cmd_pub.publish(cmd)


def main(args=None):

    rclpy.init(args=args)

    node = CoverageController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
