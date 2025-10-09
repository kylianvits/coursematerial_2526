# write your code here
#| Rock     | 0              |
#| Paper    | 1              |
#| Scissors | 2              |

def rock_paper_scissors(player1_choice, player2_choice):
    if player1_choice==player2_choice:
        return 0
    if player1_choice==0 and player2_choice==1 or player1_choice==1 and player2_choice==2 or player1_choice==2 and player2_choice==0:
        return 2
    #if player1_choice==1 and player2_choice==0:
    else:
        return 1