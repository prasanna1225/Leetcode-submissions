class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalAnagram=defaultdict(list)
        for str in strs:
            sortedStr = ''.join(sorted(str))
            finalAnagram[sortedStr].append(str)
        return list(finalAnagram.values())
            
        