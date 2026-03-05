apt update
apt install -y locales curl gnupg lsb-release software-properties-common build-essential neovim
locale-gen en_US en_US.UTF-8
update-locale LANG=en_US.UTF-8
export LANG=en_US.UTF-8
curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  | gpg --dearmor -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2.list
apt update
apt install -y ros-humble-desktop
apt install -y python3-colcon-common-extensions
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source /opt/ros/humble/setup.bash
ros2
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
source install/setup.bash
exit
apt update
apt install -y libxcb-cursor0
colcon build
ls
cd root
cd ros2_ws/
;ls
ls
clear
colcon build
source install/setup.bash
ros2 launch coverage_webots project_launch.py
apt install ros-humble-slam-toolbox
exit
