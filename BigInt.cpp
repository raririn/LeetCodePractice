#include <vector>
#include <algorithm>
#include <iostream>
#include <string>

using namespace std;


class BigInt{

private:
    bool sign;
    vector<vector<int>> val;

public:
    BigInt(){
    };

    BigInt (string s){
        vector<int> tmp;
        if (s.at(0) == '-'){
            sign = false;
            for (int i = 1; i < s.length(); i++){
                if (i % 4 == 0){
                    val.push_back(tmp);
                    tmp.clear();
                }
                tmp.push_back(s.at(i));
            }
            if (!tmp.empty()){
                val.push_back(tmp);
            }
        }
        else{
            sign = true;
            for (int i = 0; i < s.length(); i++){
                if (i % 4 == 3){
                    val.push_back(tmp);
                    tmp.clear();
                }
                tmp.push_back(s.at(i));
            }
            if (!tmp.empty()){
                val.push_back(tmp);
            }
        }
    };

    BigInt operator + (BigInt const &rhs){
        BigInt ret;
    }



};