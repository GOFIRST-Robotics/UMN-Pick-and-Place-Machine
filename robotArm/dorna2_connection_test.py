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

    # Go to "working" position!
    print("Executing commands now")
    robot.play(timeout=2, cmd="jmove", rel=1, j0=-90, vel=120, accel=120)
    print(robot.recv())
    robot.play(timeout=2, cmd="jmove", rel=1, j1=-160, vel=120, accel=120)
    print(robot.recv())
    robot.play(timeout=2, cmd="jmove", rel=1, j2=50, vel=120, accel=120)
    print(robot.recv())
    robot.play(timeout=2, cmd="jmove", rel=1, j3=-150, vel=120, accel=120)
    print(robot.recv())

    robot.sleep(2)
    robot.play(timeout=2, cmd="lmove", rel=0, x=0, y=375, z=140, vel=120, accel=120)
    print(robot.recv())

    # Got back to our home/origin
    """robot.play(timeout=2, cmd="jmove", rel=1, j3=150, vel=120, accel=120, cont=1)
    print(robot.recv())
    robot.play(timeout=2, cmd="jmove", rel=1, j2=-50, vel=120, accel=120, cont=1)
    print(robot.recv())
    robot.play(timeout=2, cmd="jmove", rel=1, j1=160, vel=120, accel=120, cont=1)
    print(robot.recv())
    robot.play(timeout=2, cmd="jmove", rel=1, j0=90, vel=120, accel=120, cont=1)
    print(robot.recv())"""


robot.close()  # Always close the socket when you are done :)
print("Script is over now")
