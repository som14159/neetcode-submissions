class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i, prefix = 0, ""
        while i < len(strs[0]):
            all_equal = True
            for s in strs[1:]:
                if i >= len(s) or s[i] != strs[0][i]:
                    all_equal = False
                    break
            if not all_equal:
                break
            prefix += strs[0][i]
            i += 1
        return prefix
