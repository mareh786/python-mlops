# Day 13 

## Problem 1: Find the Third Largest Number

Write a function that returns the third largest **distinct** number in a list.

Return `None` if it does not exist.

### Example

```python
third_largest([10, 4, 7, 20, 15])
```

Output:

```text
10
```

### Concepts

- loops
- tracking multiple values
- comparisons

---

## Problem 2: Check if a String is an Anagram

Two strings are anagrams if they contain the same characters with the same frequencies.

Ignore letter casing.

### Example

```python
is_anagram("Listen", "Silent")
```

Output:

```text
True
```

### Concepts

- dictionaries
- frequency counting
- strings

---

## Problem 3: Find the Missing Character

Given two strings where the second string contains exactly one extra character, return the extra character.

### Example

```python
missing_char("abcd", "abcde")
```

Output:

```text
e
```

### Concepts

- frequency counting
- strings
- comparison

---

## Problem 4: Separate Even and Odd Numbers

Return a new list where all even numbers appear first, followed by all odd numbers.

Maintain the original order within each group.

### Example

```python
separate_even_odd([5, 2, 8, 1, 6, 3])
```

Output:

```text
[2, 8, 6, 5, 1, 3]
```

### Concepts

- lists
- filtering
- traversal

---

## Problem 5: Print a Hollow Right Triangle

For `n = 5`, print:

```text
*
**
* *
*  *
*****
```

### Concepts

- nested loops
- conditions
- pattern printing
