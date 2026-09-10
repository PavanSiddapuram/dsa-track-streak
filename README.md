# DSA Track Streak

A long-term DSA → Competitive Programming → ICPC preparation system, built around problem-solving ability rather than memorizing patterns.

## North Star

Build the algorithmic thinking required to be competitive for top software engineering interviews and eventually reach serious Competitive Programming / ICPC level.

> The goal is not to "finish DSA". The goal is to become someone who can see a problem, model it, derive an approach, prove it, implement it, and debug it under constraints.

## The Learning Loop

For every new problem:

1. **Understand** — restate the problem and identify the input/output.
2. **Constraint signature** — estimate what complexity can survive.
3. **Brute force** — write the obvious solution first.
4. **Bottleneck** — identify what makes brute force too slow.
5. **Information question** — _What information would make the next decision obvious?_ 
6. **Invariant** — state what must remain true during the algorithm.
7. **Visual trace** — dry-run the smallest useful example and edge cases.
8. **Implementation** — write Python from scratch before looking at a solution.
9. **Proof** — explain correctness and why the invariant is preserved.
10. **Complexity** — prove time and auxiliary-space complexity.
11. **Postmortem** — record the mistake, missed clue, and reusable pattern.

## Kanban

### 🟦 Backlog

- Foundations: math, Big-O, recurrence intuition, bit operations
- Arrays and strings
- Hashing / frequency maps
- Prefix sums / difference arrays
- Two pointers
- Fast & slow pointers
- Sliding window
- Sorting fundamentals
- Binary search and binary search on answer
- Linked lists
- Stacks / queues / deque
- Monotonic stack / queue
- Trees / BST
- DFS / BFS
- Heaps / priority queues
- Tries
- Intervals / sweep line
- Graph representation and traversal
- Topological sort
- DSU / Union-Find
- Shortest paths
- Greedy algorithms
- Recursion / backtracking
- Dynamic programming
- Bitmask DP / state compression
- Number theory / combinatorics
- Advanced data structures
- Competitive programming implementation speed
- Codeforces contests
- ICPC-style team problem solving

### 🟨 In Progress

- **Two Pointers — Day 1**
  - [ ] Understand the invariant
  - [ ] Solve sorted two-sum by hand
  - [ ] Code without reference
  - [ ] Prove O(n) time / O(1) extra space
  - [ ] Solve 3 follow-up variations

### 🟩 Review

Move a topic here after initial learning. Review using spaced repetition and fresh problems.

### ✅ Mastered

Only move a topic here after you can solve unfamiliar medium problems without relying on a memorized template.

## Roadmap

### Phase 0 — Foundations

**Goal:** Learn to reason about algorithms.

- Big-O / Big-Theta / Big-Omega
- Time vs auxiliary space
- Constants and lower-order terms
- Sequential vs nested complexity
- Basic recurrences
- Input constraints → feasible complexity
- Modular arithmetic / GCD
- Bitwise operators

**Exit test:** Given unfamiliar code, derive its complexity and explain why.

### Phase 1 — Core Array Patterns

**Goal:** Turn arrays from loops into structured search spaces.

- Two pointers
- Fast/slow pointers
- Prefix sums
- Hash maps / sets
- Frequency counting
- Fixed and dynamic sliding windows
- Sorting as a preprocessing tool

Core problems:
- Two Sum II
- 3Sum
- Remove Duplicates
- Container With Most Water
- Longest Substring Without Repeating Characters
- Minimum Size Subarray Sum
- Trapping Rain Water

### Phase 2 — Linear Data Structures

- Python list internals
- Linked lists
- Stack
- Queue
- Deque
- Monotonic stack
- Monotonic queue

Core problems:
- Reverse Linked List
- Linked List Cycle
- Daily Temperatures
- Next Greater Element
- Largest Rectangle in Histogram

### Phase 3 — Search + Trees

- Binary search
- Lower/upper bound
- Search on answer
- Binary trees
- BST
- Recursive DFS
- Iterative DFS
- BFS / level order
- Tree height, diameter, path sums
- Lowest Common Ancestor

### Phase 4 — Heaps, Tries, Intervals

- Heap invariants
- Top-K
- K-way merge
- Streaming median
- Trie
- Interval merging
- Interval scheduling
- Sweep-line intuition

### Phase 5 — Graphs

- Adjacency list / matrix
- BFS / DFS
- Connected components
- Cycle detection
- Bipartite graphs
- Topological sorting / Kahn
- DAG reasoning
- DSU / Union-Find
- Dijkstra
- 0-1 BFS
- Minimum spanning tree

### Phase 6 — Recursion, Backtracking, DP

- Recursion and call stack
- Decision trees
- Subsets / permutations / combinations
- Pruning
- Memoization
- Tabulation
- State / transition / base case
- 1D DP
- 2D DP
- Knapsack
- LIS
- Edit distance
- Tree DP
- Bitmask/state compression

