# Import the necessary modules for this project
import csv  # for reading .csv files
import starting_mat  # this is the code that William wrote
from dorna2 import Dorna  # this is the dorna2 python API

robot = Dorna()  # Create a new instance of a "Dorna" object
robot_ip_address = "169.254.63.192"  # Specify the ip address to connect to

# Velocity of the arm measured in mm/s
velocity = 100

raised_z = 150  # TODO: Configure this through actual testing!
lowered_z = 50  # TODO: Configure this through actual testing!
shift_amount = (0, 300)

starting_mat.add_mat_positions("centroid.csv", "centroid-with-mat.csv")

# Access our .csv and .txt files
csv_file = open("centroid-with-mat.csv")
instructions = open("instructions.txt", "w")

# Configure how to read our .csv file
csvReader = csv.reader(csv_file, delimiter=',')
csv_labels = {"x": 1, "y": 2, "rotation": 4, "start_x": 5, "start_y": 6}


def pickup_next_part():
    start_x = str(int(row[csv_labels["start_x"]]) + shift_amount[0])
    start_y = str(int(row[csv_labels["start_y"]]) + shift_amount[1])
    # Move to the next part on the mat
    instructions.write("{" + f'"cmd":"lmove", "x":{start_x}, "y":{start_y}, "rel":0, "vel":{velocity}' + "}\n")
    # Lower down to the pcb
    instructions.write("{" + f'"cmd":"lmove", "z":{lowered_z}, "rel":0, "vel":{velocity}' + "}\n")
    # Enable the Suction
    instructions.write("{" + f'"cmd":"output", "out0":1' + "}\n")
    # Raise back up
    instructions.write("{" + f'"cmd":"lmove", "z":{raised_z}, "rel":0, "vel":{velocity}' + "}\n")


next(csvReader)  # We want to skip the first row of the .csv file since it is just the column labels

for row in csvReader:
    pickup_next_part()
    x_value = str(int(row[csv_labels["x"]].replace("mm", "")) + shift_amount[0])  # Remove the 'mm' label from the value
    y_value = str(int(row[csv_labels["y"]].replace("mm", "")) + shift_amount[1])  # Remove the 'mm' label from the value
    # Move to specifed (x, y) position of the component
    instructions.write("{" + f'"cmd":"lmove", "x":{x_value}, "y":{y_value}, "rel":0, "vel":{velocity}' + "}\n")
    # Lower down to the pcb
    instructions.write("{" + f'"cmd":"lmove", "z":{lowered_z}, "rel":0, "vel":{velocity}' + "}\n")
    # Disable the Suction
    instructions.write("{" + f'"cmd":"output", "out0":0' + "}\n")
    # Raise back up
    instructions.write("{" + f'"cmd":"lmove", "z":{raised_z}, "rel":0, "vel":{velocity}' + "}\n")

if not robot.connect(robot_ip_address):  # (Attempt to) Connect to the robot server at the specified IP address
    print("ERROR: Could not find the dorna2 robot at port:", robot_ip_address)
    print("Stopping the script now")
else:
    print("Successfully connected to the dorna2 at port:", robot_ip_address, "!")
    print("Executing commands now")
    robot.play_script(script_path="instructions.txt")  # Instruct the robot to execute these commands
robot.close()  # Always close the socket when you are done :)
