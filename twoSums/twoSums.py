Class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_dict = {}
        result = []
        for idx, val in enumerate(nums):
            rem = target - val
            if rem in val_dict:
                result.append(idx)
                result.append(val_dict[rem])
            val_dict[val] = idx
        return result