### Phase 7 — Competitive Programming Core

Transition from interview-style DSA to contest problem solving.

- Fast input/output
- Implementation discipline
- Prefix / difference techniques
- Binary lifting
- Fenwick tree
- Segment tree
- Sparse table / RMQ intuition
- Modular arithmetic
- Prime sieve
- Factorization
- Combinatorics
- Probability basics
- Coordinate compression
- Sweep line
- Meet-in-the-middle
- Offline processing
- Greedy proofs
- Advanced graph algorithms

Practice progression:

**LeetCode / basic implementation → Codeforces 800–1000 → 1100–1300 → 1400–1600 → 1700–1900 → 2000+**

Codeforces exposes problem ratings and tags, which make it useful for controlled progression. citeturn886553search0

### Phase 8 — ICPC Track

The target is not merely a rating number. Train the contest skillset:

- Team communication
- Parallel problem triage
- Choosing which problems to attack first
- Proof under time pressure
- Contest debugging
- Partial scoring / subtasks
- Post-contest upsolving
- Regional/National contest simulation

A strong cycle:

**Contest → mark unsolved problems → upsolve → write editorial-quality notes → reattempt later without notes.**

## 2-Hour Daily Protocol

### 25 min — Concept

Learn the idea, invariant, and when it is applicable.

### 20 min — Dry Run

Use a tiny example. Draw pointers, states, queues, stacks, graph frontiers, or DP tables.

### 35 min — Implementation

Code from scratch. No autocomplete or solution lookup during the first serious attempt.

### 40 min — Error Journal

Record:

- What clue did I miss?
- What invariant did I violate?
- What edge case broke me?
- What complexity mistake did I make?
- What information would have made the next decision obvious?

## Problem Difficulty Protocol

Don't rush to medium/hard problems.

**Easy:** learn the pattern.

**Easy+:** vary the pattern.

**Medium:** derive it from constraints and clues.

**Hard:** combine multiple ideas and prove the approach.

For every major pattern, solve:

- 2 guided problems
- 3 independent easy problems
- 5 medium problems
- 1 mixed/unlabeled problem

Then revisit after a gap.

## Resource Shelf

### Gentle Foundations

- **VisuAlgo** — visual demonstrations of data structures and algorithms.
- **LeetCode Explore** — structured topic cards and guided learning paths. citeturn886553search12
- **NeetCode** — approachable explanations and pattern-oriented problem lists.
- **Python `collections` / `heapq` / `bisect` documentation** — use when a standard-library primitive is part of the solution.

### Strong DSA Reference

- **CP-Algorithms** — reference for algorithms and data structures used in competitive programming.
- **USACO Guide** — structured competitive-programming curriculum with topic progression.

### Competitive Programming

- **Codeforces Problemset** — use rating + tags to progress systematically; the current problemset exposes both difficulty ratings and topic tags. citeturn886553search0
- **Codeforces contests** — contest-speed practice.
- **AtCoder** — clean problem statements and strong fundamentals practice.
- **ICPC archives / regional problem sets** — later-stage contest preparation.

### When a topic feels too hard

We will deliberately add a second, simpler resource rather than forcing a single difficult explanation.

Default fallback order:

**simple visual explanation → guided problem → our own explanation → formal reference → implementation → harder problems.**

## Review System

Use spaced repetition instead of rereading whole chapters.

- **Same day:** explain from memory.
- **+2 days:** solve one fresh problem.
- **+7 days:** solve one unlabeled problem.
- **+21 days:** timed mixed problem.
- **Before contest/interview:** rapid pattern and invariant review.

## Mistake Journal Template

```text
Problem:
Pattern:
My first approach:
Where it failed:
Missed clue:
Invariant:
Better information/state:
Correct complexity:
Edge case I missed:
Reusable lesson:
```

## Mastery Standard

A topic is **not mastered** because you watched a video or solved one problem.

Move it to Mastered only when you can:

- recognize when the technique applies,
- explain why it works,
- state and maintain the invariant,
- derive the solution from constraints,
- implement it without copying,
- handle edge cases,
- prove its complexity,
- and solve a fresh problem where the pattern is not announced.

## Long-Term North Star

### Stage A — Interview-capable

Strong fundamentals + common patterns + consistent medium-problem solving.

### Stage B — Contest-capable

Regular Codeforces/AtCoder participation, faster implementation, stronger math and graph fundamentals.

### Stage C — ICPC-capable

Team contests, advanced algorithms, rigorous proofs, upsolving, and time-pressure execution.

### Stage D — Elite trajectory

2000+ Codeforces-level problem solving, advanced data structures/algorithms, contest experience, and sustained independent study.

The purpose of this repository is to make progress visible and make every failure useful.
