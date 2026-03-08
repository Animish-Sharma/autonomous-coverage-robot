import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import Twist
import numpy as np

class FrontierExplorer(Node):

    def __init__(self):
        super().__init__('frontier_explorer')

        self.map_sub = self.create_subscription(
            OccupancyGrid,
            '/map',
            self.map_callback,
            10)

        self.cmd_pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            10)

    def map_callback(self, msg):

        width = msg.info.width
        height = msg.info.height

        data = np.array(msg.data).reshape((height, width))

        frontiers = []

        for y in range(1, height-1):
            for x in range(1, width-1):

                if data[y,x] == 0:  # free

                    neighbors = [
                        data[y+1,x],
                        data[y-1,x],
                        data[y,x+1],
                        data[y,x-1]
                    ]

                    if -1 in neighbors:
                        frontiers.append((x,y))

        self.get_logger().info(f'Frontiers detected: {len(frontiers)}')

        # simple exploration motion
        cmd = Twist()
        cmd.linear.x = 0.1
        self.cmd_pub.publish(cmd)


def main(args=None):

    rclpy.init(args=args)

    node = FrontierExplorer()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
