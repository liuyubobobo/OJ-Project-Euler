/// Source : https://www.hackerrank.com/contests/projecteuler/challenges/euler014
/// Author : liuyubobobo
/// Time   : 2017-09-27

#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

class Solution{

private:
    int* record;
    int* maxLength;
    int* startNumber;
    int maxNum;

public:
    Solution(int maxNum){

        this->maxNum = maxNum;
        record = new int[maxNum + 1];
        maxLength = new int[maxNum + 1];
        startNumber = new int[maxNum + 1];
        for(int i = 0 ; i <= maxNum ; i ++) {
            record[i] = 0;
            maxLength[i] = 0;
            startNumber[i] = 0;
        }

        for(int i = 1 ; i <= maxNum ; i ++){

            long long tnum = (long long)i;
            int k = 1;
            while(true){
                if(tnum == (long long)1){
                    record[i] = k;
                    break;
                }

                if(tnum < (long long)i){
                    record[i] = k + record[tnum] - 1;
                    break;
                }

                if(tnum % (long long)2 == (long long)0)
                    tnum /= (long long)2;
                else
                    tnum = (long long)3 * tnum + (long long)1;
                k ++;
            }

            if(record[i] >= maxLength[i-1]){
                maxLength[i] = record[i];
                startNumber[i] = i;
            }
            else{
                maxLength[i] = maxLength[i-1];
                startNumber[i] = startNumber[i-1];
            }

        }

    }

    ~Solution(){
        delete[] record;
        delete[] maxLength;
        delete[] startNumber;
    }

    int longestChain(int N){
        return startNumber[N];
    }

};

int main() {

    int maxN = 5000000;
    Solution solution(maxN);

    int T;
    cin >> T;
    while(T --){
        int N;
        cin >> N;
        cout << solution.longestChain(N) << endl;
    }

    return 0;
}