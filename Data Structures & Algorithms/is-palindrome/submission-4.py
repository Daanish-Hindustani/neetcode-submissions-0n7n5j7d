class Solution:
    def isPalindrome(self, nums: str) -> bool:
        
        # processed = ""

        # for char in s:
        #     if not char.isalnum():
        #         continue
            
        #     if char.isdigit():
        #         processed+= char

        #     processed += char.lower()
        
        # return processed == processed[::-1]


        l, r = 0, len(nums)-1

        while l<r:
            while not nums[l].isalnum() and l<r:
                l+=1
            
            while not nums[r].isalnum() and l<r:
                r-=1
            
            if nums[l].isdigit() and nums[r].isdigit():
                if nums[l] != nums[r]:
                    return False
                l += 1
                r-=1
            
            elif not nums[l].isdigit() and not nums[r].isdigit():
                if nums[l].lower() != nums[r].lower():
                    return False
                l += 1
                r-=1
            else:
                return False

        return True
            
