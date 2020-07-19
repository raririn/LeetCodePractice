class Solution {
    public int findSpecialInteger(int[] arr) {
        int last = arr[0];
        int count = 0;
        int baseline = arr.length / 4;
        for (int cur: arr) {
            if (cur == last) {
                count += 1;
                if (count > baseline) {
                    return cur;
                }
            }
            else {
                count = 1;
            }
            last = cur;
        }
        return -1;
    }
}

/*
Runtime: 1 ms, faster than 50.87% of Java online submissions for Element Appearing More Than 25% In Sorted Array.
Memory Usage: 44.8 MB, less than 8.66% of Java online submissions for Element Appearing More Than 25% In Sorted Array.
*/