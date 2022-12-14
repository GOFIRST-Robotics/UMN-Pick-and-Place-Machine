# library: umn-pick-and-place-machine
# extends a pick-and-place centroid csv file to include starting mat positions for each component
import csv


def add_mat_positions(infilename, outfilename, delimiter=",", \
                      grid_spacing=10, grid_row_length=10, grid_origin=(0, 0)):
    # Parameter info:
    # grid_spacing: how many milimeters wide each square in the grid is
    # grid_row_length: how many parts go in each row of the grid

    with open(infilename, mode="r") as infile, open(outfilename,
                                                    mode="w") as outfile:
        csv_reader = csv.reader(infile, delimiter=delimiter)
        csv_writer = csv.writer(outfile, delimiter=delimiter)

        # Create the header row in the outfile
        header_row = next(csv_reader)
        header_row.extend(["Start mat x", "Start mat y"])
        csv_writer.writerow(header_row)

        # Writing the actual grid data to the csv
        grid_row = 0
        grid_column = 0

        for row in csv_reader:
            # Calculates starting mat position for this entry
            start_x = grid_origin[0] + grid_column * grid_spacing
            start_y = grid_origin[1] + grid_row * grid_spacing
            row.extend([start_x, start_y])

            # Increments position on grid.
            grid_column = (grid_column + 1) % grid_row_length
            if grid_column == 0:  # Rolls over to next row if needed
                grid_row += 1

            csv_writer.writerow(row)
