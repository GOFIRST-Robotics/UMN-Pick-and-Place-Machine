# Import the csv module
import csv
import starting_mat

# Velocity of the arm measured in mm/s
velocity = 100

raised_z = 100  # TODO: Configure this through actual testing!
lowered_z = 10  # TODO: Configure this through actual testing!

starting_mat.add_mat_positions("centroid.csv", "centroid-with-mat.csv")

# Access our .csv and .txt files
csv_file = open("centroid-with-mat.csv")
instructions = open("instructions.txt", "w")

# Configure how to read our .csv file
csvReader = csv.reader(csv_file, delimiter=',')
csv_labels = {"x": 1, "y": 2, "rotation": 4, "start_x": 5, "start_y": 6}


# TODO: This method is a WIP
def pickup_next_part():
    start_x = row[csv_labels["start_x"]]
    start_y = row[csv_labels["start_y"]]
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
    x_value = row[csv_labels["x"]].replace("mm", "")  # Remove the 'mm' label from the value
    y_value = row[csv_labels["y"]].replace("mm", "")  # Remove the 'mm' label from the value
    # Move to specifed (x, y) position of the component
    instructions.write("{" + f'"cmd":"lmove", "x":{x_value}, "y":{y_value}, "rel":0, "vel":{velocity}' + "}\n")
    # Lower down to the pcb
    instructions.write("{" + f'"cmd":"lmove", "z":{lowered_z}, "rel":0, "vel":{velocity}' + "}\n")
    # Disable the Suction
    instructions.write("{" + f'"cmd":"output", "out0":0' + "}\n")
    # Raise back up
    instructions.write("{" + f'"cmd":"lmove", "z":{raised_z}, "rel":0, "vel":{velocity}' + "}\n")
