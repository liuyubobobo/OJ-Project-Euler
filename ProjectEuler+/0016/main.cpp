/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler016
/// Author : liuyubobobo
/// Time   : 2017-10-05

#include <iostream>
#include <vector>

using namespace std;

class Solution{

private:
    vector<vector<int> > powerOf2;

public:
    Solution(int maxPower){
        powerOf2.push_back(vector<int>(1, 1));
        for(int i = 1 ; i <= maxPower; i ++)
            powerOf2.push_back(mul(powerOf2[i-1], 2));
    }

    int sumOfDigits(int power){

        int sum = 0;
        for(int digit : powerOf2[power])
            sum += digit;
        return sum;
    }

private:
    vector<int> add(const vector<int> &num1, const vector<int> num2){

        vector<int> sum(num1.begin(), num1.end());

        while(sum.size() < num2.size())
            sum.push_back(0);

        for(int i = 0 ; i < num2.size() ; i ++)
            sum[i] += num2[i];

        int k = 0;
        for(int i = 0 ; i < sum.size() ; i ++){
            sum[i] += k;

            int t = sum[i];
            sum[i] = t%10;
            k = t/10;
        }

        if(k)
            sum.push_back(k);

        return sum;
    }

    vector<int> mul(const vector<int> &num1, const vector<int> &num2){
        vector<int> res(1, 0);
        for(int i = 0 ; i < num2.size() ; i ++){
            vector<int> t = mul(num1, num2[i]);
            vector<int> num(i, 0);
            for(int digit: t)
                num.push_back(digit);
            res = add(res, num);
        }
        return res;
    }

    vector<int> mul(const vector<int> &num, const int scalar){
        vector<int> res(num.begin(), num.end());

        for(int i = 0 ; i < res.size() ; i ++)
            res[i] *= scalar;

        int k = 0;
        for(int i = 0 ; i < res.size() ; i ++){
            res[i] += k;
            k = res[i]/10;
            res[i] = res[i]%10;
        }

        if(k)
            res.push_back(k);

        return res;
    }

    void printVector(const vector<int> v){
        for(int digit: v)
            cout << digit;
        cout << endl;
    }
};

int main() {

    int maxPower = 10000;
    Solution solution(maxPower);

    int T;
    cin >> T;
    while(T --) {
        int N;
        cin >> N;
        cout << solution.sumOfDigits(N) << endl;
    }

    return 0;
}