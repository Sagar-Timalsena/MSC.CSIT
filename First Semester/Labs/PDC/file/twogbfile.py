import os

# Define the size of the file in bytes (2GB = 2 * 1024 * 1024 * 1024 bytes)
file_size_bytes = 2 * 1024 * 1024 * 1024

# Define the text to be repeated
text_to_write = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n"

# Calculate the number of repetitions needed to reach the desired file size
repetitions = file_size_bytes // len(text_to_write)

# Open a file for writing
with open("2GB_file.txt", "w") as file:
    # Write the text the calculated number of times
    for _ in range(repetitions):
        file.write(text_to_write)