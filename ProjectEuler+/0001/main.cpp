/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler001
/// Author : liuyubobobo
/// Time   : 2017-09-23

#include <iostream>

using namespace std;

class Solution{

public:
    long long sumOf3and5(int num){

        int lastNumber = num - 1;

        long long sumOf3 = sumOf(3, 3, (lastNumber/3)*3);
        long long sumOf5 = sumOf(5, 5, (lastNumber/5)*5);
        long long sumOf15 = sumOf(15, 15, (lastNumber/15)*15);

        return sumOf3 + sumOf5 - sumOf15;
    }

private:
    long long sumOf(int multiple, int startNumber, int endNumber){

        if(endNumber < startNumber)
            return 0;

        int num = (endNumber - startNumber) / multiple + 1;
        return (long long)(startNumber + endNumber) * (long long)num / (long long)2;
    }
};

int main() {

    int T;
    cin >> T;
    while(T --) {
        int num;
        cin >> num;
        cout << Solution().sumOf3and5(num) << endl;
    }
    return 0;
}