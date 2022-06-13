import random
mylist = ["R", "P","S"]

Draw = True
while Draw:
    cpu = random.choice(mylist)
    player = input('choose a character from "R","P","S": ')
    while player not in mylist:
        print("Invalid Character!")
        player = input('choose a character from "R","P","S": ')
        continue
        
    if (cpu == mylist[0] and player == mylist[1]) or (cpu == mylist[1]  and player ==mylist[2]) or (cpu == mylist[2] and player == mylist[0]):
        print(f"Computer:{cpu} \nPlayer:{player}")   
        print("You win!")
        Draw = False 
                                  
    elif (cpu == mylist[0]  and player == mylist[2]) or (cpu == mylist[1] and player == mylist[0]) or (cpu == mylist[2]  and player ==mylist[1]):
        print(f"Computer:{cpu} \nPlayer:{player}")       
        print("Computer wins!")
        Draw = False
                        
    else:
        print(f"Computer:{cpu} \nPlayer:{player}")
        print("The game is a tie")
     
         
   