class Solution {
public:
    int minDistance(string word1, string word2) {
        int length_w1 = word1.size();
        int length_w2 = word2.size();
        int dp[length_w1+1][length_w2+1];
        // Boundary conditions
        for (int i = 0; i <= length_w1; i++){
            dp[i][0] = i;
        }
        for (int j = 0; j <= length_w2; j++){
            dp[0][j] = j;
        }
        for (int i = 1; i <= length_w1; i++){
            for (int j = 1; j <= length_w2; j++){
                if (word1[i-1] == word2[j-1]){
                    dp[i][j] = dp[i-1][j-1];
                }
                else{
                    dp[i][j] = min(dp[i-1][j-1]+1, min(dp[i-1][j]+1, dp[i][j-1]+1));
                }
            }
        }
        return dp[length_w1][length_w2];
    }
};