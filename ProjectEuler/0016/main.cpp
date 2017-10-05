/// Source : https://projecteuler.net/problem=16
/// Author : liuyubobobo
/// Time   : 2017-10-05

#include <iostream>
#include <vector>

using namespace std;

class Solution{

public:
    int sumOfDigits(int power){

        vector<int> res = powerOf2(power);
        // printVector(res);

        int sum = 0;
        for(int digit : res)
            sum += digit;
        return sum;
    }

private:
    vector<int> powerOf2(int power){

        if(power == 0)
            return vector<int>(1, 1);

        if(power == 1)
            return vector<int>(1, 2);

        // cout << power << " : " << endl;
        vector<int> halfRes1 = powerOf2(power/2);
        // printVector(halfRes1);
        vector<int> halfRes2(halfRes1.begin(), halfRes1.end());
        if(power % 2 == 0)
            return mul(halfRes1, halfRes2);
        else
            return mul(mul(halfRes1, halfRes2), 2);
    }

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

    cout << Solution().sumOfDigits(1000) << endl;

    return 0;
}