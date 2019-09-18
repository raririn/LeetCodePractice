class Solution {
public:
    string toLowerCase(string str) {
        for (char& c: str){
            if (c >= 'A') && (c <= 'Z'){
                c += ('a' - 'A');
            }
        }
        return str;
    }
};

/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for To Lower Case.
Memory Usage: 8.1 MB, less than 100.00% of C++ online submissions for To Lower Case.
*/