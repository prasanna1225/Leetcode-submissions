class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dicts, dictt = {}, {}

        for i in s:
            dicts[i] = dicts.get(i, 0) + 1

        for j in t:
            dictt[j] = dictt.get(j, 0) + 1

        return dicts == dictt
    # Time complexity: O(n)
    # Space complexity: O(n)
        