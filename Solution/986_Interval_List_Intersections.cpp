class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& A, vector<vector<int>>& B) {
        auto v1 = A.begin();
        auto v2 = B.begin();
        vector<vector<int>> res;
        while (v1 < A.end() && v2 < B.end()){
            vector<int> a = *v1;
            vector<int> b = *v2;

            if (a[1] < b[0]){
                v1++;
            }
            else if (b[1] < a[0]){
                v2++;
            }
            else{
                vector<int> tmp = {max(a[0], b[0]), min(a[1], b[1])};
                if (a[1] == b[1]){
                    v1++;
                    v2++;
                }
                else if (tmp[1] == a[1]){
                    v1++;
                }
                else{
                    v2++;
                }
                res.push_back(tmp);
            }
        }
        return res;
    }
};

/*
Runtime: 84 ms, faster than 7.07% of C++ online submissions for Interval List Intersections.
Memory Usage: 15.8 MB, less than 80.00% of C++ online submissions for Interval List Intersections.
*/