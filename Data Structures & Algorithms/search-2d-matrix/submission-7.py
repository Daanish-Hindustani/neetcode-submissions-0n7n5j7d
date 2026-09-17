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
        

        col = r

        l,r = 0, len(matrix[0])-1

        while l<=r:
            mid = (l + r) //2
            
            if matrix[col][mid] == target:
                return True
            
            elif matrix[col][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False

        
