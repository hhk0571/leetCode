 #include <vector>
#include <iostream>
#include <string>
#include <tuple>

using namespace std;

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x=0, ListNode *next=nullptr) : val(x), next(next) {}
    ListNode(const vector<int>& v): ListNode()
    {
        auto p = this;
        for (const auto&i : v)
        {
            p->next = new ListNode(i);
            p = p->next;
        }
    }

    vector<int> toVector() const
    {
        vector<int> v;
        auto p = this;
        while (p) {
            v.emplace_back(p->val);
            p = p->next;
        }
        return v;
    }

};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode ret;
        auto a = l1;
        auto b = l2;
        auto c = &ret;
        int carry = 0;

        while (a or b)
        {
            int av = a ? a->val : 0;
            int bv = b ? b->val : 0;
            int x = av + bv + carry;
            c->next = new ListNode(x % 10);
            carry = x >= 10 ? 1 : 0;
            if (a) {
                a = a->next;
            }
            if (b) {
                b = b->next;
            }
            c = c->next;
        }

        if (carry) {
            c->next = new ListNode(carry);
        }

        return ret.next;
    }
};


auto print_all = [](const auto &v, const string &s="") {
    if (s != "") cout << s;
    for (const auto &i:v) cout << i << ' ';
    cout << endl;
};

int main(int argc, char const *argv[])
{
    vector<tuple<vector<int>, vector<int>, vector<int>>> testCases {
        {{2,4,3}, {5,6,4}, {7,0,8}},
        {{0    }, {0    }, {0    }},
        {{1,2,7}, {8,9  }, {9,1,8}},
        {{9,9,9,9,9,9,9}, {9,9,9,9},{8,9,9,9,0,0,0,1}}
    };
    auto s = Solution();
    for (auto& testcase:testCases){
        auto idx = &testcase - testCases.data();
        ListNode l1(std::get<0>(testcase));
        ListNode l2(std::get<1>(testcase));
        auto l3_p = s.addTwoNumbers(l1.next, l2.next);
        auto ret = l3_p->toVector();
        cout << "case " << idx << ": " <<(ret == std::get<2>(testcase) ? "PASSED" : "FAILED") << endl;
        print_all(std::get<2>(testcase), "    expected: ");
        print_all(ret, "    returned: ");
    }

    return 0;
}
