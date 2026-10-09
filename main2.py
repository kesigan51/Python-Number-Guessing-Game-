import random
def user():
    while True:
      name = input("What's your name:")
      try:
         val = int(name)
         user()
      except ValueError:
         break
    print(f"Welcome! {name}")
    score = 0
    while True:
       cnum = random.randint(1,11)
       num = int(input("Enter a number/ 1<=your number<=10:"))
       if 0<num and num<=10:
           if num == cnum:
               score +=10    
               print(f"You won!, Your score is {score}")
              
           else:
               print(f"You lost! Answer is {cnum}") 
               dif = cnum -num
               if dif <0:
                 dif = dif*-1
               if dif<=5:    
                 print("Too low") 
               else:
                 print("Too high") 
               
               while True:
                playagain = input("Would you like to play again? Y/N:")
                if playagain in ["N","n"]:
                   return
                    
                elif playagain in ["Y","y"]:
                   score = 0
                   break
                else:
                   print("Obey Rules...")
                   continue          
       else:
           print("Obey rules..")
       
print("Welcome to Number Guessing Game!")
user()           