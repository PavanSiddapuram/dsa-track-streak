# Day 01 — Two Pointers

## Goal

Derive the two-pointer technique from the structure of a sorted search space rather than memorizing a template.

## Problem 1 — Two Sum II

Given a sorted array numbers and a target, find two distinct indices whose values sum to target.

Example:
numbers = [2, 7, 11, 15]
target = 9

Expected pair: 2 + 7 = 9.

## Learning sequence

### A. Understand
- What exactly is being asked?
- What does “sorted” give us?

### B. Constraints
Estimate what happens with:
- O(n^2) pair checking
- O(n) scan with additional storage
- O(n) two-pointer scan

### C. Brute force
Describe the obvious pair enumeration and derive why it is O(n^2).

### D. Bottleneck
The brute-force method keeps reconsidering many pairs.

### E. Information question
What information would make the next decision obvious?

### F. Invariant
State, in plain language, what candidate pairs remain possible between the left and right boundaries.

### G. Trace
Trace [2, 7, 11, 15], target 9:
- L=0, R=3
- sum=17, too large: determine which pointer can safely move
- continue until the pair is found

### H. Implementation
Python, from scratch. Prefer a minimal loop with two indices.

### I. Proof
Explain why moving the chosen pointer cannot discard a valid solution.

### J. Complexity
Target:
- Time: O(n)
- Auxiliary space: O(1)

## Follow-ups

1. Target pair may not exist.
2. Duplicates are present.
3. Return values instead of indices.
4. 3Sum as a composition of sorting + two pointers.
5. Unlabeled problem where two pointers must be recognized from clues.

## Mastery gate

Do not mark Two Pointers mastered until Pavan can explain why the pointer movement is safe on a fresh problem and can identify when the technique does not apply.
