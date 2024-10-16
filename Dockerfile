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
COPY ./src/publisherodometry /app/publisherodometry

# Build the ROS2 package
RUN . /opt/ros/${ROS_DISTRO}/setup.sh && \
    cd /app/publisherodometry && \
    colcon build

# Run the ROS2 node
# Rosrun format: ros2 run <package_name> <node_name>
CMD . /opt/ros/${ROS_DISTRO}/setup.sh && \
    . /app/publisherodometry/install/setup.sh && \
    ros2 run publisherodometry publisherodometry_node
