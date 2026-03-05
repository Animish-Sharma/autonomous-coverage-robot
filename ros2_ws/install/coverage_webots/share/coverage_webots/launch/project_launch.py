from launch import LaunchDescription
from webots_ros2_driver.webots_launcher import WebotsLauncher
import os

def generate_launch_description():

    package_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    world = os.path.join(package_dir, 'worlds', 'project_world.wbt')

    webots = WebotsLauncher(
        world=world
    )

    return LaunchDescription([
        webots
    ])
