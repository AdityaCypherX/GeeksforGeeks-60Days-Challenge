📅 Day 4 – Maximum Number of Overlapping Intervals

#GeekStreak60 | GeeksforGeeks POTD | Difficulty: Hard

🧠 Problem Statement

Given an array of intervals arr[][], where each interval is represented by two integers [start, end] (inclusive), return the maximum number of intervals that overlap at any point in time.

📌 Example
Input:
[[1, 2], [2, 4], [3, 6]]

Output:
2

Explanation:

The maximum overlapping intervals are 2.

💡 Approach – Sweep Line Algorithm

Instead of checking every pair (which would take O(n²) time), we use an optimized approach:

✅ Steps:

Separate all start times and end times into two arrays.

Sort both arrays.

Use two pointers to simulate a timeline.

If start[i] <= end[j], increase current overlap.

Otherwise, decrease overlap.

Track the maximum overlap encountered.

Since intervals are inclusive, we must use <=.

🧮 Time & Space Complexity
Complexity	Value
Time	O(n log n)
Space	O(n)
