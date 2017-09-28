/// Source : https://projecteuler.net/problem=15
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
    int maxN, maxM;
    long long** ctable;

public:
    Solution(int maxN, int maxM){
        this->maxN = maxN;
        this->maxM = maxM;

        int len_n = (maxN + maxM + 1);
        int len_m = ((maxN + maxM)/2 + 1);
        ctable = new long long*[len_n];
        for(int i = 0 ; i < len_n ; i ++){
            ctable[i] = new long long[len_m];
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

    long long routeNumber(int n, int m){
        return C(n+m, n);
    }

private:
    long long C(int m, int n){

        if(m-n < n)
            return C(m, m-n);

        if(n == 0)
            return (long long)1;

        if(m == n)
            return (long long)1;

        if(ctable[m][n] != -1)
            return ctable[m][n];

        return ctable[m][n] = C(m-1, n) + C(m-1, n-1);
    }
};

int main() {

    Solution solution(20, 20);

    cout << solution.routeNumber(2, 2) << endl;
    cout << solution.routeNumber(20, 20) << endl;

    return 0;
}