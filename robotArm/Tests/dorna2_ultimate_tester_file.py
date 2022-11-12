from dorna2 import Dorna  # this is the dorna2 python API

robot = Dorna()  # Create a new instance of a "Dorna" object
robot_ip_address = "169.254.63.192"  # Specify the ip address to connect to

x_offset = 0
y_offset = 0
z_offset = 0


def line_move(x_pos, y_pos, z_pos):
    x = x_pos+x_offset
    y = y_pos+y_offset
    z = z_pos+z_offset

    print(f'Moving to: ({x}, {y}, {z})')

    robot.play(timeout=2, cmd="lmove", rel=0, x=x, y=y, z=z, vel=120, accel=120)


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

    x_offset = robot.recv()['x']
    y_offset = robot.recv()['y']
    z_offset = robot.recv()['z']

    robot.sleep(2)

    #line_move(0, 0, 0)
    robot.play(timeout=2, cmd="lmove", rel=1, x=0, y=0, z=20, vel=120, accel=120)
    robot.sleep(0.1)
    print(robot.recv())

robot.close()  # Always close the socket when you are done :)
print("Script is over now")
