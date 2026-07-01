# Function to reverse the array in-place
def reverseArray(arr):
    # Get the size of the array
    n = len(arr)
    
    # Initialize two pointers
    a = 0            # start (left pointer)
    b = n - 1        # end (right pointer)

    # Run loop until pointers meet
    while a < b:
        # Swap elements at positions a and b
        arr[a], arr[b] = arr[b], arr[a]

        # Move pointers towards center
        a += 1
        b -= 1


# Input array
arr = [1, 7, 9, 3]

# Print original array
print(f"The initial array is {arr}")

# Call function to reverse array
reverseArray(arr)

# Print reversed array
print(f"After reversing, the array becomes: {arr}")


