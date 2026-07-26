"""
---------------------------------------------------------
Program: Check if Two Strings are One Edit Away

An edit can be:
1. Insert one character.
2. Delete one character.
3. Replace one character.

Approach:
- If the difference in lengths is greater than 1, return False.
- If the lengths are equal:
    - Check if the strings differ by at most one replacement.
- If one string is longer by one character:
    - Traverse both strings using two pointers.
    - On a mismatch, advance only the pointer of the longer string.
    - If more than one mismatch occurs, return False.
- If none of the above conditions fail, return True.

Time Complexity:
- Best Case: O(1)
  (Length difference is greater than 1.)

- Average Case: O(n)

- Worst Case: O(n)
  (Each character is compared at most once.)

Space Complexity:
- O(1)
  (Only a few pointer variables are used.)

Key Learning:
- The Two Pointer Technique efficiently handles insertion,
  deletion, and replacement cases.
- At most one edit operation is allowed.
---------------------------------------------------------
"""


def edit_required(s1, s2):
    # Lengths of both strings
    l1, l2 = len(s1), len(s2)

    # If length difference is greater than 1
    if abs(l1 - l2) > 1:
        return False

    # -----------------------------
    # Case 1: First string is longer
    # -----------------------------
    if l1 > l2:

        i = 0
        j = 0
        diff = 0

        while i < l1 and j < l2:

            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                diff += 1

                if diff > 1:
                    return False

                # Skip one character from the longer string
                i += 1

        return True

    # ------------------------------
    # Case 2: Second string is longer
    # ------------------------------
    if l2 > l1:

        i = 0
        j = 0
        diff = 0

        while i < l1 and j < l2:

            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                diff += 1

                if diff > 1:
                    return False

                # Skip one character from the longer string
                j += 1

        return True

    # -----------------------
    # Case 3: Equal Length
    # -----------------------
    edits = 0

    i = 0
    j = 0

    while i < l1 and j < l2:

        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            edits += 1

            if edits > 1:
                return False

            i += 1
            j += 1

    return True


# Driver Code
print(edit_required("abc", "abd"))      # True
print(edit_required("abc", "abdc"))     # True
print(edit_required("abdc", "abc"))     # True
print(edit_required("abc", "axy"))      # False
print(edit_required("abc", "abc"))      # True
print(edit_required("", "a"))           # True
print(edit_required("a", ""))           # True
print(edit_required("", ""))            # True
