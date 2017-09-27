/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler009
/// Author : liuyubobobo
/// Time   : 2017-09-27

#include <iostream>
#include <unordered_map>
#include <cmath>

using namespace std;

class Solution{

private:
    unordered_map<int, long long> res;

public:
    Solution(int maxN){

        for(int a = 1 ; a <= maxN - 2 ; a ++)
            for(int b = a + 1 ; b <= maxN - 1 ; b ++){
                int csquare = a*a + b*b;
                int c = (int)sqrt((double)csquare);
                if(c <= maxN && c*c == csquare){
                    int N = a + b + c;
                    if(res.find(N) == res.end())
                        res.insert(make_pair(N, (long long)a * (long long)b * (long long)c));
                    else
                        res[N] = max(res[N], (long long)a * (long long)b * (long long)c);
                }
            }
    }

    long long abc(int N){
        if(res.find(N) == res.end())
            return -1;
        return res[N];
    }
};

int main() {

    int maxN = 3000;
    Solution solution(maxN);

    int T;
    cin >> T;
    while(T --) {
        int N;
        cin >> N;
        cout << solution.abc(N) << endl;
    }

    return 0;
}