class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int slow = 0;
        for (int i = 0; i < nums.size(); i++){
            if (nums[i]){
                nums[slow] = nums[i];
                slow++;
            }
        }
        for (int i = slow; i < nums.size(); i++){
            nums[i] = 0;
        }
    }
};

/*
Runtime: 16 ms, faster than 61.70% of C++ online submissions for Move Zeroes.
Memory Usage: 9.4 MB, less than 100.00% of C++ online submissions for Move Zeroes.
*/