# [5,5,5,10,20] = True
# [5,5,10,10,20] = False
# [5,5,5,10,5,5,10,20,20,20] = False

from typing import List

class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        
        # Variables para almacenar bills de 5 y 10
        bills5, bills10 = 0, 0

        # Recibimos lista de pago por limonadas
        for b in bills:

            # Cuando recibimos 5 solo almacenamos
            if b == 5:
                bills5 += 1

            # Validamos cambio cuando recibimos 10
            elif b == 10:

                if bills5 >= 1:
                    bills10 += 1
                    bills5 -= 1
                else:
                    return False

            # Validamos los cambios cuando recibimos 20
            elif b == 20:

                if bills10 >= 1 and bills5 >= 1:
                    bills10 -= 1
                    bills5 -= 1
                elif bills5 >= 3:
                    bills5 -= 3
                else:
                    return False
            
        return True

solution = Solution()

print(solution.lemonadeChange(bills=[5,5,10,10,20]))