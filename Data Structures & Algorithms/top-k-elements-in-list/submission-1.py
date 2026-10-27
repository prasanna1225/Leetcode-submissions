class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        sortednums=sorted(freq, key=freq.get, reverse=True) #only keys in descending order
        return sortednums[:k]

      #for this i used sorting
    #   Overall time: (O(n + mlog m))
    #   Overall auxiliary space: (O(m))  
    # n counts all the elements, while m counts only the unique elements.

        
             




        
                
        