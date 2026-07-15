class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the correct row
        lr, cr = 0, len(matrix)-1
        while lr<=cr:
            mid = (lr+cr) // 2
           
            if matrix[mid][0] == target:
                return True
            
            if matrix[mid][0] < target:
                lr = mid + 1
            else:
                cr = mid - 1
            
        
        l,r = 0, len(matrix[0])-1

        while l<=r:
            mid = (l+r) //2

            if matrix[cr][mid] == target:
                return True
            
            if matrix[cr][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False

        # find the correct col