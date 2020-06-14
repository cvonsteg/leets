"""
Problem Name: Median of Two Sorted Arrays
Difficulty: Hard
Runtime: 104ms (beats 34% of submissions)
Memory: 14.1MB (beats 45.79% of submissions)
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        mid, mod = divmod(total, 2)
        # if mod == 0, median = idx[mid] + idx[mid-1] / 2
        srted = []
        idx1 = 0 
        idx2 = 0
        while len(srted) <= mid:
            v1 = nums1[idx1] if idx1 < len(nums1) else None
            v2 = nums2[idx2] if idx2 < len(nums2) else None
            if (v1 is None):
                srted.append(v2)
                idx2 += 1
            elif (v2 is None):
                srted.append(v1)
                idx1 += 1
            elif (v2 < v1):
                srted.append(v2)
                idx2 += 1
            elif (v1 < v2):
                srted.append(v1)
                idx1 += 1
            else:
                srted.append(v1)
                idx1 += 1
        
        if mod == 0:
            med = (srted[-2] + srted[-1]) / 2
        else:
            med = srted[-1]
        return med
