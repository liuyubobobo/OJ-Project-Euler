/// Source : https://projecteuler.net/problem=1
/// Author : liuyubobobo
/// Time   : 2017-09-23

#include <iostream>

using namespace std;

class Solution{

public:
    int sumOf3and5(int num){

        int lastNumber = num - 1;

        int sumOf3 = sumOf(3, 3, (lastNumber/3)*3);
        int sumOf5 = sumOf(5, 5, (lastNumber/5)*5);
        int sumOf15 = sumOf(15, 15, (lastNumber/15)*15);

        return sumOf3 + sumOf5 - sumOf15;
    }

private:
    int sumOf(int multiple, int startNumber, int endNumber){

        if(endNumber < startNumber)
            return 0;

        int num = (endNumber - startNumber) / multiple + 1;
        return (startNumber + endNumber) * num / 2;
    }
};

int main() {

    cout << Solution().sumOf3and5(10) << endl;
    cout << Solution().sumOf3and5(1000) << endl;

    return 0;
}