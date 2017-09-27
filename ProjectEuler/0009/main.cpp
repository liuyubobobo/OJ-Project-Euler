/// Source : https://projecteuler.net/problem=9
/// Author : liuyubobobo
/// Time   : 2017-09-27

#include <iostream>

using namespace std;

class Solution{

public:
    long long abc(int N){
        for(int a = 1 ; a <= N - 2 ; a ++)
            for(int b = a + 1 ; b <= N - 1 ; b ++)
                if(a*a + b*b == (N-a-b)*(N-a-b))
                    return (long long)a * (long long)b * (long long)(N-a-b);

        return -1;
    }
};

int main() {

    cout << Solution().abc(1000) << endl;

    return 0;
}