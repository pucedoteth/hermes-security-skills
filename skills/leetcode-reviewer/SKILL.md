---
name: leetcode-reviewer
description: Review LeetCode solutions for time/space complexity and suggest optimizations
version: 1.0.0
metadata:
  hermes:
    tags: [coding, algorithms, interview]
    category: education
---

# LeetCode Reviewer

## When to Use
Use this when the user shares a LeetCode solution or asks for help with a coding problem.

## Procedure
1. Identify the problem name/number if given.
2. Analyze the provided solution for time complexity (Big O).
3. Analyze space complexity.
4. Suggest 1-2 optimizations or alternative approaches.
5. Explain the algorithmic pattern used (e.g., sliding window, two pointers, DFS).

## Pitfalls
- **Premature optimization**: Don't suggest micro-optimizations that hurt readability.
- **Wrong complexity**: Double-check nested loops and recursive calls.
- **Missing edge cases**: Point out if empty input, single element, or max constraints aren't handled.

## Verification
Confirm the optimized solution handles all edge cases and has better or equal complexity.
