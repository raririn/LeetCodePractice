class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n <= 0){
            return 0;
        }
        while (n > 2){
            if (n % 2 != 0){
                return 0;
            }
            n = n / 2;
        }
        return 1;
    }
};

/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Power of Two.
Memory Usage: 8.1 MB, less than 76.00% of C++ online submissions for Power of Two.

Personally thought best answer
https://leetcode.com/problems/power-of-two/discuss/379320/Constant-time-and-memory-complexity.-One-line-easy-solution-with-explanation.
*/