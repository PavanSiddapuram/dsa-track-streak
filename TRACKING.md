# Progress Tracking

## Current status

- Foundations: usable, reinforced in context
- Big-O: working knowledge (reinforced difference between linear decrement vs halving)
- Current topic: Two Pointers — Day 1 completed
- Solved problem: Two Sum II (Input Array Is Sorted) — LeetCode 167

## Completed Checkpoints

### Day 1: Two Sum II (Sorted Array)
- [x] **Invariant in own words:** Moving left pointer rightwards strictly increases/maintains sum; moving right pointer leftwards strictly decreases/maintains sum. Safely eliminates candidates because smallest + largest boundaries prove no other pair can match.
- [x] **Hand trace:** Traced `[2, 7, 11, 15]`, target 9 step-by-step to `L=0, R=1`.
- [x] **From-scratch implementation:** Written and verified in Python (`days/day_01_two_sum_sorted.py`).
- [x] **$O(n)$ / $O(1)$ proof:** Each step reduces pointer separation by 1; maximum $n - 1$ steps with $O(1)$ work per step = $O(n)$ time, $O(1)$ auxiliary space.
- [x] **Misconception documented:** Initial thought was $O(n \log n)$; clarified that $\log n$ comes from division/halving (e.g. binary search), whereas stepping pointers by 1 is strictly linear $O(n)$.
- [x] **Edge case verification:** Tested negatives (`[-5, -3, 0, 2, 4]`), duplicates (`[1, 2, 2, 3, 5]`), and nonexistent targets.

## Recent strengths

- Understands that $n$ is input size and Big-O is growth rate.
- Accurately determined safe pointer movement from monotonic properties of sorted arrays.
- Implemented correct pointer termination condition (`left < right`) and boundary adjustments from scratch.
- Handled negative and duplicate edge cases cleanly with first-principles reasoning.

## Gaps reinforced this session

- **Linear vs Logarithmic:** Do not assume search/matching has a $\log n$ factor unless the search space is being geometrically halved. Constant-step inward moves are $O(n)$.

## Next checkpoint

- Two Pointers Problem 2 (e.g., Valid Palindrome or Container With Most Water / 3Sum) to test pointer movement and invariant identification on a fresh problem.
