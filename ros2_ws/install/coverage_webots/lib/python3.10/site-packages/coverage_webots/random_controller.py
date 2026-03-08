import math
import random

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class RandomExplorer(Node):

    def __init__(self):

        super().__init__('random_explorer')

        self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)

        self.cmd_pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            10)

        self.front_distance = float("inf")

        self.timer = self.create_timer(
            0.1,
            self.control_loop)

    # ---------------------

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

    # ---------------------

    def control_loop(self):

        cmd = Twist()

        # obstacle avoidance
        if self.front_distance < 0.6:

            cmd.linear.x = 0.0
            cmd.angular.z = random.uniform(0.5,1.2)

        else:

            cmd.linear.x = 0.3
            cmd.angular.z = random.uniform(-0.4,0.4)

        self.cmd_pub.publish(cmd)


def main(args=None):

    rclpy.init(args=args)

    node = RandomExplorer()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
