/// Source : https://projecteuler.net/problem=2
/// Author : liuyubobobo
/// Time   : 2017-09-23

#include <iostream>

using namespace std;

class Solution{

public:
    int sumOfEvenValues(int limit){

        if(limit <= 1)
            return 0;

        int fib[2] = {1, 2};
        int cur = 1;
        int sum = 0;
        int nextfib = 2;
        while(nextfib <= limit){

            if(nextfib % 2 == 0)
                sum += nextfib;

            nextfib = fib[0] + fib[1];
            cur ++;
            fib[cur&1] = nextfib;
        }

        return sum;
    }
};

int main() {

    cout << Solution().sumOfEvenValues(4000000) << endl;

    return 0;
}