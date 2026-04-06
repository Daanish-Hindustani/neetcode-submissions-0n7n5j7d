class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        G: Group related anagrams together
        1. Find the anagram
            - Loop though each str and char and determin cound
        2. Group the anigrams
            - Once we get a count we need to put it in some stroage
            - We can use a dict and map k:v -> count -> [words]

        Complexity:
            - Time O(n)*O(c)
            - Space: O(n)
        """


        freq = defaultdict(list)

        # Looping and finding anagrams
        for word in strs:
            # capture count
            cnt = [0]*26
            for char in word:
                cnt[ord(char) - ord('a')] += 1
            
            freq[tuple(cnt)].append(word)
        
        return list(freq.values())
            

