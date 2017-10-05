/// Source : https://projecteuler.net/problem=18
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

    string numsStrings[] = {
            "75",
            "95 64",
            "17 47 82",
            "18 35 87 10",
            "20 04 82 47 65",
            "19 01 23 75 03 34",
            "88 02 77 73 07 63 67",
            "99 65 04 28 06 16 70 92",
            "41 41 26 56 83 40 80 70 33",
            "41 48 72 33 47 32 37 16 94 29",
            "53 71 44 65 25 43 91 52 97 51 14",
            "70 11 33 28 77 73 17 78 39 68 17 57",
            "91 71 52 38 17 14 91 43 58 50 27 29 48",
            "63 66 04 68 89 53 67 30 73 16 69 87 40 31",
            "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
    };
    int row = 15;

    vector<vector<int> > numbers;
    for(int i = 0 ; i < row ; i ++){
        stringstream ss(numsStrings[i]);
        vector<int> v;
        for(int j = 0 ; j<= i ; j ++){
            int t;
            ss >> t;
            v.push_back(t);
        }
        numbers.push_back(v);
    }

    cout << Solution().bestRoute(numbers) << endl;

    return 0;
}