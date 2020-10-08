class Solution:
    def subtractProductAndSum(self, n):
        number = list(map(int, str(n)))
        return reduce(operator.mul, number) - sum(number)
        