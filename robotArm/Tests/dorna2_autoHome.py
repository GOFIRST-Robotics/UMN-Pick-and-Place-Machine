from dorna2 import Dorna  # this is the dorna2 python API

robot = Dorna()  # Create a new instance of a "Dorna" object
robot_ip_address = "169.254.63.192"  # Specify the ip address to connect to

if not robot.connect(robot_ip_address):  # (Attempt to) Connect to the robot server at the specified IP address
    print("ERROR: Could not find the dorna2 robot at port:", robot_ip_address)
else:
    print("Successfully connected to the dorna2 at port:", robot_ip_address)

    # Disable the alarm mode
    if robot.get_alarm():
        robot.set_alarm(0)
        print("Disabling the alarm")

    robot.set_motor(1)  # Turn on the motors
    print("Turning on the motors")

    # Got back to our home/origin
    print("Executing commands now")
    robot.play(timeout=2, cmd="jmove", rel=0, j0=-0.230625, j1=0.144, j2=-0.036, j3=0.10125, j4=0.79875, j5=-0.0, j6=-0.0, j7=-0.0, vel=120, accel=120)

    print(robot.recv())

robot.close()  # Always close the socket when you are done :)
print("Script is over now")
