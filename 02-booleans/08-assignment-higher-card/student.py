# write your code here
def higher_card(card1, card2):
    if card1==1:
        card1=14
    if card2==1:
        card2=14
    if card1>card2:
        return True
    return False