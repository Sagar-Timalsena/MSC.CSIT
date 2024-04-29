import os

# Function to split large file into smaller files with a maximum of 1000 lines each
def split_file(input_file, output_directory):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Open the large input file
    with open(input_file, "r") as file:
        chunk_number = 1
        lines = []
        for line in file:
            lines.append(line)
            # If 1000 lines have been read, write them to a new file
            if len(lines) == 1000:
                output_file = os.path.join(output_directory, f"chunk_{chunk_number}.txt")
                with open(output_file, "w") as output:
                    output.writelines(lines)
                chunk_number += 1
                lines = []

        # Write any remaining lines to a new file
        if lines:
            output_file = os.path.join(output_directory, f"chunk_{chunk_number}.txt")
            with open(output_file, "w") as output:
                output.writelines(lines)

# Usage
large_file = "2GB_file.txt"
output_directory = "split_files"
split_file(large_file, output_directory)
