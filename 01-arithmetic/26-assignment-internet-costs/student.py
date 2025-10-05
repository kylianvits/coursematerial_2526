# write your code here
import math
def internet_costs(duration_in_seconds, cost_per_block):
   result=math.ceil(duration_in_seconds / 360) * cost_per_block
   return result