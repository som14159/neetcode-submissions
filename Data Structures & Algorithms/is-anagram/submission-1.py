class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mappie = {}
        for c in s:
            if c in mappie:
                mappie[c] += 1
            else:
                mappie[c] = 1
        for c in t:
            if c in mappie:
                mappie[c] -= 1
            else:
                mappie[c] = -1
        for k, v in mappie.items():
            if v != 0:
                return False
        return True
