class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        largest = candies[0]
        for item in candies:
            if item>largest:
                largest = item
        
        ans = list()
        for i in candies:
            if i+extraCandies >= largest:
                ans.append(True)
            else:
                ans.append(False)

        return ans