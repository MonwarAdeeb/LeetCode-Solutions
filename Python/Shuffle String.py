class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = [''] * len(s)
        
        for item in range(len(s)):
            output[indices[item]] = s[item]
            
        return ''.join(letter for letter in output)