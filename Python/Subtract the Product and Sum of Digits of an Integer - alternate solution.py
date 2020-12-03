class Solution:
    def subtractProductAndSum(self, n):
        sum, prod = 0, 1
        
        while n:
            n, digit = divmod(n, 10)
            sum += digit
            prod *= digit
            
        return prod - sum