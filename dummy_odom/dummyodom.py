"""
This module contains the implementation of the publisher Odometry Node class.
"""

import math

import rclpy
from builtin_interfaces.msg import Time
from nav_msgs.msg import Odometry
from rclpy.node import Node

# Messages
from std_msgs.msg import Header

PI = math.pi

QUEUE_SIZE = 50


class PublisherNode(Node):
    """A node that publisher to a topic."""

    def __init__(self):
        super().__init__("OdometryPublisher_node")

        self.publisher = self.create_publisher(Odometry, "processed_odom", QUEUE_SIZE)
        self.prev_pose = None
        self.prev_timestamp = None
        self.prev_enc_ltrac = None
        self.prev_enc_rtrac = None

        self.timer = self.create_timer(0.1, self.publish_odom)

    def publish_odom(
        self,
    ):
        """Print the received message."""

        # Create an instance of the Header and set the timestamp
        header = Header()
        header.stamp = self.get_clock().now().to_msg()
        header.frame_id = "Odometry.0"

        # Define nav_msgs/Odometry
        odometry_msg = Odometry()
        odometry_msg.header = header

        # Set the position
        self.publisher.publish(odometry_msg)


def main(args=None):
    """The main function."""
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
