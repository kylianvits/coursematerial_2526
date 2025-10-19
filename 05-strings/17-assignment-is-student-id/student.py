# write your code here
def is_student_id(string):
    res=len(string)
    if string[0]=="r" or string[0]=="s"or string[0]=="R"or string[0]=="S" :
        if string[1:].isdigit():
            if res==8:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
print(is_student_id("r1096x27"))