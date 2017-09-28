/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler015
/// Author : liuyubobobo
/// Time   : 2017-09-27

#include <iostream>

using namespace std;

class Solution{

private:
    const int MOD = 1000000007;
    int maxN, maxM;
    int* res;

public:
    Solution(int maxN, int maxM){
        this->maxN = maxN;
        this->maxM = maxM;

        int len  = (maxN + 1) * (maxM + 1);
        res = new int[len];
        for(int i = 0 ; i < len ; i ++)
            res[i] = 0;

        res[0] = 1;
        for(int j = 1 ; j <= maxM ; j ++)
            res[j] = res[j-1];

        for(int i = 1 ; i <= maxN ; i ++)
            res[i*(maxM+1)] = res[(i-1)*(maxM+1)];

        for(int i = 1 ; i <= maxN ; i ++)
            for(int j = 1 ; j <= maxM ; j ++)
                res[i*(maxM+1) + j] = (res[(i-1)*(maxM+1) + j] + res[i*(maxM+1) + j-1]) % MOD;

    }

    ~Solution(){
        delete[] res;
    }

    int routeNumber(int n, int m){
        return res[n * (maxM+1) + m];
    }

};

int main() {

    int maxN = 500, maxM = 500;
    Solution solution(maxN, maxM);

    int T;
    cin >> T;
    while(T --) {
        int n, m;
        cin >> n >> m;
        cout << solution.routeNumber(n, m) << endl;
    }

    return 0;
}