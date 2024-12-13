from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # First Node: webots_apriltags
        Node(
            package='webots_apriltags',  # The package name
            executable='webots_apriltags',  # The node executable name
            name='webots_apriltags_node',  # Optional: Custom node name
            output='screen'  # Output to screen
        ),
        
        # Second Node: apriltag_ros
        Node(
            package='apriltag_ros',  # The package name
            executable='apriltag_node',  # The node executable name
            name='apriltag_ros_node',  # Optional: Custom node name
            output='screen',  # Output to screen
            arguments=[
                '--ros-args', 
                '-r', 'image_rect:=/image_raw', 
                '-r', 'camera_info:=/camera_info', 
                '--params-file',
                Command(['ros2 pkg prefix apriltag_ros', '/opt/ros/humble/cfg/tags_36h11.yaml'])
            ]
        ),
    ])

