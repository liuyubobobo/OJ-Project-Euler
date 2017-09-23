/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler002
/// Author : liuyubobobo
/// Time   : 2017-09-23

#include <iostream>
#include <vector>

using namespace std;

class Solution{

private:
    vector<long long> fibs;
    vector<long long> sums;

public:
    Solution(long long maxNumber){
        fibs.push_back((long long)1);
        sums.push_back((long long)0);

        long long nextfib = (long long)2;
        while(nextfib <= maxNumber){
            fibs.push_back(nextfib);
            if(nextfib % 2 == 0)
                sums.push_back(*(sums.end()-1) + nextfib);
            else
                sums.push_back(*(sums.end()-1));

            nextfib = *(fibs.end()-1) + *(fibs.end()-2);
        }
    }

    long long sumOfEvenValues(long long limit){

        if(limit <= (long long)1)
            return (long long)0;

        vector<long long>::iterator iter = lower_bound(fibs.begin(), fibs.end(), limit);
        int index = iter - fibs.begin();
        if(*iter == limit)
            return sums[index];
        else
            return sums[index-1];
    }
};

int main() {

    Solution solution(40000000000000000);

    int T;
    cin >> T;
    while(T--) {
        long long limit;
        cin >> limit;
        cout << solution.sumOfEvenValues(limit) << endl;
    }

    return 0;
}