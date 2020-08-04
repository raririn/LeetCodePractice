class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int i = 0;
        for (int j = i; j < nums.length; j++) {
            if (nums[i] != nums[j]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i+1;
    }
}

/*
Runtime: 1 ms, faster than 50.28% of Java online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 45.3 MB, less than 5.17% of Java online submissions for Remove Duplicates from Sorted Array.
*/