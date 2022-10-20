from dorna2 import Dorna  # this is the dorna2 python API

robot = Dorna()  # Create a new instance of a "Dorna" object
robot_ip_address = "169.254.63.192"  # Specify the ip address to connect to

if not robot.connect(robot_ip_address):  # (Attempt to) Connect to the robot server at the specified IP address
    print("ERROR: Could not find the dorna2 robot at port:", robot_ip_address)
    print("Stopping the script now")
else:
    print("Successfully connected to the dorna2 at port:", robot_ip_address, "!")
    print("Executing commands now")
    robot.play_script(script_path="test.txt")  # Instruct the robot to execute these commands

robot.close()  # Always close the socket when you are done :)
