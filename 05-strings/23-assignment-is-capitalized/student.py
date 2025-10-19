# write your code here
def is_capitalized(string):
    if len(string) == 0:
        return False
    if len(string) == 1:
        return string.isupper()
    return string[0].isupper() and string[1:].islower()
