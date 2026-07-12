# Print Pascal's Triangle (6 rows)

def pascal_triangle(rows):
    # Create an empty list to store all rows of the triangle
    triangle = []

    # Generate each row
    for i in range(rows):
        # Every row starts with 1
        row = [1]

        # Calculate the middle elements using the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # Every row except the first ends with 1
        if i > 0:
            row.append(1)

        # Add the completed row to the triangle
        triangle.append(row)

    # Print each row of the triangle
    for row in triangle:
        print(*row)


# Example usage
pascal_triangle(6)
