/// Source : https://projecteuler.net/problem=7
/// Author : liuyubobobo
/// Time   : 2017-09-26

#include <iostream>
#include <vector>

using namespace std;

class Solution{

public:
    int prime(int n){

        if(n <= 0)
            return 1;

        vector<int> primes;
        primes.push_back(2);
        for(int i = 3; primes.size() < n ; i += 2){

            bool isPrime = true;
            for(int j = 0 ; j < primes.size() && primes[j] * primes[j] <= i ; j ++)
                if(i % primes[j] == 0){
                    isPrime = false;
                    break;
                }

            if(isPrime)
                primes.push_back(i);
        }

        return primes[n-1];
    }
};

int main() {

    cout << Solution().prime(10001) << endl;

    return 0;
}