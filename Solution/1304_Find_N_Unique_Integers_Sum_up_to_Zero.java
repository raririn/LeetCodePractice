class Solution {
    public int[] sumZero(int n) {
        int[] ret = new int[n];
        int delta = 2;
        for (int i = 0; i < n; i++){
            ret[i] = delta * i - n + 1;
        }
        return ret;
    }
}

/*
Runtime: 0 ms, faster than 100.00% of Java online submissions for Find N Unique Integers Sum up to Zero.
Memory Usage: 37.4 MB, less than 100.00% of Java online submissions for Find N Unique Integers Sum up to Zero.
*/