class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Search col
        # search rols

        l,r = 0, len(matrix)-1

        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0] == target:
                return True
            
            if matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        

        col = l

        l,r = 0, len(matrix[0])

        while l<=r:
            mid = (l + r) //2
            if matrix[mid][col] == target:
                return True
            
            elif matrix[mid][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False

        
