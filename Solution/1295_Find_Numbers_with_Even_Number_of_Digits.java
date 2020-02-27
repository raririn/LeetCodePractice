class Solution {
    public int findNumbers(int[] nums) {
        int ret = 0;
        for (int i = 0; i < nums.length; i++){
            if ((nums[i] > 9 && nums[i] < 100) || (nums[i] > 999 && nums[i] < 10000)){
                ret++;
            }
        }
        return ret;
    }
}

/*
Runtime: 0 ms, faster than 100.00% of Java online submissions for Find Numbers with Even Number of Digits.
Memory Usage: 38.6 MB, less than 100.00% of Java online submissions for Find Numbers with Even Number of Digits.
*/