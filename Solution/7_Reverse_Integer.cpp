class Solution {
public:
/*
Take care of the possible overflow!
*/
    int reverse(int x) {
        int ret = 0;
        int y = 0;
        while (x){
            y = x % 10;
            ret = 10 * ret + y;
            x = x / 10;
            if ((ret > INT_MAX/10 && x > 0) || (ret < INT_MIN/10 && x < 0)){
                return 0;
            }
        }
        return ret;
    }
};