/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler003
/// Author : liuyubobobo
/// Time   : 2017-09-23

#include <iostream>
#include <cmath>

using namespace std;

class Solution{

public:
    long long largestPrimeFactor(long long num){

        if(num == (long long)1)
            return 1;

        if(num <= (long long)0)
            return 0;

        long long res;
        if(num % (long long)2 == 0)
            res = (long long)2;
        else
            res = (long long)1;

        num = removeFactor(num, (long long)2);
        int factorLimit = (int)sqrt(num);
        for(int i = 3 ; i <= factorLimit && num != (long long)1; i += 2)
            if(num % (long long)i == 0){
                res = (long long)i;
                num = removeFactor(num, (long long)i);
            }

        res = max(res, num);
        return res;
    }

private:
    long long removeFactor(long long num, long long factor){
        while(num % factor == 0)
            num /= factor;
        return num;
    }
};

int main() {

    int T;
    cin >> T;
    while(T --) {
        long long num;
        cin >> num;
        cout << Solution().largestPrimeFactor(num) << endl;
    }

    return 0;
}