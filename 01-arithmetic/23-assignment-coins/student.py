# write your code here
def coins(amount):
    vijf=amount//5
    twee=(amount-(vijf*5))//2
    een=(amount-(vijf*5))%2
    result=vijf+twee+een
    return result