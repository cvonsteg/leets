"""
Problem Name: Palindrome Number
Difficulty: Easy
Runtime: 60ms (beats 70.96% of submissions)
Memory: 12.9MB (info not given, although min in distribution is 13.5 MB...)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == "".join(reversed(str(x)))
