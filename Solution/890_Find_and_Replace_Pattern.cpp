class Solution {
public:
    int generatePattern(string pattern){
        string::iterator si;
        unordered_map<char, int> umap;
        int count = 0;
        int ret = 0;
        
        for (si = pattern.begin(); si < pattern.end(); si++){
            if (umap.find(*si) == umap.end()){
                count += 1;
                umap[*si] = count;
                ret *= 26;
                ret += umap[*si];
                ret = ret % 10000;
            }
            else{
                ret *= 26;
                ret += umap[*si];
                ret = ret % 10000;
            }
        }
        return ret;
    }

    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        int pattern_i = generatePattern(pattern);
        vector<string> ret;
        for (auto i = words.begin(); i < words.end(); i++){
            if (pattern_i == generatePattern(*i)){
                ret.push_back(*i);
            }
        }
        return ret;
    }
};

/*
Runtime: 12 ms, faster than 5.72% of C++ online submissions for Find and Replace Pattern.
Memory Usage: 8.5 MB, less than 100.00% of C++ online submissions for Find and Replace Pattern.
*/