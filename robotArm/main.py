# Import the necessary modules for this project
import csv  # for reading .csv files
import starting_mat  # this is the code that William wrote
from dorna2 import Dorna  # this is the dorna2 python API

robot = Dorna()  # Create a new instance of a "Dorna" object
robot_ip_address = "10.164.161.152"  # Specify the ip address to connect to

# Velocity of the arm measured in mm/s
velocity = 100

raised_z = 150  # TODO: Configure this through actual testing!
lowered_z = 50  # TODO: Configure this through actual testing!
shift_amount = (0, 300)

starting_mat.add_mat_positions("centroid.csv", "centroid-with-mat.csv")

# Access our .csv and .txt files
csv_file = open("centroid-with-mat.csv")

# Configure how to read our .csv file
csvReader = csv.reader(csv_file, delimiter=',')
csv_labels = {"x": 1, "y": 2, "rotation": 4, "start_x": 5, "start_y": 6}


def pickup_next_part():
    start_x = str(int(row[csv_labels["start_x"]]) + shift_amount[0])
    start_y = str(int(row[csv_labels["start_y"]]) + shift_amount[1])
    # Move to the next part on the mat
    robot.play(cmd="lmove", x=start_x, y=start_y, rel=0, vel=velocity)
    # Lower down to the pcb
    robot.play(cmd="lmove", z=lowered_z, rel=0, vel=velocity)
    # Enable the Suction
    robot.play(cmd="output", out0=1)
    # Raise back up
    robot.play(cmd="lmove", z=raised_z, rel=0, vel=velocity)


next(csvReader)  # We want to skip the first row of the .csv file since it is just the column labels

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

    for row in csvReader:
        pickup_next_part()
        x_value = str(int(row[csv_labels["x"]].replace("mm", "")) + shift_amount[0])  # Remove the 'mm' label
        y_value = str(int(row[csv_labels["y"]].replace("mm", "")) + shift_amount[1])  # Remove the 'mm' label
        # Move to specifed (x, y) position of the component
        robot.play(cmd="lmove", x=x_value, y=y_value, rel=0, vel=velocity)
        # Lower down to the pcb
        robot.play(cmd="lmove", z=lowered_z, rel=0, vel=velocity)
        # Disable the Suction
        robot.play(cmd="output", out0=0)
        # Raise back up
        robot.play(cmd="lmove", z=raised_z, rel=0, vel=velocity)

robot.close()  # Always close the socket when you are done :)
print("Script is over now")
