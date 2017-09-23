/// Source : https://projecteuler.net/problem=4
/// Author : liuyubobobo
/// Time   : 2017-09-23

#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution{

public:
    int largestPalindromeFrom(int digits){

        int smallest = (int)pow(10, digits - 1);
        int largest = (int)pow(10, digits) - 1;
        int res = -1;
        for(int i = largest ; i >= smallest ; i --)
            for(int j = i ; j >= smallest ; j --){
                int tres = i * j;
                if(tres > res && isPalindrome(tres))
                    res = tres;
            }
        return res;
    }

private:
    bool isPalindrome(int num){

        int n = num;
        int rev = 0;
        while(n){
            int dig = n % 10;
            rev = rev * 10 + dig;
            n /= 10;
        }
        return rev == num;
    }
};

int main() {

    cout << Solution().largestPalindromeFrom(3) << endl;

    return 0;
}