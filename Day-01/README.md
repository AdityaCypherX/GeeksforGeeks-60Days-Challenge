Day 01 – Painter's Partition Problem-II
🧠 Problem Statement
Given an array arr[] representing board lengths and k painters, each painter paints contiguous boards only.
Each unit length takes 1 unit time.
Find the minimum time required to paint all boards.

💡 Core Idea
This is a Binary Search on Answer problem.
We are not searching in the array —
We are searching for the minimum possible maximum time.

Why Binary Search?
Minimum possible time = max(arr)
Maximum possible time = sum(arr)
Answer lies between them.
For a guessed time mid, we:
Check if we can paint all boards using ≤ k painters.
If possible → try smaller time.
If not → increase time.

🛠 Approach
Set:
low = max(arr)
high = sum(arr)

Apply Binary Search
Use a helper function to check feasibility
Return minimum valid time
Time Complexity:O(n log(sum - max))
Space Complexity:O(1)
