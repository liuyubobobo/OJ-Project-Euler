/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler015
/// Author : liuyubobobo
/// Time   : 2017-09-27

/***
 * The answer is C(m+n, m) or C(m+n, n)
 *
 * In a grid of size m by n, we know that no matter what path we take,
 * there will be exactly m movements to the right (R) and n movements down (D).
 * This means the pathway can be represented as a string of R’s and D’s
 * of length m + n.
 */

#include <iostream>

using namespace std;

class Solution{

private:
    const int MOD = 1000000007;
    int maxN, maxM;
    int** ctable;

public:
    Solution(int maxN, int maxM){
        this->maxN = maxN;
        this->maxM = maxM;

        int len_n = (maxN + maxM + 1);
        int len_m = ((maxN + maxM)/2 + 1);
        ctable = new int*[len_n];
        for(int i = 0 ; i < len_n ; i ++){
            ctable[i] = new int[len_m];
            for(int j = 0 ; j < len_m ; j ++)
                ctable[i][j] = -1;
        }
    }

    ~Solution(){
        int len_n = (maxN + maxM + 1);
        for(int i = 0 ; i < len_n ; i ++)
            delete[] ctable[i];
        delete[] ctable;
    }

    int routeNumber(int n, int m){
        return C(n+m, n);
    }

private:
    int C(int m, int n){

        if(m-n < n)
            return C(m, m-n);

        if(n == 0)
            return 1;

        if(m == n)
            return 1;

        if(ctable[m][n] != -1)
            return ctable[m][n];

        return ctable[m][n] = (C(m-1, n) + C(m-1, n-1)) % MOD;
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