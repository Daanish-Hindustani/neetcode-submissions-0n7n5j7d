class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        R: We have a 2d array and we need to find the target value
        I: Iterate through the first idcie of each row till we find the correct row, then BS to find the value
        D: 1)use bs of the first elemnt of each row 2) use bs for the row
        E: 
            1) BS for the fist element of each row
            2) Bs for the choosen row
            3) return val
        """

        def bst(l, r, target, temp):
            if l > r:  
                return False
            
            mid = (l + r) // 2

            if temp[mid] == target:
                return True
            
            elif temp[mid] > target:
                return bst(l, mid - 1, target, temp)
            else:
                return bst(mid + 1, r, target, temp)

        
        idx = 0
        for i in range(len(matrix)):
            val = matrix[i][0]
            if val == target:
                return True
            
            if val < target:
                idx = i
        
        return bst(0, len(matrix[0])-1, target, matrix[idx])

        












