/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler067
/// Author : liuyubobobo
/// Time   : 2017-10-05

#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

class Solution{

public:
    int bestRoute(const vector<vector<int>> triangle){
        vector<vector<int>> res(2, vector<int>(triangle[triangle.size()-1].size(), -1));
        res[0][0] = triangle[0][0];
        for(int i = 1 ; i < triangle.size() ; i ++){
            res[i%2][0] = res[(i-1)%2][0] + triangle[i][0];
            for(int j = 1 ; j < i ; j ++)
                res[i%2][j] = max(res[(i-1)%2][j-1], res[(i-1)%2][j]) + triangle[i][j];
            res[i%2][i] = res[(i-1)%2][i-1] + triangle[i][i];
        }

        int lastRow = (triangle.size() - 1) % 2;
        int maxRes = 0;
        for(int i = 0 ; i < res[lastRow].size() ; i ++)
            maxRes = max(maxRes, res[lastRow][i]);
        return maxRes;
    }
};

int main() {

    int T;
    cin >> T;
    while(T --) {
        int row;
        cin >> row;

        vector<vector<int> > numbers;
        for (int i = 0; i < row; i++) {
            vector<int> v;
            for (int j = 0; j <= i; j++) {
                int t;
                cin >> t;
                v.push_back(t);
            }
            numbers.push_back(v);
        }

        cout << Solution().bestRoute(numbers) << endl;
    }
    return 0;
}