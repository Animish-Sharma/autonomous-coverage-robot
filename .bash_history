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
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 topic list
ros2 node list
ros2 topic echo /scan
ros2 node list
ros2 topic list
ros2 node list
ros2 pkg list | grep webots
ls
cd root
ls
cd ros2_ws
ls
source install/setup.bash
ros2 node list
ls
cd src
ls
cd coverage_webots/
ls
cd worlds/
ls
vim project_world.wbt 
rm -rf ~/ros2_ws/src/coverage_webots/launch/project_launch.py
vim ~/ros2_ws/src/coverage_webots/launch/project_launch.py
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 node list
colcon build
source install/setup.bash
ros2 run coverage_webots coverage_controller
[A
ros2 run coverage_webots coverage_controller
ls
cd src/coverage_webots/
ls
cd worls
cd worlds
ls
vim project_world.wbt 
cd ~/ros2_ws/
colcon build
source install/setup.bash
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 run coverage_webots coverage_controller
colcon build --package-select coverage_webots
colcon build --packages-select coverage_webots
source install/setup.bash
vim src/coverage_webots/worlds/project_world.wbt 
ros2 pkg list | grep webots
source /opt/ros/humble/setup.bash
ros2 pkg executables webots_ros2_driver
vim ~/ros2_ws/src/coverage_webots/launch/project_launch.py
rm -rf ~/ros2_ws/src/coverage_webots/launch/project_launch.py
vim ~/ros2_ws/src/coverage_webots/launch/project_launch.py
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 launch coverage_webots project_launch.py
ls
ls -l
cd src
ls -
ls -l
cd coverage_webots/
ls -l
cd worlds
ls -l
ls
cd..
ls
cd ..
ls
cd launch
ls
vim project_launch.py 
rm -rf project_launch.py 
vim project_launch.py 
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 launch coverage_webots webots_launch.py
ros2 launch coverage_webots project_launch.py
export PATH=$PATH:/usr/local/webots
webots
echo 'export PATH=$PATH:/usr/local/webots' >> ~/.bashrc
source ~/.bashrc
ros2 launch coverage_webots project_launch.py
ros2 topic list
ros2 run coverage_webots coverage_controller
source ~/ros2_ws/install/setup.bash
ros2 run webots_ros2_driver driver
ros2 run webots_ros2_driver driver   --ros-args -p robot_name:=TurtleBot3Burger
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 run webots_ros2_driver driver   --ros-args   -p robot_name:=TurtleBot3Burger   -p port:=1234
export USER=root
sudo apt install ros-humble-turtlebot3-description
apt install ros-humble-turtlebot3-description
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
export TURTLEBOT3_MODEL=burger
export USER=root
ros2 run webots_ros2_driver driver   --ros-args   -p robot_name:=TurtleBot3Burger   -p port:=1234   -p robot_description:="$(xacro /opt/ros/humble/share/turtlebot3_description/urdf/turtlebot3_burger.urdf.xacro)"
apt update
apt install ros-humble-turtlebot3-description
ls /opt/ros/humble/share/turtlebot3_description/urdf
find ~/ros2_ws -name "xml.py"
mkdir -p /tmp/webots/root
chmod 777 /tmp/webots/root
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 launch webots_ros2_turtlebot robot_launch.py
ros2 run webots_ros2_driver driver   --ros-args   -p robot_name:=TurtleBot3Burger   -p port:=1234
ros2 run webots_ros2_driver driver
clear
ls
cd ..
ls
cd ros2_ws
colcon build
source install/setup.bash
ros2 run webots_ros2_driver driver
ros2 run coverage_webots coverage_controller
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 run coverage_webots coverage_controller
export USER=root
export USERNAME=root
echo 'export USER=root' >> ~/.bashrc
echo 'export USERNAME=root' >> ~/.bashrc
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 node list
rm -rf ~/ros2_ws/src/coverage_webots/launch/project_launch.py
vim ~/ros2_ws/src/coverage_webots/launch/project_launch.py
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 launch coverage_webots project_launch.py
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 launch coverage_webots project_launch.py
ros2 launch webots_ros2_turtlebot robot_launch.py
ros2 run coverage_webots coverage_controller
ros2 launch coverage_webots project_launch.py
ros2 run coverage_webots coverage_controller
ros2 launch webots_ros2_turtlebot robot_launch.py
ros2 launch webots_ros2_turtlebot robot_launch.py world:=~/ros2_ws/src/coverage_webots/worlds/project_world.wbt
ros2 launch webots_ros2_turtlebot robot_launch.py world:=/root/ros2_ws/src/coverage_webots/worlds/project_world.wbt
ros2 launch webots_ros2_turtlebot robot_launch.py
ros2 topic list
ros2 launch webots_ros2_turtlebot robot_launch.py world:=/root/ros2_ws/src/coverage_webots/worlds/project_world.wbt
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch webots_ros2_turtlebot robot_launch.py world:=/root/ros2_ws/src/coverage_webots/worlds/project_world.wbt
apt update
apt install -y mesa-utils libgl1-mesa-dri
export LIBGL_ALWAYS_SOFTWARE=1
export MESA_GL_VERSION_OVERRIDE=3.3
ros2 launch webots_ros2_turtlebot robot_launch.py world:=/root/ros2_ws/src/coverage_webots/worlds/project_world.wbt
export WEBOTS_HOME=/root/.ros/webotsR2025a/webots
apt update
apt install -y mesa-utils libgl1-mesa-dri libgl1-mesa-glx
glxinfo | grep OpenGL
export WEBOTS_HOME=/root/.ros/webotsR2025a/webots
export LIBGL_ALWAYS_SOFTWARE=1
export MESA_GL_VERSION_OVERRIDE=3.3
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 launch webots_ros2_turtlebot robot_launch.py world:=/root/ros2_ws/src/coverage_webots/worlds/project_world.wbt
ros2 launch webots_ros2_turtlebot project_launch.py
ros2 launch coverage_webots project_launch.py
export WEBOTS_HOME=/root/.ros/webotsR2025a/webots
export LIBGL_ALWAYS_SOFTWARE=1
export MESA_GL_VERSION_OVERRIDE=3.3
ros2 launch coverage_webots project_launch.py
--net=host
-e DISPLAY=$DISPLAY
-v /tmp/.X11-unix:/tmp/.X11-unix
export DISPLAY=:0
xhost +
export DISPLAY=:0
ros2 launch coverage_webots project_launch.py
colcon build
source install/setup.bash
ros2 launch coverage_webots project_launch.py
exit
cd root
cd ros2_ws/
colcon build
source install/setup.bash
ls
ros2 coverage_webots project_launch.py
ros2 launch coverage_webots project_launch.py
rm -rf /tmp/webots
rm -rf ~/.ros/webots*
ros2 launch coverage_webots project_launch.py
export WEBOTS_HOME=/root/.ros/webotsR2025a/webots
export LIBGL_ALWAYS_SOFTWARE=1
export MESA_GL_VERSION_OVERRIDE=3.3
ros2 launch coverage_webots project_launch.py
export WEBOTS_HOME=/root/.ros/webotsR2025a/webots
mkdir -p /tmp/webots/root
chmod 777 /tmp/webots/root
export LIBGL_ALWAYS_SOFTWARE=1
export MESA_GL_VERSION_OVERRIDE=3.3
export QT_XCB_GL_INTEGRATION=none
ros2 launch coverage_webots project_launch.py
$WEBOTS_HOME/webots
echo $DISPLAY
$WEBOTS_HOME/webots
glxinfo | grep OpenGL
export QT_QPA_PLATFORM=xcb
$WEBOTS_HOME/webots
exit
