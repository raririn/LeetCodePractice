class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ret;
        sort(nums.begin(), nums.end());
        int i = 0;
        while (i < nums.size()){
            int sum_inloop = -nums.at(i);
            if (sum_inloop < 0){
                break;
            }

            int lo = i + 1;
            int hi = nums.size() - 1;
            while (lo < hi){
                if (nums.at(lo) + nums.at(hi) < sum_inloop){
                    lo++;
                }
                else if (nums.at(lo) + nums.at(hi) > sum_inloop){
                    hi--;
                }
                else{
                    vector<int> tmp = {nums.at(i), nums.at(hi), nums.at(lo)};
                    ret.push_back(tmp);
                    while ((lo < hi) && nums.at(lo) == tmp[2]){
                        lo++;
                    } 
                    while ((lo < hi) && nums.at(hi) == tmp[1]){
                        hi--;
                    }                    
                }
            }
            while (i+1 < nums.size() && nums.at(i) == nums.at(i+1)){
                i++;
            }
            i++;
        }
        return ret;
    }
};

/*
Runtime: 96 ms, faster than 84.83% of C++ online submissions for 3Sum.
Memory Usage: 15.3 MB, less than 50.00% of C++ online submissions for 3Sum.
*/