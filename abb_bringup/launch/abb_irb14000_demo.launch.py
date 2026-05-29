from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    description_package = LaunchConfiguration("description_package")
    description_file = LaunchConfiguration("description_file")
    controllers_file = LaunchConfiguration("controllers_file")
    moveit_config_package = LaunchConfiguration("moveit_config_package")
    robot_xacro_file = LaunchConfiguration("robot_xacro_file")
    support_package = LaunchConfiguration("support_package")
    moveit_config_file = LaunchConfiguration("moveit_config_file")
    launch_rviz = LaunchConfiguration("launch_rviz")
    use_fake_hardware = LaunchConfiguration("use_fake_hardware")
    rws_ip = LaunchConfiguration("rws_ip")
    rws_port = LaunchConfiguration("rws_port")

    control_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare("abb_bringup"), "launch", "abb_control.launch.py"])
        ),
        launch_arguments={
            "description_package": description_package,
            "description_file": description_file,
            "controllers_file": controllers_file,
            "moveit_config_package": moveit_config_package,
            "launch_rviz": "false",
            "use_fake_hardware": use_fake_hardware,
            "rws_ip": rws_ip,
            "rws_port": rws_port,
        }.items(),
    )

    moveit_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare("abb_bringup"), "launch", "abb_moveit.launch.py"])
        ),
        launch_arguments={
            "robot_xacro_file": robot_xacro_file,
            "support_package": support_package,
            "moveit_config_package": moveit_config_package,
            "moveit_config_file": moveit_config_file,
            "launch_rviz": launch_rviz,
        }.items(),
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "description_package",
                default_value="abb_irb14000_support",
            ),
            DeclareLaunchArgument(
                "description_file",
                default_value="irb14000.urdf.xacro",
            ),
            DeclareLaunchArgument(
                "controllers_file",
                default_value="abb_irb14000_controllers.yaml",
            ),
            DeclareLaunchArgument(
                "moveit_config_package",
                default_value="abb_irb14000_moveit_config",
            ),
            DeclareLaunchArgument(
                "robot_xacro_file",
                default_value="irb14000.urdf.xacro",
            ),
            DeclareLaunchArgument(
                "support_package",
                default_value="abb_irb14000_support",
            ),
            DeclareLaunchArgument(
                "moveit_config_file",
                default_value="abb_irb14000.srdf.xacro",
            ),
            DeclareLaunchArgument(
                "use_fake_hardware",
                default_value="true",
            ),
            DeclareLaunchArgument(
                "rws_ip",
                default_value="None",
            ),
            DeclareLaunchArgument(
                "rws_port",
                default_value="80",
            ),
            DeclareLaunchArgument(
                "launch_rviz",
                default_value="false",
            ),
            control_launch,
            moveit_launch,
        ]
    )