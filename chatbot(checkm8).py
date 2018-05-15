import random
import time 

print(" Hello I am checkm8, lets play you are  :) :" )
decision = raw_input()
chess={"tactics":[ "place the white king a5, a white pawn on b7, a king on a7, a rook on white rook on c7, and a black rook on  ", " white rook a2, white king c3, white bishop c4, black king d1,black rook e8" ], "play":[ "would you like to be black or white","your playing white", "your playing black"], "playerlookup":[" plz enter the player name", "put in th player name"] }

chess_template= "checkM8:{0}"
user_template= "user:{0}"
template = 'I can hear you, you said:'+" "
def bot(decision):
  if decision in chess:
    print(random.choice(chess[decision]))
  else:
    print("Error you have not inputed neither of the following: tactics, play, playerlookup  ")
    
bot(decision)
