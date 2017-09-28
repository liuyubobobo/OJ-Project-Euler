/// Source : https://projecteuler.net/problem=15
/// Author : liuyubobobo
/// Time   : 2017-09-27

#include <iostream>

using namespace std;

class Solution{

private:
    int maxN, maxM;
    long long* res;

public:
    Solution(int maxN, int maxM){
        this->maxN = maxN;
        this->maxM = maxM;

        int len  = (maxN + 1) * (maxM + 1);
        res = new long long[len];
        for(int i = 0 ; i < len ; i ++)
            res[i] = 0;

        res[0] = (long long)1;
        for(int j = 1 ; j <= maxM ; j ++)
            res[j] = res[j-1];

        for(int i = 1 ; i <= maxN ; i ++)
            res[i*(maxM+1)] = res[(i-1)*(maxM+1)];

        for(int i = 1 ; i <= maxN ; i ++)
            for(int j = 1 ; j <= maxM ; j ++)
                res[i*(maxM+1) + j] = res[(i-1)*(maxM+1) + j] + res[i*(maxM+1) + j-1];

//        for(int i = 0 ; i <= maxN ; i ++) {
//            for (int j = 0; j <= maxM; j++)
//                cout << res[i * (maxM + 1) + j] << "\t";
//            cout << endl;
//        }
    }

    ~Solution(){
        delete[] res;
    }

    long long routeNumber(int n, int m){
        return res[n * (maxM+1) + m];
    }

};

int main() {

    Solution solution(20, 20);

    cout << solution.routeNumber(2, 2) << endl;
    cout << solution.routeNumber(20, 20) << endl;

    return 0;
}