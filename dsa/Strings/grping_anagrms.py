"""
---------------------------------------------------------
Program: Group Anagrams

Approach:
- Create an empty dictionary to group anagrams.
- Traverse each word in the list.
- Sort the characters of the word to form a unique key.
- If the key is not present in the dictionary, create a new list.
- Append the current word to the corresponding list.
- Return all grouped anagrams as a list of lists.

Time Complexity:
- Best Case: O(n × k log k)
- Average Case: O(n × k log k)
- Worst Case: O(n × k log k)

  where:
  - n = number of words
  - k = maximum length of a word

  (Sorting each word takes O(k log k).)

Space Complexity:
- O(n × k)
  (The dictionary stores all words grouped by their sorted keys.)

Key Learning:
- Two words are anagrams if their sorted characters are the same.
- Dictionaries (hash maps) are useful for grouping elements
  based on a common key.
- This is a very common interview problem.
---------------------------------------------------------
"""


def group_anagrams(words):
    # Dictionary to store grouped anagrams
    groups = {}

    # Traverse each word
    for word in words:

        # Create a key by sorting the characters
        key = "".join(sorted(word))

        # Create a new group if the key doesn't exist
        if key not in groups:
            groups[key] = []

        # Add the word to its group
        groups[key].append(word)

    # Return all grouped anagrams
    return list(groups.values())


# Driver Code
arr = ["eat", "tea", "tan", "ate", "nat", "bat"]

print("Grouped Anagrams:")
print(group_anagrams(arr))
