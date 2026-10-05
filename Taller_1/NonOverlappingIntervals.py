# [[1,2],[2,3],[3,4],[1,3]] = 1
# [[1,2],[1,2],[1,2]] = 2
# [[1,2],[2,3]] = 0

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # Criterio Greedy: Ordenar por tiempo de fin para maximizar espacio libre
        intervals.sort(key=lambda x: x[1])
        
        removals = 0
        last_end = float('-inf')
        
        for start, end in intervals:
            if start >= last_end:
                # No se solapan, lo aceptamos
                last_end = end
            else:
                # Se solapan, hay que "borrarlo"
                removals += 1
                
        return removals