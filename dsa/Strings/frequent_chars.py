
"""
---------------------------------------------------------
Program: Find the Most Frequent Character in a String

Approach:
- Create an empty dictionary to store the frequency of each
  character.
- Traverse the string and update the frequency of each character.
- Traverse the dictionary to find the character with the highest
  frequency.
- Return the most frequent character.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (The string is traversed once to count frequencies and once to
  find the maximum.)

Space Complexity:
- O(k)
  (Where k is the number of unique characters in the string.)

Key Learning:
- Dictionaries (hash maps) provide efficient frequency counting.
- Frequency counting is a common technique in string and array
  problems.
---------------------------------------------------------
"""


def most_frequent_character(text):
    # Dictionary to store character frequencies
    char_freq = {}

    # Count the frequency of each character
    for ch in text:
        if ch in char_freq:
            char_freq[ch] += 1
        else:
            char_freq[ch] = 1

    # Variables to store the most frequent character
    max_count = 0
    max_char = None

    # Find the character with the highest frequency
    for char, count in char_freq.items():
        if count > max_count:
            max_count = count
            max_char = char

    return max_char


# Driver Code
print("Most Frequent Character:", most_frequent_character("programming"))
