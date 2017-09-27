/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler010
/// Author : liuyubobobo
/// Time   : 2017-09-27

#include <iostream>
#include <vector>

using namespace std;

class Solution{

    vector<int> primes;
    vector<long long> sum;

public:
    Solution(int maxN){

        if(maxN <= 1)
            return;

        primes.push_back(2);
        sum.push_back((long long)2);
        for(int i = 3; i <= maxN ; i += 2){

            bool isPrime = true;
            for(int j = 0 ; j < primes.size() && primes[j] * primes[j] <= i ; j ++)
                if(i % primes[j] == 0){
                    isPrime = false;
                    break;
                }

            if(isPrime){
                primes.push_back(i);
                sum.push_back(sum[sum.size()-1] + (long long)i);
            }
        }
    }

    long long sumOfPrimes(int n){
        vector<int>::iterator iter = lower_bound(primes.begin(), primes.end(), n);
        int index;
        if(*iter == n)
            index = iter - primes.begin();
        else
            index = iter - primes.begin() - 1;

        return sum[index];
    }
};

int main() {

    Solution solution(1000000);

    int T;
    cin >> T;
    while(T --) {
        int N;
        cin >> N;
        cout << solution.sumOfPrimes(N) << endl;
    }

    return 0;
}