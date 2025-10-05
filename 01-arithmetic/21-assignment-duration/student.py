# write your code here
import math
def hours(duration):
    result=math.floor(duration//3600)
    return result
def minutes(duration):
    result=math.floor(duration%3600)//60
    return result
def seconds(duration):
    result=math.floor(duration%60)
    return result