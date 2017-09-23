/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler004
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
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution{

private:
    vector<int> sortedPalindromes;
public:
    Solution(){

        unordered_set<int> palindromes;

        int smallest = 100;
        int largest = 999;
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
                if(isPalindrome(tres) && palindromes.find(tres) == palindromes.end())
                    sortedPalindromes.push_back(tres);
            }
        }

        sort(sortedPalindromes.begin(), sortedPalindromes.end());
    }

    int largestPalindromeLessThan(int N){

        vector<int>::iterator iter =
                lower_bound(sortedPalindromes.begin(), sortedPalindromes.end(), N);

        return *(iter-1);
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

    int T;
    cin >> T;

    Solution solution = Solution();
    while(T --){
        int N;
        cin >> N;
        cout << solution.largestPalindromeLessThan(N) << endl;
    }
    return 0;
}