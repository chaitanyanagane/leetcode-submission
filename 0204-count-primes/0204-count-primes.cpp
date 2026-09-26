#include <vector>
using namespace std;

class Solution {
public:
    int countPrimes(int n) {
        if (n < 3) return 0;

        int size = n / 2;
        vector<char> isComposite(size, 0);

        int count = (n > 2) ? 1 : 0; 

        for (int i = 1; i < size; i++) {
            if (!isComposite[i]) {
                long long num = 2LL * i + 1;
                count++;
                for (long long j = num * num; j < n; j += 2 * num) {
                    isComposite[(j - 1) / 2] = 1;
                }
            }
        }

        return count;
    }
};