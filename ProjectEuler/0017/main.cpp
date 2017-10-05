/// Source : https://projecteuler.net/problem=17
/// Author : liuyubobobo
/// Time   : 2017-10-05

#include <iostream>
#include <vector>

using namespace std;

class Solution{

private:
    int basicCounts[20] = {
            4, // zero
            3, // one
            3, // two
            5, // three
            4, // four
            4, // five
            3, // six
            5, // seven
            5, // eight
            4, // nine
            3, // ten
            6, // eleven
            6, // twelve
            8, // thirteen
            8, // fourteen
            7, // fifteen
            7, // sixteen
            9, // seventeen
            8, // eighteen
            8  // nineteen
    };
    int tenthCounts[10] = {
            0, // 0
            0, // 10
            6, // twenty
            6, // thirty
            5, // forty
            5, // fifty
            5, // sixty
            7, // seventy
            6, // eighty
            6 // ninety
    };
    int hundred = 7;
    int thousand = 8;
    int million = 7;
    int billion = 7;

public:
    int totalLetterCountOfNumberWord(int num){

        int res = 0;
        for(int i = 1 ; i <= num ; i ++)
            res += letterCountOfNumberWord(i);
        return res;
    }

private:
    int letterCountOfNumberWord(int num){
        if(num < 20)
            return basicCounts[num];

        if(num <= 99) {
            int res = tenthCounts[num / 10];
            if(num % 10 != 0)
                res += letterCountOfNumberWord(num % 10);
            return res;
        }
        if(num <= 999) {
            int res = basicCounts[num / 100] + hundred;
            if(num % 100 != 0)
                res += 3 + letterCountOfNumberWord(num % 100);
            return res;
        }

        if(num <= 9999) {
            int res = basicCounts[num / 1000] + thousand;
            if(num % 1000 != 0)
                res += letterCountOfNumberWord(num % 100);
            return res;
        }
    }
};

int main() {

    cout << Solution().totalLetterCountOfNumberWord(1000) << endl;

    return 0;
}