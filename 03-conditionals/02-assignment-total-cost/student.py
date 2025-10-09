# write your code here
def total_cost(amount):
    result=amount
    if amount<100:
        result=amount+10
    if amount>=200:
        result=amount*0.95
    
    return result