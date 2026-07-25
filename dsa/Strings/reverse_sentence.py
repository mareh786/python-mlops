"""
---------------------------------------------------------
Program: Reverse the Words in a Sentence

Approach:
- Split the sentence into individual words using `split()`.
- Traverse the list of words in reverse order.
- Append each word to a new string.
- Remove the trailing space using `strip()`.
- Return the reversed sentence.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (Each word is processed exactly once.)

Space Complexity:
- O(n)
  (A new list of words and a new string are created.)

Key Learning:
- `split()` converts a sentence into a list of words.
- `reversed()` iterates over the list in reverse order.
- `strip()` removes leading and trailing spaces.
- This is a common string manipulation interview problem.
---------------------------------------------------------
"""


def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Initialize an empty string
    result = ""

    # Traverse the words in reverse order
    for word in reversed(words):
        result += word + " "

    # Remove the trailing space
    result = result.strip()

    return result


# Driver Code
print("Reversed Sentence:", reverse_words("I am Adil"))
