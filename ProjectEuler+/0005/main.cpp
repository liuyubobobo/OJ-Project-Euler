/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler005
/// Author : liuyubobobo
/// Time   : 2017-09-23

#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>

using namespace std;

class Solution{

private:
    vector<int> primes;
    vector<unordered_map<int,int>> factorsVec;

public:

    Solution(int max_num){

        primes = findAllPrimes(max_num);
        for(int i = 0 ; i <= max_num ; i ++){
            unordered_map<int, int> numFactors = factorize(i);
            factorsVec.push_back(numFactors);
        }
    }

    long long smallestNumberDivisibleByAllNumbers(int num){

        unordered_map<int, int> factors;
        for(int i = 2 ; i <= num ; i ++){
            unordered_map<int, int> numFactors = factorsVec[i];
            //cout << "num = "<< i << endl;

            for(unordered_map<int,int>::iterator iter = numFactors.begin() ;
                    iter != numFactors.end() ; iter ++){
                int prime = (*iter).first;
                int freq = (*iter).second;
                //cout << prime << " : " << freq << endl;
                if(factors.find(prime) == factors.end())
                    factors.insert(make_pair(prime, freq));
                else
                    factors[prime] = max(factors[prime], freq);
            }
        }

        long long res = (long long)1;
        for(unordered_map<int,int>::iterator iter = factors.begin() ;
            iter != factors.end() ; iter ++)
            res *= (long long)pow((*iter).first, (*iter).second);

        return res;
    }

private:
    vector<int> findAllPrimes(int num){

        if(num <= 1)
            return vector<int>();

        vector<int> primes;
        primes.push_back(2);
        for(int i = 3 ; i <= num ; i += 2){
            bool isPrime = true;
            for(int j = 0 ; j < primes.size() && primes[j]*primes[j] <= i ; j ++)
                if(i % primes[j] == 0){
                    isPrime = false;
                    break;
                }
            if(isPrime)
                primes.push_back(i);
        }

        return primes;
    }

    unordered_map<int, int> factorize(int num){

        unordered_map<int, int> res;
        for(int i = 0 ; i < primes.size() && primes[i] <= num ; i ++)
            if(num % primes[i] == 0){
                int k = 0;
                while(num % primes[i] == 0){
                    num /= primes[i];
                    k ++;
                }
                res.insert(make_pair(primes[i], k));
            }

        if(num != 1)
            res.insert(make_pair(num, 1));

        return res;
    };
};

int main() {

    Solution solution(40);

    int T;
    cin >> T;
    while(T --) {
        int N;
        cin >> N;
        cout << solution.smallestNumberDivisibleByAllNumbers(N) << endl;
    }
    return 0;
}