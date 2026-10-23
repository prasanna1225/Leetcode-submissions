class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
# Both sorted lists are identical, so the result is True.
# Time: O(n log n) — sorting both strings takes O(n log n).
# Space: O(n)— sorted() creates new lists containing the characters.

        