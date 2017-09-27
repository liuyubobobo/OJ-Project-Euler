/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler007
/// Author : liuyubobobo
/// Time   : 2017-09-26

#include <iostream>
#include <vector>

using namespace std;

class Solution{

    vector<int> primes;

public:
    Solution(int maxN){

        if(maxN < 1)
            return;

        primes.push_back(2);
        for(int i = 3; primes.size() < maxN ; i += 2){

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

    int prime(int n){
        return primes[n-1];
    }
};

int main() {

    int N = 10000;
    Solution solution(N);

    int T;
    cin >> T;
    while(T --) {
        int n;
        cin >> n;
        cout << solution.prime(n) << endl;
    }
    return 0;
}