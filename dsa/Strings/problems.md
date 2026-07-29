# Strings

## Problem 1: Toggle Case

Convert every uppercase letter to lowercase and every lowercase letter to uppercase.

### Example

```python
toggle_case("PyThOn123")
```

Output:

```text
pYtHoN123
```

### Concepts

- ASCII values
- Character traversal

---

## Problem 2: Check if One String is a Rotation of Another

Return `True` if one string is a rotation of the other.

### Example

```python
is_rotation("ABCD", "CDAB")
```

Output:

```text
True
```

### Concepts

- String manipulation
- Pattern recognition

---

## Problem 3: Find the Longest Common Prefix

Given a list of strings, return the longest common prefix.

### Example

```python
longest_common_prefix(["flower", "flow", "flight"])
```

Output:

```text
"fl"
```

### Concepts

- String comparison
- Traversal

---

## Problem 4: Check if Two Strings Differ by Exactly One Character

Return `True` if two strings have the same length and differ at exactly one position.

### Example

```python
one_char_difference("cat", "cut")
```

Output:

```text
True
```

### Concepts

- Character comparison
- Traversal

---

## Problem 5: Remove Consecutive Duplicate Characters

Remove consecutive duplicate characters while keeping one occurrence.

### Example

```python
remove_consecutive_duplicates("aaabbccdaa")
```

Output:

```text
abcda
```

### Concepts

- Traversal
- String construction

---

## Problem 6: Find the Most Frequent Character

Return the character that appears the most.

Assume there is only one correct answer.

### Example

```python
most_frequent("programming")
```

Output:

```text
g
```

### Concepts

- Hashing
- Frequency counting

---

## Problem 7: Check if a String is a Subsequence of Another

Return `True` if the first string is a subsequence of the second.

### Example

```python
is_subsequence("ace", "abcde")
```

Output:

```text
True
```

### Concepts

- Two pointers (intro)
- Traversal

---

## Problem 8: Find the First Repeating Character

Return the first character that repeats in the string.

### Example

```python
first_repeating("abcaef")
```

Output:

```text
a
```

### Concepts

- Hashing
- Traversal

---

## Problem 9: Check if Two Strings are Isomorphic

Two strings are isomorphic if characters from one string can be replaced to get the other.

### Example

```python
is_isomorphic("egg", "add")
```

Output:

```text
True
```

### Concepts

- Mapping
- Hashing

---

## Problem 10: Reverse the Order of Words

Reverse the order of words in a sentence without reversing the characters of each word.

### Example

```python
reverse_words("I love Python")
```

Output:

```text
Python love I
```

### Concepts

- Strings
- Split
- Traversal

# Strings

## Problem 11: Check if Two Strings are One Edit Away

Two strings are one edit away if you can make them equal by performing **exactly one** of the following operations:

- Insert one character
- Delete one character
- Replace one character

### Example

```python
one_edit_away("pale", "ple")
```

Output:

```text
True
```

### Concepts

- Two Pointers
- String Comparison
- Edge Cases

---

## Problem 12: Longest Substring Without Repeating Characters

Return the length of the longest substring containing unique characters.

### Example

```python
longest_unique_substring("abcabcbb")
```

Output:

```text
3
```

### Concepts

- Sliding Window (Introduction)
- Hash Set
- Two Pointers

---

## Problem 13: Group Anagrams

Given a list of strings, group all anagrams together.

### Example

```python
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
```

Output:

