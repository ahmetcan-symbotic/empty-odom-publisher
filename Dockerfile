ARG ROS_DISTRO=humble
FROM ros:${ROS_DISTRO}-ros-base

# Install additional dependencies
RUN apt-get update && apt-get install -y \
    python3-pip

# Install the scipy package using pip
RUN pip3 install --no-cache-dir scipy

# Set the working directory
WORKDIR /app

# Initialize the workspace
RUN . /opt/ros/${ROS_DISTRO}/setup.sh


# Copy the ROS2 package into the container
COPY ./dummy_odom /app/dummyodom

# Build the ROS2 package
RUN . /opt/ros/${ROS_DISTRO}/setup.sh && \
    cd /app/dummyodom && \
    colcon build

# Run the ROS2 node
# Rosrun format: ros2 run <package_name> <node_name>
CMD . /opt/ros/${ROS_DISTRO}/setup.sh && \
    . /app/dummyodom/install/setup.sh && \
    ros2 run dummyodom dummyodom_node
