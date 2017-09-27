/// Source : https://projecteuler.net/problem=10
/// Author : liuyubobobo
/// Time   : 2017-09-27

#include <iostream>
#include <vector>

using namespace std;

class Solution{

    vector<int> primes;

public:
    Solution(int maxN){

        if(maxN <= 1)
            return;

        primes.push_back(2);
        for(int i = 3; i <= maxN ; i += 2){

            bool isPrime = true;
            for(int j = 0 ; j < primes.size() && primes[j] * primes[j] <= i ; j ++)
                if(i % primes[j] == 0){
                    isPrime = false;
                    break;
                }

            if(isPrime)
                primes.push_back(i);
        }
    }

    long long sumOfPrimes(int n){
        long long sum = (long long)0;
        for(int i = 0 ; i < primes.size() && primes[i] <= n ; i ++)
            sum += (long long)primes[i];
        return sum;
    }
};

int main() {

    Solution solution(2000000);
    cout << solution.sumOfPrimes(2000000) << endl;

    return 0;
}