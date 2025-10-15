# write your code here
def box(string):
    res=len(string)+2
    woord=("-"*res)
    return f"+{woord}+\n| {string} |\n+{woord}+"