class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = ""
        for word in strs:
            length = len(word)
            res += str(length) + '<s>' + word
        
        return res


    def decode(self, s: str) -> List[str]:

        res = []

        i = 0
        while i in range(len(s)):
            j = i

            while s[j] != '<':
                j += 1
            
            length = int(s[i:j])
            word = s[j+3:j+3+length]

            res.append(word)

            i = j+3+length
        
        return res

