import random
rock="r"
paper="p"
scissor="s"
game_letters=[rock,paper,scissor]
user_choice=int(input('What do you want choose?Type 0 for rock,1 for paper,2 for scissor'))
if user_choice>=0 and user_choice <=2:
    print(game_letters[user_choice])
computer_choice=random.randint(0,2)
print(game_letters[computer_choice])

if user_choice >=3 or user_choice <0:
    print("You typed a invalid number,You lose")
elif user_choice==0 and computer_choice==2 :
    print("You win!")
elif user_choice==2 and computer_choice==0:
    print("You lose")
elif user_choice == computer_choice:
    print("It's a draw")
elif user_choice>computer_choice:
    print("You win")
elif computer_choice>user_choice:
    print("You lose!")

       