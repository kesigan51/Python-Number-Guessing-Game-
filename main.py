import random
def user():
    name = input("What's your name:")
    print(f"Welcome! {name}")
    score = 0
    while True:
       cnum = random.randint(1,11)
       num = int(input("Enter a number/ 1<=your number<=10:"))
       if 0<num and num<=10:
           if num == cnum:
               score +=10    
               print(f"You won!, Your score is {score}")
               continue
           else:
               print(f"You lost! Answer is {cnum}") 
               dif = cnum -num
               if dif <0:
                 dif = dif*-1
               if dif<=5:    
                 print("Too low") 
               else:
                 print("Too high") 
               playagain = input("Would you like to play again? Y/N:")
               if playagain == "N" or playagain == "n":
                   break  
               else:
                   score = 0
                   continue  
       else:
           print("Obey rules..")

print("Welcome to Number Guessing Game!")
user()           