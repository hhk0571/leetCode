#include <vector>
#include <iostream>
#include <string>
#include <tuple>
#include <map>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        int result {0};
        int tmp {0};
        int n {0};
        int lastN {10000};
        for (const auto& c : s)
        {
            // auto n = symbol[c]; // lower performance, consumed more memory
            // auto n = getNum(c); // a little bit better
            switch (c) // for better performance
            {
                case 'I': n = 1;   break;
                case 'V': n = 5;   break;
                case 'X': n = 10;  break;
                case 'L': n = 50;  break;
                case 'C': n = 100; break;
                case 'D': n = 500; break;
                case 'M': n = 1000;break;
            }

            // cout << c << " lastN: " << lastN << " n: " << n;
            if (n > lastN)
            {
                result += (n - tmp -tmp);
                tmp = 0;
            }
            else
            {
                result += n;
                tmp = n;
            }
            lastN = n;
            // cout << " result: " << result << " tmp: " << tmp << endl;
        }
        return result;
    }

private:
    int getNum(char c)
    {
        switch (c)
        {
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
        default: return 0;
        }
    }
    map<char, int> symbol {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };

};

int main(int argc, char const *argv[])
{
    vector<tuple<string, int>> testCases {
        {"III",     3},
        {"IV",      4},
        {"IX",      9},
        {"XII",     12},
        {"VIII",    8},
        {"XXVII",   27},
        {"LVIII",   58},
        {"MCMXCIV", 1994}
    };
    auto s = Solution();
    for (auto& testcase:testCases){
        auto idx = &testcase - testCases.data();
        auto ret = s.romanToInt(get<0>(testcase));
        cout << "case " << idx << ": " << (ret == std::get<1>(testcase) ? "PASSED" : "FAILED") << "."
             << " expected: " << std::get<1>(testcase)
             << " returned: " << ret
             << endl;
    }
    return 0;
}
