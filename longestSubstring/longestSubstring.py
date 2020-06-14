"""
Problem Name: Longest Substring without Repeating Characters
Difficulty: Medium
Runtime: 52ms (beats 90.02% of submissions)
Memory: 14MB (beats 34.71% of submissions)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l_str = ''
        for ltr in s:
            if ltr not in l_str:
                l_str += ltr
            else:
                longest = max(longest, len(l_str))
                ltr_idx = l_str.find(ltr)
                l_str = l_str[ltr_idx + 1:]
                l_str += ltr
        longest = max(longest, len(l_str))
        return longest
