# [[1,3],[2,6],[8,10],[15,18]] = [[1,6],[8,10],[15,18]]
# [[1,4],[4,5]] = [[1,5]]
# [[4,7],[1,4]] = [[1,7]]

from typing import List

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        
        # Ordenar tomando como clave el extremo izquierdo
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            last_merged_start, last_merged_end = merged[-1]
            
            # Si se solapan o tocan, ensanchar el límite
            if current_start <= last_merged_end:
                merged[-1][1] = max(last_merged_end, current_end)
            else:
                # Si no, cerrar el actual y meter el nuevo
                merged.append(intervals[i])
                
        return merged