# Print a hollow right-angled triangle pattern

def hollow_right_triangle(n):
    # Loop through each row
    for i in range(n):
        # Loop through each column in the current row
        for j in range(i + 1):
            # Print '*' for:
            # - the first column
            # - the diagonal (last element of each row)
            # - the last row
            if j == 0 or j == i or i == n - 1:
                print("*", end="")
            else:
                # Print space inside the triangle
                print(" ", end="")
        # Move to the next line after each row
        print()


# Test the function
hollow_right_triangle(5)
