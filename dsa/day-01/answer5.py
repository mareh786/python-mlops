# -------------------- Approach 1 --------------------

# Create a list of string values
list1 = ['1', '2', '3']

# Add more elements to the list
list1.append('4')
list1.append('5')
list1.append('6')

# Display the updated list
print(list1)

# Variable to store the count of even indices
evencount = 0

# Loop through the indices of the list
for i in range(len(list1)):
    
    # Check whether the index is even (0, 2, 4, ...)
    if i % 2 == 0:
        evencount += 1

# Print the number of even indices
print(evencount)


# -------------------- Approach 2 --------------------

def evenCount():
    # Take space-separated numbers as input
    # Example input: 1 2 3 4 5 6
    list2 = list(map(int, input(
        "Enter the numbers separated by spaces: "
    ).split()))

    # Display the input list
    print(list2)

    # Variable to count even numbers
    count = 0

    # List to store the even numbers
    list3 = []

    # Iterate through each element using its index
    for i in range(len(list2)):

        # Check if the current element is even
        if list2[i] % 2 == 0:
            count += 1
            list3.append(list2[i])

    # Return both the count and the list of even numbers
    return count, list3


# Call the function and unpack the returned tuple
count, even_numbers = evenCount()

# Display the final result
print(
    f"There are {count} even numbers and those are {even_numbers}!!"
)