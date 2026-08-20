class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            cnt = len(word)
            res += f"{cnt}<s>{word}"
        
        return res

    def decode(self, s: str) -> List[str]:

        res = []

        i = 0
        
        while i < len(s):

            j = i

            while s[j] != "<":
                j += 1
            
            cnt = int(s[i:j])
            word = s[j+3:j+3+cnt]

            res.append(word)

            i = j+3+cnt
        return res