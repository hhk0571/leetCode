#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_len = len(s)
        for win_size in range(s_len, 0, -1):
            # print('win_size:', win_size)
            if win_size == s_len:
                if self.is_Palindrome(s):
                    return s
            else:
                for i in range(s_len - win_size + 1):
                    # print('sub_s:', s[i:win_size+i])
                    if self.is_Palindrome(s[i:win_size+i]):
                        return s[i:win_size+i]
        return ''


    @staticmethod
    def is_Palindrome(s):
        mid = len(s)//2
        for i in range(mid):
            if s[i] != s[-i-1]:
                return False
        return True


if __name__ == "__main__":
    # with open('q003_longtext.txt') as f:
    #     longtext = f.read()
    testcases = [
        ('abcdcbaeee'   , 'abcdcba'),
        ('123abcdcbaeee', 'abcdcba'),
        ('123abcdcba'   , 'abcdcba'),
        ('a'        , 'a'       ),
        ('123ea'        , ''       ),
        ("klvxwqyzugrdoaccdafdfrvxiowkcuedfhoixzipxrkzbvpusslsgfjocvidnpsnkqdfnnzzawzsslwnvvjyoignsfbxkgrokzyusxikxumrxlzzrnbtrixxfioormoyyejashrowjqqzifacecvoruwkuessttlexvdptuvodoavsjaepvrfvbdhumtuvxufzzyowiswokioyjtzzmevttheeyjqcldllxvjraeyflthntsmipaoyjixygbtbvbnnrmlwwkeikhnnmlfspjgmcxwbjyhomfjdcnogqjviggklplpznfwjydkxzjkoskvqvnxfzdrsmooyciwulvtlmvnjbbmffureoilszlonibbcwfsjzguxqrjwypwrskhrttvnqoqisdfuifqnabzbvyzgbxfvmcomneykfmycevnrcsyqclamfxskmsxreptpxqxqidvjbuduktnwwoztvkuebfdigmjqfuolqzvjincchlmbrxpqgguwuyhrdtwqkdlqidlxzqktgzktihvlwsbysjeykiwokyqaskjjngovbagspyspeghutyoeahhgynzsyaszlirmlekpboywqdliumihwnsnwjc", 'wrong'),
        ("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg", 'avc'),
    ]

    solution = Solution()
    # print(solution.is_Palindrome('abcdcba'))
    # print(solution.is_Palindrome('abcdc'))
    for i, tc in enumerate(testcases):
        ans = solution.longestPalindrome(tc[0])
        print(i, 'OK' if ans == tc[1] else 'Failed', 'expected:%s, return:%s'%(tc[1], ans))
