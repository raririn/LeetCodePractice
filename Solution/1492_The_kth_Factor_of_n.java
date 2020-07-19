class Solution {
    public int kthFactor(int n, int k) {
        int count = 0;
        if (n == 1 || k == 1) {
            return 1;
        }
        for (int i=1; i<=n; i++) {
            if (n % i == 0) {
                count += 1;
                if (count >= k) {
                    return i;
                }
            }
        }
        return -1;
    }
}


/*
Runtime: 1 ms, faster than 80.86% of Java online submissions for The kth Factor of n.
Memory Usage: 38.2 MB, less than 50.00% of Java online submissions for The kth Factor of n.
*/