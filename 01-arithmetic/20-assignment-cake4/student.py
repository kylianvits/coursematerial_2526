# write your code here
import math
def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    eieren=math.floor(eggs//eggs_per_cake)
    bloem=math.floor(flour//flour_per_cake)
    boter=math.floor(butter//butter_per_cake)
    suiker=math.floor(sugar//sugar_per_cake)
    return min(bloem,eieren,boter,suiker) 