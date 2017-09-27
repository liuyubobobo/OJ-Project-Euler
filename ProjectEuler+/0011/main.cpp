/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler011
/// Author : liuyubobobo
/// Time   : 2017-09-27

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cassert>

using namespace std;

class Solution{

private:
    int N = 20, M = 20;
    int d[4][2] = {{0,1}, {1,0}, {1,1}, {-1,1}};

public:
    int largestProduct(const vector<vector<int>> g){

        assert(g.size() == N);
        for(int i = 0 ; i < N ; i ++)
            assert(g[i].size() == M);

        int res = -1;
        for(int i = 0 ; i < N ; i ++)
            for(int j = 0 ; j < M ; j ++)
                for(int k = 0 ; k < 4 ; k ++){
                    if(!inArea(i + 3*d[k][0], j + 3*d[k][1]))
                        continue;

                    int i1 = i, j1 = j;
                    int i2 = i1 + d[k][0], j2 = j1 + d[k][1];
                    int i3 = i2 + d[k][0], j3 = j2 + d[k][1];
                    int i4 = i3 + d[k][0], j4 = j3 + d[k][1];

                    res = max(res, g[i1][j1] * g[i2][j2] * g[i3][j3] * g[i4][j4]);
                }

        return res;
    }

private:
    bool inArea(int x, int y){
        return x >= 0 && x < N && y >= 0 && y < M;
    }
};

int main() {

    int N = 20, M = 20;
    vector<vector<int>> g(N, vector<int>(M, 0));

    string s;
    for(int i = 0 ; i < N ; i ++){
        getline(cin, s);
        stringstream ss(s);
        for(int j = 0 ; j < M ; j ++)
            ss >> g[i][j];
    }

    cout << Solution().largestProduct(g) << endl;

    return 0;
}