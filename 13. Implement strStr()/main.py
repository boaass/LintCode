# -*- coding:utf-8 -*-


class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        len_s = len(source)
        len_t = len(target)
        for i in range(len_s - len_t + 1):
            if source[i:i+len_t] == target:
                return i

        return -1


if __name__ == '__main__':
    source = "abcdabcdefg"
    target = "bcd"

    s = Solution()
    r = s.strStr(source, target)
    print(r)