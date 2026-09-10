# DSA → CP → ICPC Roadmap

## North Star

Become capable of solving unfamiliar algorithmic problems from first principles, then progressively build competitive-programming and ICPC-level speed, mathematics, algorithms, and proof skills.

## Kanban Board

### 🟦 BACKLOG

- [ ] Foundations: Big-O, complexity, recurrences
- [ ] Arrays / strings
- [ ] Hashing
- [ ] Two pointers
- [ ] Fast/slow pointers
- [ ] Prefix sums
- [ ] Sliding window
- [ ] Sorting
- [ ] Binary search
- [ ] Linked lists
- [ ] Stack / queue / deque
- [ ] Monotonic stack / queue
- [ ] Trees / BST
- [ ] DFS / BFS
- [ ] Heaps / priority queues
- [ ] Tries
- [ ] Intervals / sweep line
- [ ] Graph fundamentals
- [ ] Topological sorting
- [ ] DSU
- [ ] Shortest paths
- [ ] Greedy
- [ ] Backtracking
- [ ] Dynamic programming
- [ ] Bit manipulation
- [ ] Number theory
- [ ] Combinatorics
- [ ] Fenwick tree
- [ ] Segment tree
- [ ] Binary lifting
- [ ] Advanced graph algorithms
- [ ] Contest implementation speed
- [ ] Codeforces rated progression
- [ ] ICPC problem sets
- [ ] ICPC team simulation

### 🟨 IN PROGRESS

- [ ] Two Pointers — Day 1
  - [ ] Invariant
  - [ ] Constraint signature
  - [ ] Hand trace
  - [ ] Implementation
  - [ ] Complexity proof
  - [ ] 3 independent variations

### 🟩 REVIEW

- [ ] Big-O / complexity

### ✅ MASTERED

> A topic moves here only after fresh, unlabeled problems can be solved without copying a template.

## 2-Hour Daily Loop

1. **25 min — Concept:** intuition, invariant, applicability.
2. **20 min — Dry run:** tiny example + edge cases.
3. **35 min — Implementation:** from scratch; no solution lookup initially.
4. **40 min — Error journal:** missed clue, invariant, edge case, complexity, and the information that would make the next decision obvious.

## Problem Progression

For each major pattern:

- 2 guided problems
- 3 easy independent problems
- 5 medium problems
- 1 unlabeled/mixed problem
- spaced repetition at +2 days, +7 days, +21 days

## Phase 0 — Foundations

Big-O, Theta/Omega, time vs auxiliary space, simplification, sequential vs nested work, recurrence intuition, constraints → feasible complexity, GCD/modulo, bitwise basics.

**Exit:** derive complexity from unfamiliar code and justify it.

## Phase 1 — Arrays & Core Patterns

Two pointers, fast/slow, hashing, prefix sums, frequency counting, sliding windows, sorting as preprocessing.

Suggested problems: Two Sum II, 3Sum, Container With Most Water, Longest Substring Without Repeating Characters, Minimum Size Subarray Sum, Trapping Rain Water.

## Phase 2 — Linear Structures

Python lists, linked lists, stacks, queues, deque, monotonic stack/queue.

Suggested problems: Reverse Linked List, Linked List Cycle, Daily Temperatures, Next Greater Element, Largest Rectangle in Histogram.

## Phase 3 — Search & Trees

Binary search, lower/upper bound, binary search on answer, binary trees, BST, DFS/BFS, height, diameter, path sums, LCA.

## Phase 4 — Heaps, Tries & Intervals

Heap invariants, Top-K, K-way merge, streaming median, tries, interval merging/scheduling, sweep line.

## Phase 5 — Graphs

Representations, BFS/DFS, components, cycles, bipartite graphs, topological sorting, DSU, Dijkstra, 0-1 BFS, MST.

## Phase 6 — Recursion, Backtracking & DP

Call stack, decision trees, subsets/permutations/combinations, pruning, memoization, tabulation, state/transition/base case, 1D/2D DP, knapsack, LIS, edit distance, tree DP, bitmask DP.

## Phase 7 — Competitive Programming

Fast I/O, implementation speed, coordinate compression, Fenwick tree, segment tree, sparse table/RMQ, number theory, sieve, factorization, modular arithmetic, combinatorics, probability basics, meet-in-the-middle, offline processing, advanced greedy and graph techniques.

Suggested rating progression: Codeforces 800–1000 → 1100–1300 → 1400–1600 → 1700–1900 → 2000+.

## Phase 8 — ICPC

Team communication, problem triage, parallel solving, proof under time pressure, contest debugging, partial scoring, upsolving, regional problem sets, and full contest simulation.

Cycle: **Contest → upsolve → write clean explanation → reattempt later.**

## Resources

### Easy / Visual

- VisuAlgo — visual algorithms and data structures.
- LeetCode Explore — structured beginner-to-interview topic paths.
- NeetCode — approachable pattern explanations and problem progression.
- Python docs for `collections`, `heapq`, `bisect` — implementation reference.

### Core Reference

- CP-Algorithms — deep competitive-programming algorithm/data-structure reference.
- USACO Guide — structured CP curriculum and progression.

### Contest Practice

- Codeforces — rated problems, tags, and contests.
- AtCoder — high-quality algorithmic contest practice.
- ICPC archives / regional problem sets — later-stage practice.

**Fallback rule:** If a primary explanation feels hard, use a visual/easy explanation first, then return to the formal reference. We will add easier resources topic-by-topic rather than forcing one source.

## Mastery Checklist

A topic is mastered only when you can:

- recognize when it applies,
- explain why it works,
- state and preserve the invariant,
- derive it from constraints,
- implement without copying,
- handle edge cases,
- prove correctness,
- prove complexity,
- solve an unfamiliar problem where the pattern is not announced.
