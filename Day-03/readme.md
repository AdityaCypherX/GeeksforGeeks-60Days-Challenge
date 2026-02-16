
📅 Day 03 – Meeting Rooms
🧠 Problem Statement
Given meeting intervals, determine whether a person can attend all meetings.
A meeting can be attended only if:
next_start >= previous_end

💡 Core Idea
This is an Interval Overlapping problem.
If two intervals overlap → answer is False.

🛠 Approach
Sort intervals by start time.
Traverse from second interval.
If:
arr[i][0] < arr[i-1][1]

→ Overlap detected → return False
If no overlap → return True

⏱ Time Complexity
O(n log n)
Space Complexity:O(1)
