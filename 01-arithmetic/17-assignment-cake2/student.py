# write your code here
import math
def cake2(eggs, flour):
    eieren=math.floor(eggs//5)
    bloem=math.floor(flour//250)
    return min(bloem,eieren)