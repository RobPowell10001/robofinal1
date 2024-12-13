# robofinal1

### How to run the controller and world:

#### 1. Setup environment and enter directory
Run the following commands:
- `source /opt/ros/humble/setup.bash`
- `export WEBOTS_HOME=/mnt/c/Program\ Files/Webots`
- `cd [project root]/webots_finalproject/src/webots_finalproject/`

#### 2. Build and run launch file
Once in the directory, you should only have to:
- `colcon build`
- `source install/setup.bash`

And run the launch file with:
- `ros2 launch webots_finalproject webots_finalproject.launch.py`

