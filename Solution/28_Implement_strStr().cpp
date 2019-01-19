class Solution {
public:
    int strStr(string haystack, string needle) {
        int size_h = haystack.size();
        int size_n = needle.size();
        if (needle.empty()){
            return 0;
        }
        for (int i = 0; i < size_h - size_n + 1; i++){
            int flag = 0;
            for (int j = 0; j < size_n; j++){
                if (haystack[i + j] != needle[j]){
                    break;
                }
                if (j == size_n - 1){
                    flag = 1;
                }
            }
            if (flag){
                return i;
            }
        }
        return -1;
    }
};