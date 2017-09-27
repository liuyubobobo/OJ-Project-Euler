/// Source : https://projecteuler.net/problem=8
/// Author : liuyubobobo
/// Time   : 2017-09-26

#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

class Solution{

public:
    long long greatestProduct(const string &digits, int num){

        vector<int> d;

        for(int i = 0 ; i < digits.size() ; i ++)
            d.push_back(digits[i] - '0');

        long long tres = (long long)1;
        for(int i = 0 ; i < num ; i ++)
            tres *= (long long)d[i];
        long long maxres = tres;

        for(int i = num ; i <= d.size() - num ; i ++){

            if(d[i-num] != 0){
                tres /= (long long)d[i-num];
                tres *= (long long)d[i];
            }
            else{
                tres = (long long)1;
                for(int j = i-num+1 ; j <= i ; j ++)
                    tres *= (long long)d[j];
            }

            maxres = max(maxres, tres);
        }

        return maxres;
    }
};

int main() {

    int T;
    (cin >> T).get();
    while(T --){
        int N, K;
        (cin >> N >> K).get();

        string str;
        getline(cin, str);

        cout << Solution().greatestProduct(str, K) << endl;
    }

    return 0;
}