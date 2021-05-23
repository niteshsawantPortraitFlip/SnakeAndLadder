import random
def ladder_and_snake():
    print("***Welcome to ladder and sanke game***")
    Player1=input("Player1 enter your name= ").upper()     #.center(10,"#")
    Player2=input("Player2 enter your name= ").upper()     #.center(10,"#")
    Player3=input("Player3 enter your name= ").upper()     #.center(10,"#")
    Player4=input("Player4 enter your name= ").upper()     #.center(10,"#")
    position_of_player1=0
    position_of_player2=0
    position_of_player3=0
    position_of_player4=0
    lucky=6
    print(f"You all are at 0 position")
    game_over= False
    while not game_over:
        
        p1 = position_of_player1
        p2 = position_of_player2
        p3 = position_of_player3
        p4 = position_of_player4

        x = {p1:100, p2:100, p3:100, p4:100}
        
        # Code for Player1
        #game_over1 = False
        if position_of_player1 != 100:
            Dice=random.randint(1,6)
            a=input(f"{Player1} press Enter to throw a dice")
            position_of_player1+=Dice
            while lucky==Dice:
                Dice=random.randint(1,6)
                a2=input(f"{Player1} you got {lucky} number and you are at {position_of_player1} position now press Enter again to throw a dice") 
                position_of_player1+=Dice
                if position_of_player1>100:
                    position_of_player1-=6
                    print(f"{Player1} You are back to your {position_of_player1} position")
                continue 

            print(f"{Player1} you got {Dice} number")  
            if position_of_player1>100:
                position_of_player1-=Dice
                print(f"{Player1} You are at {position_of_player1} position and you have to get {100-position_of_player1} to win")
            print(f"{Player1} you are at {position_of_player1} now")

            ladder={2:23,6:45,20:59,52:72,57:96,71:92}
            snake={43:17,50:5,56:8,73:15,84:58,98:95}        
            for i,j in ladder.items():
                if position_of_player1==i:
                    position_of_player1=j
                    print(f"{Player1} You got a ladder and now you are at {position_of_player1} position now")
            for i,j in snake.items():
                if position_of_player1==i:
                    position_of_player1=j
                    print(f"{Player1} Badluck you were bitten by snake and now you are at {position_of_player1} position now")
            
            if position_of_player1==100:
                #game_over1=True
                print(f"Congratulation {Player1} YOU WIN!!!")
                
        
            # else:
            #     pass          
        
        
        #game_over2 = False
        
        # Code for Player2
        if position_of_player2 != 100:
            Dice=random.randint(1,6)
            b=input(f"{Player2} press enter to throw a dice")
            position_of_player2+=Dice
            while lucky==Dice:
                Dice=random.randint(1,6)
                b2=input(f"{Player2} you got {lucky} number and you are at {position_of_player2} position now press Enter again to throw a dice")
                position_of_player2+=Dice
                if position_of_player2>100:
                    position_of_player2-=6
                continue   
                
            print(f"{Player2} you got {Dice} number")
            if position_of_player2>100:
                position_of_player2-=Dice
                print(f"{Player2} You are at {position_of_player2} position and you have to get {100-position_of_player2}")
            print(f"{Player2} you are at {position_of_player2} now")

            ladder={2:23,6:45,20:59,52:72,57:96,71:92}
            snake={43:17,50:5,56:8,73:15,84:58,98:95}
            for i,j in ladder.items():
                if position_of_player2==i:
                    position_of_player2=j
                    print(f"{Player2} You got a ladder and you are at {position_of_player2} position now")

            for i,j in snake.items():
                if position_of_player2==i:
                    position_of_player2=j
                    print(f"{Player2} Badluck you were bitten by snake and now you are at {position_of_player2} position now") 

            if position_of_player2==100:
                print(f"Congratulation {Player2} YOU WIN!!!")
                #game_over2=True
            
                
        # else:
        #     pass

        # game_over3 = False
        
        if position_of_player3 !=100:
        # Code for Player3
            Dice=random.randint(1,6)
            c=input(f"{Player3} press enter to throw a dice")
            position_of_player3+=Dice
            while lucky==Dice:
                Dice=random.randint(1,6)
                c2=input(f"{Player3} you got {lucky} number and you are at {position_of_player3} position now press Enter again to throw a dice")
                position_of_player3+=Dice
                if position_of_player3>100:
                    position_of_player3-=6
                continue    

            print(f"{Player3} you got {Dice} number")     
            if position_of_player3>100:
                position_of_player3-=Dice
                print(f"{Player3} You are at {position_of_player3} position and you have to get {100-position_of_player3}")
            print(f"{Player3} you are at {position_of_player3} now")

            ladder={2:23,6:45,20:59,52:72,57:96,71:92}
            snake={43:17,50:5,56:8,73:15,84:58,98:95}
            for i,j in ladder.items():
                if position_of_player3==i:
                    position_of_player3=j
                    print(f"{Player3} You got a ladder and you are at {position_of_player3} position now")

            for i,j in snake.items():
                if position_of_player3==i:
                    position_of_player3=j
                    print(f"{Player3} Badluck you were bitten by snake and now you are at {position_of_player3} position now") 

            if position_of_player3==100:
                print(f"Congratulation {Player3} YOU WIN!!!")
                #game_over3=True
            
                
        # else:
        #     pass

        # game_over4 = False
        if position_of_player4 !=100 :
        # Code for Player4
            Dice=random.randint(1,6)   
            d=input(f"{Player4} press enter to throw a dice")
            position_of_player4+=Dice
            while lucky==Dice:
                Dice=random.randint(1,6)
                d2=input(f"{Player4} you got {lucky} number and you are at {position_of_player4} position now press Enter again to throw a dice")
                position_of_player4+=Dice
                if position_of_player4>100:
                    position_of_player4-=6
                continue  

            print(f"{Player4} you got {Dice} number")    
            if position_of_player4>100:
                position_of_player4-=Dice
                print(f"{Player4} You are at {position_of_player4} position and you have to get {100-position_of_player4}")
            print(f"{Player4} you are at {position_of_player4} now")

            ladder={2:23,6:45,20:59,52:72,57:96,71:92}
            snake={43:17,50:5,56:8,73:15,84:58,98:95} 
            for i,j in ladder.items():
                if position_of_player4==i:
                    position_of_player4=j
                    print(f"{Player4} You got a ladder and you are at {position_of_player4} position now")

            for i,j in snake.items():
                if position_of_player4==i:
                    position_of_player4=j
                    print(f"{Player4} Badluck you were bitten by snake and now you are at {position_of_player4} position now")        

            if position_of_player4==100:
                print(f"Congratulation {Player4} YOU WIN!!!")
                #game_over4=True

            
                
        # else:
        #     pass

        if position_of_player1==100 and position_of_player2==100 and position_of_player3==100 and position_of_player4==100:
            game_over = True
            

ladder_and_snake()