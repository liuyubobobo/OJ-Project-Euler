/// Source : https://projecteuler.net/problem=4
/// Author : liuyubobobo
/// Time   : 2017-09-23

/***
 * If P is a product of two 3 digits, then P must be 6 digits.
 * Since P is a palindrome, we can express P as following:
 *
 * P = 100000x + 10000y + 1000z + 100z + 10y + x
 * P = 100001x + 10010y + 1100z
 * P = 11 * (9091x + 910y + 100z)
 *
 * We can see P has a factor 11, which can make us search faster
 */

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
        for(int i = largest ; i >= smallest ; i --){
            int j, step;
            if(i % 11 == 0){
                j = largest;
                step = 1;
            }
            else{
                j = 990;
                step = 11;
            }
            for(; j >= smallest ; j -= step){
                int tres = i * j;
                if(tres > res && isPalindrome(tres))
                    res = tres;
            }
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