/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler006
/// Author : liuyubobobo
/// Time   : 2017-09-24

#include <iostream>

using namespace std;

class Solution{

public:
    long long sumSquareDiff(int num){

        long long a = squareOfSum(num);
        long long b = sumOfSquare(num);
        return a - b;
    }

private:
    long long squareOfSum(int num){
        long long sum = ((long long)1 + (long long)num) * (long long)num / (long long)2;
        return sum * sum;
    }

    long long sumOfSquare(int num){
        long long one = (long long)1;
        long long lnum = (long long)num;
        return lnum * (lnum + one) * ((long long)2 * lnum + one) / (long long)6;
    }
};

int main() {

    int T;
    cin >> T;
    while(T --){
        int N;
        cin >> N;
        cout << Solution().sumSquareDiff(N) << endl;
    }

    return 0;
}