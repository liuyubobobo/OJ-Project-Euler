/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler013
/// Author : liuyubobobo
/// Time   : 2017-09-27

#include <iostream>
#include <string>
#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;

class Solution{

public:

    long long firstTenDigits(const vector<string> &numberStrs){

        vector<int> sum;
        for(int i = 0 ; i < numberStrs[0].size() ; i ++)
            sum.push_back(numberStrs[0][i] - '0');
        reverse(sum.begin(), sum.end());

        for(int i = 1 ; i < numberStrs.size() ; i ++){

            vector<int> num;
            for(int j = 0 ; j < numberStrs[i].size() ; j ++)
                num.push_back(numberStrs[i][j] - '0');
            reverse(num.begin(), num.end());

            add(sum, num);
        }

        long long res = (long long)0;
        for(int i = sum.size() - 1 ; i >= sum.size() - 10 ; i --)
            res = res * (long long)10 + (long long)sum[i];
        return res;
    }

private:
    void add(vector<int> &sum, const vector<int> &num){

        while(sum.size() < num.size())
            sum.push_back(0);

        for(int i = 0 ; i < num.size() ; i ++)
            sum[i] += num[i];

        int k = 0;
        for(int i = 0 ; i < sum.size() ; i ++){
            sum[i] += k;

            int t = sum[i];
            sum[i] = t%10;
            k = t/10;
        }

        if(k)
            sum.push_back(k);
    }

};

int main() {

    int N;
    (cin >> N).get();

    vector<string> numbers;
    string s;
    for(int i = 0 ; i < N ; i ++){
        getline(cin, s);
        numbers.push_back(s);
    }

    cout << Solution().firstTenDigits(numbers) << endl;

    return 0;
}