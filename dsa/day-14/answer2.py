# Merge two lists alternately.
# If one list ends before the other, append the remaining elements.

def merge_list(lst1, lst2):
    # Create an empty list to store the merged result
    merged_list = []

    # Initialize index
    i = 0

    # Add elements alternately while both lists have elements
    while i < len(lst1) and i < len(lst2):
        merged_list.append(lst1[i])
        merged_list.append(lst2[i])
        i += 1

    # Append any remaining elements from the first list
    while i < len(lst1):
        merged_list.append(lst1[i])
        i += 1

    # Append any remaining elements from the second list
    while i < len(lst2):
        merged_list.append(lst2[i])
        i += 1

    # Return the merged list
    return merged_list


# Example usage
print(merge_list([1, 2, 3, 4, 5, 6], ['a', 'b', 'c', 'd']))
