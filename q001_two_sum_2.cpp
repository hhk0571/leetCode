#include <vector>

#include <iostream>
#include <string>
#include <tuple>

// time:    0ms
// memory:  8.5M

using namespace std;

class Solution
{
  public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        int i {0};
        int j {0};

        int numsSize = nums.size();
        for (i = 0; i < numsSize - 1; i++)
        {
            for (j = i+1; j < numsSize; j++)
            {
                if ((nums[i] + nums[j]) == target)
                {
                    return {i, j};
                }

            }
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

