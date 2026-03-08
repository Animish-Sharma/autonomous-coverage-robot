import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
import numpy as np
import csv
import time


class CoverageMetrics(Node):

    def __init__(self):

        super().__init__('coverage_metrics')

        self.start_time = time.time()

        self.map_sub = self.create_subscription(
            OccupancyGrid,
            '/map',
            self.map_callback,
            10)

        self.file = open('coverage_log.csv','w',newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['time','coverage'])

    def map_callback(self,msg):

        data = np.array(msg.data)

        free = np.sum(data == 0)

        known = np.sum(data != -1)

        coverage = known / len(data)

        t = time.time() - self.start_time

        self.writer.writerow([t,coverage])

        self.get_logger().info(
            f"time={t:.1f}s coverage={coverage*100:.2f}%"
        )


def main(args=None):

    rclpy.init(args=args)

    node = CoverageMetrics()

    rclpy.spin(node)

    node.file.close()

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
