class Solution {
    public int[] runningSum(int[] nums) {
        int[] ret = new int[nums.length];
        ret[0] = nums[0];
        for (int i=1; i<nums.length; i++) {
            ret[i] = ret[i-1] + nums[i];
        }
        return ret;
    }
}

/*
Runtime: 0 ms, faster than 100.00% of Java online submissions for Running Sum of 1d Array.
Memory Usage: 39.9 MB, less than 50.00% of Java online submissions for Running Sum of 1d Array.
*/