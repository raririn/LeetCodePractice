class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        vector<int> dp;
        int last = 0;
        for (auto i = arr.begin(); i < arr.end(); i++){
            last = last^(*i);
            dp.push_back(last);
        }

        vector<int> ret;
        for (auto i = queries.begin(); i < queries.end(); i++){
            vector<int> query = *i;
            int s = query[0];
            int e = query.at(1);
            if (!s){
                ret.push_back(dp[e]);
            }
            else{
                ret.push_back(dp[s-1] ^ dp[e]);
            }
            
        }
        return ret;
    }
};

/*
Runtime: 180 ms, faster than 16.53% of C++ online submissions for XOR Queries of a Subarray.
Memory Usage: 28.6 MB, less than 100.00% of C++ online submissions for XOR Queries of a Subarray.
*/