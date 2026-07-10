# Print the upper half of a diamond pattern

def print_upperhalf_diamond(line):
    # Loop through each row
    for i in range(line):
        # Print leading spaces followed by stars
        print(" " * (line - i - 1) + "*" * (2 * i + 1))


# Call the function
print_upperhalf_diamond(6)
