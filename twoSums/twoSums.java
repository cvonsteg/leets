class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> val_map = new HashMap<Integer, Integer>();
        int result[] = new int[2];
        for(int i=0; i < nums.length; i++) {
            int rem = target - nums[i];
            if (val_map.containsKey(rem)){
                result[0] = val_map.get(rem);
                result[1] = i;
            }
            val_map.put(nums[i], i);
        }
        return result;
    }
}
