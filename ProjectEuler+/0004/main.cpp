/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler004
/// Author : liuyubobobo
/// Time   : 2017-09-23

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
        for(int i = smallest ; i <= largest ; i ++)
            for(int j = smallest ; j <= largest ; j ++){
                int tres = i * j;
                if(isPalindrome(tres) && palindromes.find(tres) == palindromes.end())
                    sortedPalindromes.push_back(tres);
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