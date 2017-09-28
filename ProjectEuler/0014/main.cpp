/// Source : https://projecteuler.net/problem=14
/// Author : liuyubobobo
/// Time   : 2017-09-27

#include <iostream>
#include <vector>

using namespace std;

class Solution{

public:
    int longestChain(int maxNum){

        vector<int> record(maxNum + 1, 0);

        int maxLength = 0;
        int startNumber = 0;
        for(int i = 1 ; i <= maxNum ; i ++){

            long long tnum = i;
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

            if(record[i] >= maxLength){
                maxLength = record[i];
                startNumber = i;
            }
        }

        return startNumber;
    }
};

int main() {

    cout << Solution().longestChain(1000000) << endl;

    return 0;
}