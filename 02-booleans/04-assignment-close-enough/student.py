# write your code here
def close_enough(x, y):
    grootste=max(x,y)
    kleinste=min(x,y)
    if grootste-kleinste<=0.1:
        return True
    return False