class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        auto v1 = nums1.begin();
        auto v2 = nums2.begin();
        vector<int> res;
        while (v1 < nums1.end() && v2 < nums2.end()){
            if (*v1 == *v2){
                res.push_back(*v1);
                v1++;
                v2++;
            }
            else if (*v1 < * v2){
                v1++;
            }
            else{
                v2++;
            }
        }
        return res;
    }
};

/*
Runtime: 4 ms, faster than 99.16% of C++ online submissions for Intersection of Two Arrays II.
Memory Usage: 6.6 MB, less than 100.00% of C++ online submissions for Intersection of Two Arrays II.
*/