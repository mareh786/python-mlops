# Find all duplicate elements in a list

def find_duplicates(lst):
    # Lists to store seen elements and duplicates
    duplicates = []
    seen = []

    # Traverse each element in the list
    for ch in lst:
        # If the element is not seen before, add it to seen
        if ch not in seen:
            seen.append(ch)
        else:
            # If already seen, add it to duplicates
            duplicates.append(ch)

    # Return the list of duplicate elements
    return duplicates


# Call the function and print the result
print(find_duplicates([1, 1, 1, 3, 3, 4, 5, 6, 6, 'a', 'a']))
