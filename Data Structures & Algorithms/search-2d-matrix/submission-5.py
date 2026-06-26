class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # n = length of rows
        # m = length of cols
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m-1
        while l <= r:
            ptr = ((r-l)//2)+l
            temp = matrix[ptr]
            if target == temp[0]:
                return True
            if target < temp[0]:
                r = ptr - 1
            elif target > temp[n-1]:
                l = ptr + 1
            elif target == temp[n-1]:
                return True
            elif target > temp[0] and target < temp[n-1]:
                l = 0
                r = n-1
                while l <= r:
                    ptr = ((r-l)//2)+l
                    if target == temp[ptr]:
                        return True
                    elif target > temp[ptr]:
                        l = ptr + 1
                    elif target < temp[ptr]:
                        r = ptr - 1
                return False
        return False


        