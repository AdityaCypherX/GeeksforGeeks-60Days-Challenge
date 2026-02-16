Day 02 – Chocolate Distribution Problem
🧠 Problem Statement
Given chocolate packets and m students, distribute exactly one packet per student such that:
Maximum chocolates - Minimum chocolates → minimum
Return that minimum difference.

💡 Core Idea
This is a Sorting + Sliding Window problem.
If we sort the array:
The minimum difference will always lie in a continuous window of size m.

🛠 Approach
Sort the array.
Use a sliding window of size m.
For each window:
difference = arr[i+m-1] - arr[i]

Return minimum difference.
Time Complexity:O(n log n) (Sorting)
Space Complexity:O(1)
