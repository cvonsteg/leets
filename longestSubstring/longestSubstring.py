class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        lngth = len(s)
        for idx, ltr in enumerate(s):
            new_str = ltr
            idx += 1
            while idx < lngth:
                tmp = s[idx]
                if tmp in new_str:
                    break
                else:
                    new_str += tmp
                    idx += 1               
            if len(new_str) > longest:
                longest = len(new_str)
        return longest
