# write your code here
def tip_calculator():
    price=input("Enter total price:")
    percentage=input ("Enter tip percentage")
    if percentage=="":
        percentage=20
    total= float(price)+(float(price)*(float(percentage)/100))
    total = round(total)
    print(f"You have to pay {total}")
