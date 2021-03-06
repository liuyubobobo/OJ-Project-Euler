/// Source : https://projecteuler.net/problem=67
/// Author : liuyubobobo
/// Time   : 2017-10-05

#include <iostream>
#include <vector>
#include <fstream>
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

    string filename = "p067_triangle.txt";
    ifstream file;
    file.open(filename);
    if(file.is_open()) {

        vector<vector<int> > numbers;
        string line;
        int i = 0;
        while(getline(file, line)) {
            stringstream ss(line);
            vector<int> v;
            for (int j = 0; j <= i; j++) {
                int t;
                ss >> t;
                v.push_back(t);
            }
            numbers.push_back(v);
            i ++;
        }

        cout << Solution().bestRoute(numbers) << endl;
        file.close();
    }
    else
        cout << "Open file " << filename << " error!" << endl;
    return 0;
}