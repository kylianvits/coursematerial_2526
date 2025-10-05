# write your code here
import math
def cake3(eggs, flour,butter,sugar):
    eieren=math.floor(eggs//5)
    bloem=math.floor(flour//250)
    boter=math.floor(butter//200)
    suiker=math.floor(sugar//250)
    return min(bloem,eieren,boter,suiker) 