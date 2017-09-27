/// Source : https://projecteuler.net/problem=12
/// Author : liuyubobobo
/// Time   : 2017-09-27

#include <iostream>
#include <vector>

using namespace std;

class Solution{

public:
    long long firstNumberHasDivisorsOver(int n){

        long long num = (long long)1;
        long long step = (long long)2;

        while(true){
            if( divisorNumber(num) > n )
                return num;

            num += step;
            step += (long long)1;
        }
    }

private:
    int divisorNumber(long long num){

        if(num == (long long)1)
            return 1;

        vector<int> factorsNumber = getFactorsNumber(num);

        int res = 1;
        for(int i = 0 ; i < factorsNumber.size() ; i ++)
            res *= (factorsNumber[i] + 1);

        return res;
    }

    vector<int> getFactorsNumber(long long num){

        vector<int> res;

        if(num % (long long)2 == (long long)0){
            int k = 0;
            while(num % (long long)2 == (long long)0){
                k ++;
                num /= (long long)2;
            }
            res.push_back(k);
        }

        for(long long i = 3 ; i*i <= num ; i += (long long)2){
            if(num % i == (long long)0){
                int k = 0;
                while(num % i == (long long)0){
                    k ++;
                    num /= i;
                }
                res.push_back(k);
            }
        }

        if(num != (long long)1)
            res.push_back(1);

        return res;
    };
};

int main() {

    cout << Solution().firstNumberHasDivisorsOver(500) << endl;

    return 0;
}