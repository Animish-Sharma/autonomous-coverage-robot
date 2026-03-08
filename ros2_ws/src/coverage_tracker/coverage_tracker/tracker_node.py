import rclpy
from rclpy.node import Node

from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import Odometry

import numpy as np


class CoverageTracker(Node):

    def __init__(self):

        super().__init__('coverage_tracker')

        self.map = None
        self.covered = None

        self.map_sub = self.create_subscription(
            OccupancyGrid,
            '/map',
            self.map_callback,
            10)

        self.odom_sub = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10)

    def map_callback(self, msg):

        if self.map is None:

            width = msg.info.width
            height = msg.info.height

            self.covered = np.zeros((height, width))

            self.map = msg

            self.get_logger().info("Coverage grid initialized")

    def odom_callback(self, msg):

        if self.map is None:
            return

        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        resolution = self.map.info.resolution
        origin = self.map.info.origin.position

        grid_x = int((x - origin.x) / resolution)
        grid_y = int((y - origin.y) / resolution)

        if 0 <= grid_x < self.map.info.width and 0 <= grid_y < self.map.info.height:

            self.covered[grid_y, grid_x] = 1

        coverage = np.sum(self.covered) / self.covered.size

        self.get_logger().info(f'Coverage: {coverage*100:.2f}%')


def main(args=None):

    rclpy.init(args=args)

    node = CoverageTracker()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
