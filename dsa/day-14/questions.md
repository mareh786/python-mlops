# Day 14 (5 Foundation Review Problems)

## Problem 1: Find the Second Most Frequent Character

Given a string, return the character with the second highest frequency.

Assume such a character always exists.

### Example

```python
second_most_frequent("aaabbccccdd")
```

Output:

```text
a
```

### Concepts

- dictionaries
- frequency counting
- comparisons

---

## Problem 2: Merge Two Lists Alternately

Given two lists, merge them by taking one element from each alternately.

If one list becomes empty, append the remaining elements.

### Example

```python
merge_alternate([1, 2, 3], ["a", "b", "c", "d"])
```

Output:

```text
[1, "a", 2, "b", 3, "c", "d"]
```

### Concepts

- lists
- indexing
- traversal

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

- strings
- comparison
- traversal

---

## Problem 4: Check if a List Contains Consecutive Numbers

Return `True` if the list contains consecutive integers regardless of order.

### Example

```python
is_consecutive([4, 2, 3, 5])
```

Output:

```text
True
```

### Concepts

- sorting (manual thinking)
- min/max
- validation

---

## Problem 5: Print Pascal's Triangle (First 6 Rows)

Print:

```text
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
```

### Concepts

- nested loops
- dynamic construction
- patterns
