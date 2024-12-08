
name = input("Please enter your name : ")

if name.upper() == "VIP" : print("Enjoy the show for free!")
else :
    num=int(input("How many tickets would you like to buy? "))
    print("the total cost is : " , num*15.5 , "$")
    print("Enjoy the show !")
