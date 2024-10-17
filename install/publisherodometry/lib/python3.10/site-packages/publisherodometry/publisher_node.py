"""
This module contains the implementation of the publisher Odometry Node class.
"""

import math

import rclpy
from nav_msgs.msg import Odometry
from rclpy.node import Node

# Messages
from std_msgs.msg import Header


PI = math.pi

QUEUE_SIZE = 50

"""
This subscribes to the raw_odometry,
processes messages using calculatePose,
and publishes the processed results to the processed_odometry
"""


class PublisherNode(Node):
    """A node that publisher to a topic."""

    def __init__(self):
        super().__init__("OdometryPublisher_node")

        self.publisher = self.create_publisher(Odometry, "processed_odom", QUEUE_SIZE)
        # Set a timer to publish at 10 Hz (0.1 seconds interval)
        self.timer = self.create_timer(0.1, self.publish_odom)

    def publish_odom(self):
        """Print the received message."""

        header = Header()
        header.stamp = self.get_clock().now().to_msg()  # Current time
        header.frame_id = "odom"
        # Convert euler angles to quaternions
        # Define nav_msgs/Odometry
        odometry_msg = Odometry()
        odometry_msg.header = header

        self.publisher.publish(odometry_msg)


def main(args=None):
    """The main function."""
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
