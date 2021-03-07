#include <vector>
#include <map>

#include <iostream>
#include <string>
#include <tuple>

// time:    4ms
// memory:  8.8M

using namespace std;

class Solution
{
  public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        int i {0};
        int a {0};
        map<int, int> m;
        for (const auto& n : nums) {
            a = target - n;
            auto idx_a = m.find(a);
            if (idx_a != m.end())
            {
                return {idx_a->second, i};
            }
            m.emplace(n, i);
            i++;
        }
        return {};
    }
};

auto print_all = [](const auto &v, const string &s="") {
    if (s != "") cout << s;
    for (const auto &i:v) cout << i << ' ';
    cout << endl;
};

int main(int argc, char const *argv[])
{
    vector<tuple<vector<int>, int, vector<int>>> testCases {
        {{2 , 7 , 11 , 15}, 9,  {0, 1}},
        {{3 , 2 , 4      }, 6,  {1, 2}},
        {{2 , 5 , 5  , 11}, 10, {1, 2}}
    };
    auto s = Solution();
    for (auto& testcase:testCases){
        auto idx = &testcase - testCases.data();
        auto ret = s.twoSum(std::get<0>(testcase), std::get<1>(testcase));
        cout << "case " << idx << ": " <<(ret == std::get<2>(testcase) ? "PASSED" : "FAILED") << endl;
        print_all(std::get<2>(testcase), "    expected: ");
        print_all(ret, "    returned: ");
    }

    return 0;
}

