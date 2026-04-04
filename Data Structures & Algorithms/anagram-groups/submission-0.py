class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = defaultdict(list)

        for str in strs: 
            temp = [0] * 26
            for ch in str:
                temp[ord(ch) - ord('a')] += 1

            hash_table[tuple(temp)].append(str)

        res = []
        for val in hash_table.values():
            res.append(val)

        return res        