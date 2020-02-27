class Solution {
    public int maximum69Number (int num) {
        int temp = num;
        int six_idx = -1;
        for (int i = 1; temp > 0; i *= 10, temp /= 10){
            if (temp % 10 == 6){
                six_idx = i;
            }
        }
        return six_idx == -1 ? num : num + 3 * six_idx;
    }
}

/*
Runtime: 0 ms, faster than 100.00% of Java online submissions for Maximum 69 Number.
Memory Usage: 35.9 MB, less than 100.00% of Java online submissions for Maximum 69 Number.
*/