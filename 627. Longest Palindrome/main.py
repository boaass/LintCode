# -*- coding:utf-8 -*-


# 给出一个包含大小写字母的字符串。求出由这些字母构成的最长的回文串的长度是多少。
#
# 数据是大小写敏感的，也就是说，"Aa" 并不会被认为是一个回文串。
#
# Example
# 样例 1:
#
# 输入 : s = "abccccdd"
# 输出 : 7
# 说明 :
# 一种可以构建出来的最长回文串方案是 "dccaccd"。


class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        container = {}

        for c in s:
            if c in container.keys():
                container.pop(c)
            else:
                container[c] = 1

        if len(container.keys()) == 0:
            return len(s)
        else:
            return len(s) - len(container.keys()) + 1


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('abccccdd'))