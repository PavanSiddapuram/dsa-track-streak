# Day 01 — Two Pointers

## Goal

Derive the two-pointer technique from the structure of a sorted search space rather than memorizing a template.

---

## Problem 1 — Two Sum II (Input Array Is Sorted)

Given a 1-indexed (or 0-indexed) array of integers `numbers` that is already sorted in non-decreasing order, find two distinct indices whose values sum to `target`.

**Example:**
- `numbers = [2, 7, 11, 15]`, `target = 9`
- Expected pair: `2 + 7 = 9` -> indices `[0, 1]` (0-indexed) or `[1, 2]` (1-indexed).

---

## Derivation & Learning Sequence

### A. Understand
- **Goal:** Find two distinct elements that add up to `target`.
- **Key Property:** The array is sorted in non-decreasing order ($A[i] \le A[i+1]$).
  - Moving rightward increases or keeps values the same.
  - Moving leftward decreases or keeps values the same.

### B. Constraints & Complexity Targets
- **Brute force:** Check all pairs $(i, j)$ with $i < j \implies O(n^2)$ time, $O(1)$ space.
- **Hash Map:** Store complements in a dictionary $\implies O(n)$ time, $O(n)$ space.
- **Two Pointers:** Leverage sorted order $\implies O(n)$ time, $O(1)$ auxiliary space.

### C. Invariant & Elimination Proof (Why moving a pointer is 100% safe)

Let the active candidate search space be defined by bounds `[left, right]`.
- All pairs containing elements outside `[left, right]` have already been proven invalid and eliminated.
- Let `current_sum = numbers[left] + numbers[right]`.

1. **If `current_sum > target`:**
   - Because `numbers[left]` is the *smallest* available element in the current candidate window, pairing `numbers[right]` with ANY other number in `[left, right]` would give a sum $\ge \text{current\_sum} > \text{target}$.
   - Thus, `numbers[right]` cannot pair with *any* valid candidate.
   - **Safe action:** Discard `right` permanently by doing `right -= 1`.

2. **If `current_sum < target`:**
   - Because `numbers[right]` is the *largest* available element in the current candidate window, pairing `numbers[left]` with ANY other number in `[left, right]` would give a sum $\le \text{current\_sum} < \text{target}$.
   - Thus, `numbers[left]` cannot pair with *any* valid candidate.
   - **Safe action:** Discard `left` permanently by doing `left += 1`.

3. **If `current_sum == target`:**
   - We have found the target pair.

### D. Hand Trace

Tracing `numbers = [2, 7, 11, 15]`, `target = 9`:

| Step | Left ($L$) | Right ($R$) | Value at $L$ | Value at $R$ | Sum | Comparison | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `0` | `3` | `2` | `15` | `17` | $17 > 9$ (too large) | `right -= 1` |
| 2 | `0` | `2` | `2` | `11` | `13` | $13 > 9$ (too large) | `right -= 1` |
| 3 | `0` | `1` | `2` | `7`  | `9`  | $9 == 9$ (match!)   | Return `[0, 1]` |

---

### E. Python Implementation

```python
def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    """
    Find two distinct elements in a sorted array that sum to target.
    Returns 0-indexed indices [left, right], or [] if no pair exists.
    (For LeetCode 167 1-indexed output: return [left + 1, right + 1])
    """
    left = 0
    right = len(numbers) - 1

    # Loop terminates when left == right because distinct indices are required
    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            # Need a larger sum: advance the left pointer
            left += 1
        else:
            # Need a smaller sum: decrement the right pointer
            right -= 1

    return []
```

---

### F. Complexity Analysis

- **Time Complexity: $O(n)$**
  - In every iteration of the loop, either `left` increases by 1 or `right` decreases by 1.
  - The initial distance between pointers is $n - 1$.
  - The pointers only move inward and cannot cross; the loop runs at most $n - 1$ times.
  - Each iteration performs $O(1)$ constant-time arithmetic and comparison.
  - Total time: at most $(n - 1) \times O(1) = O(n)$.
  - *Distinction:* It is NOT $O(n \log n)$ or $O(\log n)$. Logarithmic time requires dividing/halving the search space per step. Stepping by 1 is strictly linear.

- **Space Complexity: $O(1)$**
  - Only two integer pointers (`left`, `right`) and a scalar (`current_sum`) are stored. No extra collections are allocated.

---

### G. Edge Cases & Observations

1. **Negative numbers:**
   - e.g., `numbers = [-5, -3, 0, 2, 4]`, `target = -1`.
   - The logic holds completely because the array is sorted. Moving `left` rightward increases values algebraically (makes sum less negative / more positive); moving `right` leftward decreases values algebraically.
2. **Duplicate numbers:**
   - e.g., `numbers = [1, 2, 2, 3, 5]`, `target = 4`.
   - The array remains non-decreasing. Moving a pointer across duplicates may yield the same sum temporarily, but it never moves in the wrong direction and will evaluate valid pairs correctly.
3. **No pair exists:**
   - Pointers meet (`left == right`), loop ends cleanly, returns `[]`.

---

## Postmortem & Reusable Takeaways

- **When to think of Two Pointers:** When the search space has a monotonic direction (e.g. sorted array, palindrome checking, inward bounding).
- **Core Requirement:** Each comparison must give a *definitive reason* to safely discard an entire row/column/element from future consideration.
- **Stepping vs Halving:** Moving pointers by 1 each step yields $O(n)$ linear time, unlike binary search which cuts the remaining space by half each step to achieve $O(\log n)$.
