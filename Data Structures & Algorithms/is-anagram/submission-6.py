class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
# Counter() automatically counts the frequency of each character
# - Time: \(O(n)\) average
# - Space: \(O(n)\)

        