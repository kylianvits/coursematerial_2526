# write your code here
def player_movement(position, left_arrow, right_arrow, shift):
    if left_arrow== True and right_arrow==False and shift==False:
        return position-1
    if left_arrow== True and right_arrow==True:
        return position
    if left_arrow== True and right_arrow==False and shift== True:
        return position-2
    if left_arrow==False and right_arrow==True and shift== False:
        return position+1
    if left_arrow==False and right_arrow== True and shift== True:
        return position+2
    else:
        return position