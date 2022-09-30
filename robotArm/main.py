# Import the csv module
import csv

# Velocity of the arm measured in mm/s
velocity = 100

raised_z = 100  # TODO: Configure this!
lowered_z = 10  # TODO: Configure this!

# Access our .csv and .txt files
csv_file = open('centroid.csv')
instructions = open("instructions.txt", "w")

# Configure how to read our .csv file
csvReader = csv.reader(csv_file, delimiter=',')
csv_labels = {"x": 1, "y": 2, "rotation": 4}


# TODO: This method is a WIP
def pickup_next_part():
    # TODO: HERE WE WANT TO MOVE TO THE NEXT PART ON THE MAT/TRAY (William started code for this?)
    # Lower down to the pcb
    instructions.write("{" + f'"cmd":"lmove", "z":{lowered_z}, "rel":0, "vel":{velocity}' + "}\n")
    # TODO: HERE WE WANT TO ENABLE THE SUCTION
    # Raise back up
    instructions.write("{" + f'"cmd":"lmove", "z":{raised_z}, "rel":0, "vel":{velocity}' + "}\n")


next(csvReader)  # We want to skip the first row of the .csv file since it is just the column labels

for row in csvReader:
    x_value = row[csv_labels["x"]].replace("mm", "")  # Remove the 'mm' label from the value
    y_value = row[csv_labels["y"]].replace("mm", "")  # Remove the 'mm' label from the value
    # Move to specifed (x, y) position of the component
    instructions.write("{" + f'"cmd":"lmove", "x":{x_value}, "y":{y_value}, "rel":0, "vel":{velocity}' + "}\n")
    # Lower down to the pcb
    instructions.write("{" + f'"cmd":"lmove", "z":{lowered_z}, "rel":0, "vel":{velocity}' + "}\n")
    # TODO: HERE WE WANT TO DISABLE THE SUCTION
    # Raise back up
    instructions.write("{" + f'"cmd":"lmove", "z":{raised_z}, "rel":0, "vel":{velocity}' + "}\n")
