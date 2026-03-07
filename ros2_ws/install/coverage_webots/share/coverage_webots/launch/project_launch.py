from launch import LaunchDescription
from webots_ros2_driver.webots_launcher import WebotsLauncher
from launch_ros.actions import Node
import os

def generate_launch_description():

    world = os.path.join(
        os.getenv('HOME'),
        'ros2_ws/src/coverage_webots/worlds/project_world.wbt'
    )

    webots = WebotsLauncher(world=world)

    driver = Node(
        package='webots_ros2_driver',
        executable='driver',
        output='screen',
        additional_env={
            'WEBOTS_ROBOT_NAME': 'TurtleBot3Burger'
        },
        parameters=[{
            'robot_description': '<robot></robot>'
        }]
    )

    return LaunchDescription([
        webots,
        driver
    ])
