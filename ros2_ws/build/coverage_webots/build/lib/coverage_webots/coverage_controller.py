import random
import math

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


class CoverageController(Node):

    def __init__(self):
        super().__init__('coverage_controller')

        # Subscribers
        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.odom_sub = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        # Publisher
        self.cmd_pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        # Robot state
        self.front_distance = float("inf")
        self.pose = None

        # Control parameters
        self.obstacle_threshold = 0.8
        self.turning = False
        self.turn_time = 0.0

        # Timer loop (10 Hz)
        self.timer = self.create_timer(0.1, self.control_loop)

    def scan_callback(self, msg):

        ranges = msg.ranges
        center = len(ranges) // 2

        # Take small window in front
        front = ranges[center - 10:center + 10]

        valid = [
            r for r in front
            if not math.isinf(r) and not math.isnan(r)
            ]

        if valid:
            self.front_distance = min(valid)

    def odom_callback(self, msg):
        self.pose = msg.pose.pose

    def control_loop(self):

        cmd = Twist()

        # If obstacle → start turning
        if self.front_distance < self.obstacle_threshold and not self.turning:

            self.turning = True
            self.turn_time = random.uniform(1.0, 2.5)

            self.get_logger().info("Obstacle detected → turning")

        if self.turning:

            cmd.linear.x = 0.0
            cmd.angular.z = random.uniform(0.5, 1.2)

            self.turn_time -= 0.1

            if self.turn_time <= 0:
                self.turning = False

        else:

            cmd.linear.x = 0.3
            cmd.angular.z = random.uniform(-0.1, 0.1)

        self.cmd_pub.publish(cmd)

        self.get_logger().info(
            f"Front distance: {self.front_distance:.2f}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = CoverageController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
