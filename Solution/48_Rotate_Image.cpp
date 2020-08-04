class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        const int R = matrix.size();
        const int C = matrix[0].size();

        reverse(matrix.begin(), matrix.end());

        for (int i=0; i<R; ++i) {
            for (int j=i+1; j<C; ++j) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
    }
};

/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Rotate Image.
Memory Usage: 7.1 MB, less than 84.46% of C++ online submissions for Rotate Image.
*/