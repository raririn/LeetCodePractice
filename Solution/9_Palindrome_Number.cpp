class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 and x != 0)){
            return false;
        }
        /*
        Note: consider 10.
        1st loop: rev = 0, x = 1. x >rev
        2nd loop: rev = 0, x = 0. WARNING: x == rev
        Why does this take place? Be aware that 0 is a special case!
        */
        int rev = 0;
        while (x > rev){
            rev *= 10;
            rev += x % 10;
            x /= 10;
        }
        return (x == rev) || (x == rev / 10);
    }
};