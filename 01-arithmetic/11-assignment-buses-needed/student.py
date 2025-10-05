# write your code here
import math 
def buses_needed(people_count, bus_capacity):
    result=math.ceil(people_count/bus_capacity)
    return result
