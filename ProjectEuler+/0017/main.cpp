/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler017
/// Author : liuyubobobo
/// Time   : 2017-10-05

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution{

private:
    string basicWord[20] = {
            "Zero",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen"
    };
    string tenthWord[10] = {
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety"
    };
    string space = " ";
    string hundred = "Hundred";
    string thousand = "Thousand";
    string million = "Million";
    string billion = "Billion";

public:
    string numberToWord(long long num){

        if(num < (long long)20)
            return basicWord[num];

        if(num <= (long long)99){
            string res = tenthWord[num/(long long)10];
            if(num % (long long)10)
                res += space + numberToWord(num%(long long)10);
            return res;
        }

        if(num <= (long long)999){
            string res = basicWord[num/(long long)100] + space + hundred;
            if(num % (long long)100)
                res += space + numberToWord(num%(long long)100);
            return res;
        }

        if(num <= (long long)999999){
            string res = numberToWord(num/(long long)1000) + space + thousand;
            if(num % (long long)1000)
                res += space + numberToWord(num%(long long)1000);
            return res;
        }

        if(num <= (long long)999999999){
            string res = numberToWord(num/(long long)1000000) + space + million;
            if(num % (long long)1000000)
                res += space + numberToWord(num%(long long)1000000);
            return res;
        }

        if(num <= (long long)999999999999){
            string res = numberToWord(num/(long long)1000000000) + space + billion;
            if(num%(long long)1000000000)
                res += space + numberToWord(num%(long long)1000000000);
            return res;
        }

        return "";
    }

};

int main() {

    int T;
    cin >> T;
    while(T --){
        long long num;
        cin >> num;
        cout << Solution().numberToWord(num) << endl;
    }


    return 0;
}