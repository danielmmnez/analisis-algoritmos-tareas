# [2,3,6,7], target = 7 = [[2,2,3],[7]]
# candidates = [2,3,5], target = 8 = [[2,2,2,2],[2,3,3],[3,5]]
# candidates = [2], target = 1 []

from typing import List

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        
        def dfs(i, current_sum, current_comb):
            # Condición de éxito
            if current_sum == target:
                res.append(list(current_comb))
                return
            
            # Poda o límite superado
            if current_sum > target or i >= len(candidates):
                return
            
            # Opción 1: Elegir el candidato actual y mantener el índice (se puede repetir)
            current_comb.append(candidates[i])
            dfs(i, current_sum + candidates[i], current_comb)
            
            # Deshacer selección (Backtrack)
            current_comb.pop()
            
            # Opción 2: No elegir el candidato actual y pasar al siguiente índice
            dfs(i + 1, current_sum, current_comb)

        dfs(0, 0, [])
        return res