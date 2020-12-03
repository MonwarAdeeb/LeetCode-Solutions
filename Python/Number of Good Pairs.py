class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        repeat = {}
        count = 0

        for v in nums:
            if v in repeat:
                
                if repeat[v] == 1:
                    count += 1
                else:
                    count += repeat[v]
        
                repeat[v] += 1
            
            else:
                repeat[v] = 1
                
        return count
        