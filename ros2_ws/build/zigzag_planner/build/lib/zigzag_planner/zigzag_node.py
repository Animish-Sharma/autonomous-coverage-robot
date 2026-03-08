import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import math


class ZigZagCoverage(Node):

    def __init__(self):

        super().__init__('zigzag_coverage')

        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)

        self.cmd_pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            10)

        self.front_distance = float("inf")

        self.turning = False

        self.timer = self.create_timer(0.1,self.control_loop)

    def scan_callback(self,msg):

        ranges = msg.ranges

        center = len(ranges)//2

        front = ranges[center-10:center+10]

        valid = [
            r for r in front
            if not math.isinf(r)
        ]

        if valid:
            self.front_distance = min(valid)

    def control_loop(self):

        cmd = Twist()

        if self.front_distance < 0.8:

            cmd.angular.z = 1.0
            cmd.linear.x = 0.0

        else:

            cmd.linear.x = 0.3

        self.cmd_pub.publish(cmd)


def main(args=None):

    rclpy.init(args=args)

    node = ZigZagCoverage()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
