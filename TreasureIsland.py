print("Welcome to Treasure Island.")
print("Your Mission is to find the treasure." )
choice1=input('you are on crossroad,where do you want to go?Type"left" or "right.\n"')
      
if choice1=="left":
    choice2=input('you came to a lake,so there is an island.what do you choose?Type "wait" or "swim".\n')
    if choice2=="wait":
        choice3=input('which door you want to choose?Type "Red","blue","Yellow"\n ')
        if choice3=="Yellow":
            print("You win")
        else :
           print("You choose wrong door there is no way,game over!")    
    else:
        print("there is hole ,no chance of swimming,game over!")
else:
    print("there is no way,game over!")    

