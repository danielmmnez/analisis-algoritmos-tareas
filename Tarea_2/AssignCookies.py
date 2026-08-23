# g = [1,2,3], s = [1,1] = 1
# g = [1,2], s = [1,2,3] = 2

from typing import List

class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        # Variables para conocer felicidad de los niños y la galleta en la que nos encontramos
        nfelices = 0
        igalletas = 0

        # Ordenamos la lista de los niños y la lista de las galletas ya que debemos asegurar mayot numero de niños felices
        g.sort()
        s.sort()

        # Recorremos la felicidad de los niñós y galletas disponibles
        while nfelices < len(g) and igalletas < len(s):

            if s[igalletas] >= g[nfelices]:
                nfelices += 1
            igalletas += 1

        return nfelices


solution = Solution()

print(solution.findContentChildren(g=[1,2], s=[1,2,3]))