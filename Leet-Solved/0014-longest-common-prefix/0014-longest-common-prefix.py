class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < len(prefix) and j < len(strs[i]) and prefix[j] == strs[i][j]:
                j += 1
            prefix = prefix[:j]
            if not prefix:
                return ""
        return prefix