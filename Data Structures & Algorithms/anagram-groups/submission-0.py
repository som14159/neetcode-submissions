class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        result = []
        index = 0
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in m:
                result[m[sorted_s]].append(s)
            else:
                m[sorted_s] = index
                result.append([s])
                index += 1
        return result
                
