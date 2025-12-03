import random

print("Welcome to Rock, Paper, Scissors!")
user_choice=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n".lower())

computer_choice=random.randint(0,2)
print(f"Computer chose {computer_choice}")

if user_choice=="0" and computer_choice==1:
    print("You lose!")
elif user_choice=="0" and computer_choice==2:
    print("You win!")  
elif user_choice=="1" and computer_choice==0:
    print("You win!")      
elif user_choice=="1" and computer_choice==2:
    print("You lose!")
elif user_choice=="2" and computer_choice==0:
    print("You lose!")
elif user_choice=="2" and computer_choice==1:
    print("You win!")
else:   
    print("It's a draw!")