```text
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

### Concepts

- Hash Map
- Sorting
- Grouping

---

## Problem 14: Find the Longest Palindromic Prefix

Return the longest prefix of the string that is also a palindrome.

### Example

```python
longest_palindromic_prefix("levelup")
```

Output:

```text
"level"
```

### Concepts

- Strings
- Palindrome
- Prefix

---

## Problem 15: Decode a Compressed String

Given a compressed string where each character is followed by its count, expand it.

### Example

```python
decode("a3b2c4")
```

Output:

```text
"aaabbcccc"
```

### Concepts

- String Parsing
- Traversal
- String Construction

---

## Problem 16: Find the Smallest Window Containing a Character

Given a string and a character, return the length of the smallest substring containing that character.

### Example

```python
smallest_window("abcaad", "c")
```

Output:

```text
1
```

### Concepts

- Traversal
- Window Thinking

---

## Problem 17: Check if Two Strings are Mirror Images

Two strings are mirrors if one is the reverse of the other.

Do not use slicing (`[::-1]`) or `reversed()`.

### Example

```python
mirror("abcde", "edcba")
```

Output:

```text
True
```

### Concepts

- Two Pointers
- String Comparison

---

## Problem 18: Find the Character with Maximum Consecutive Occurrences

Return the character that has the longest consecutive run.

### Example

```python
max_consecutive_char("aaabbccccdde")
```

Output:

```text
"c"
```

### Concepts

- Traversal
- Consecutive Counting

---

## Problem 19: Check if a String Can Become a Palindrome by Removing One Character

Return `True` if removing at most one character makes the string a palindrome.

### Example

```python
valid_palindrome("abca")
```

Output:

```text
True
```

### Concepts

- Two Pointers
- Greedy Thinking

---

## Problem 20: String to Integer (atoi)

Implement a simplified version of `atoi`.

Rules:

- Ignore leading spaces.
- Handle optional '+' or '-'.
- Stop reading when a non-digit character is found.

### Example

```python
my_atoi("   -123abc")
```

Output:

```text
-123
```

### Concepts

- String Parsing
- Edge Cases
- Character Processing

# Strings

## Problem 21: Longest Palindromic Substring

Given a string, return the longest substring that is a palindrome.

If there are multiple answers, return any one of them.

### Example

```python
longest_palindrome("babad")
```

Output:

```text
"bab"
```

### Concepts

- Two Pointers
- Expand Around Center
- String Traversal

---

## Problem 22: Minimum Window Containing All Characters

Given two strings `s` and `t`, return the smallest substring of `s` that contains every character of `t`.

### Example

```python
min_window("ADOBECODEBANC", "ABC")
```

Output:

```text
"BANC"
```

### Concepts

- Sliding Window
- Hash Map
- Frequency Counting

---

## Problem 23: Longest Repeating Character Replacement

You may replace at most `k` characters.

Return the length of the longest substring containing only one repeating character.

### Example

```python
character_replacement("AABABBA", 1)
```

Output:

```text
4
```

### Concepts

- Sliding Window
- Frequency Map

---

## Problem 24: Find All Anagram Indices

Return all starting indices where an anagram of the pattern appears.

### Example

```python
find_anagrams("cbaebabacd", "abc")
```

Output:

```text
[0, 6]
```

### Concepts

- Sliding Window
- Frequency Array
- Hashing

---

## Problem 25: Longest Common Substring

Return the longest substring common to both strings.

### Example

```python
longest_common_substring("abcdef", "zcdemf")
```

Output:

```text
"cde"
```

### Concepts

- Dynamic Programming (Introduction)
- Strings

---

## Problem 26: Zigzag Conversion

Arrange characters in a zigzag pattern and then read row by row.

### Example

```python
zigzag_convert("PAYPALISHIRING", 3)
```

Output:

```text
"PAHNAPLSIIGYIR"
```

### Concepts

- Simulation
- String Construction

---

## Problem 27: Multiply Two Large Numbers Represented as Strings

Do not convert the entire string into an integer.

### Example

```python
multiply("123", "45")
```

Output:

```text
"5535"
```

### Concepts

- Simulation
- Carry Handling
- String Manipulation

---

## Problem 28: Rabin-Karp Pattern Matching

Return the first index where a pattern appears in a text using the Rabin-Karp algorithm.

### Example

```python
rabin_karp("abracadabra", "cada")
```

Output:

```text
4
```

### Concepts

- Rolling Hash
- String Matching

---

## Problem 29: Implement KMP (Knuth-Morris-Pratt)

Implement the KMP algorithm to search for a pattern in a string.

### Example

```python
kmp_search("ababcabcabababd", "ababd")
```

Output:

```text
10
```

### Concepts

- Prefix Function (LPS)
- Efficient Pattern Matching

---

## Problem 30: Text Justification

Given a list of words and a maximum line width, format the text so that each line is fully justified.

### Example

```python
justify(
    ["This","is","an","example","of","text","justification."],
    16
)
```

Output:

```text
[
"This    is    an",
"example  of text",
"justification.  "
]
```

### Concepts

- Greedy Algorithm
- String Manipulation
- Simulation
