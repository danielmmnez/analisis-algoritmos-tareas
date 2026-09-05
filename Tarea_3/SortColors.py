# nums = [2,0,2,1,1,0]

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Variables de control
        bajo = 0
        medio = 0
        alto = len(nums) - 1

        # Recorremos sin for anidados (otra opcion de realizarlo menos optima)
        while medio <= alto:
            if nums[medio] == 0:
                # Cambios de posicion
                nums[bajo], nums[medio] = nums[medio], nums[bajo]
                bajo += 1
                medio += 1
            elif nums[medio] == 1:
                medio += 1
            else: 
                # Cambios de posicion
                nums[alto], nums[medio] = nums[medio], nums[alto]
                alto -= 1


solution = Solution()

solution.sortColors([2,0,2,1,1,0])