try:
  import random 
  from functools import reduce
  choices = ["Rock", "Paper", "Scissors"]
  code ={ 1: "Rock", 2: "Paper" , 3: "Scissors"}
  # possibilities = [["rock", "paper"], ["paper", "scissors"], ["scissors", "rock"]]
  Computer = random.choice(choices)
  def desicion(a,b):
    
    if a == b :
      return ("  -------- It's a Tie --------", 0)
      
    elif(a == choices[0] and b == choices[1]) or \
    (a == choices[1] and b == choices[2]) or\
    (a == choices[2] and b == choices[0]):
      return ("  -------- Congrats, you won! -------- ", 1)
    else:
      return ("  -------- Computer has won --------", 0 )
    
  score1 =[]
  print("========== Welcome to the ROCK, PAPER AND SCISSORS Game ==========")
  print("====== Enter 1 for Rock , 2 for Paper and 3 for Scissors ======")
  # b = code[2]
  # print(b)
  for i in range(3) :
    points = i+1 
    a1 = int(input(" Enter your choice: "))
    player1 = code[a1]
    print (f" You have choosen: {player1}")
    print(f" Computer has choosen: {Computer} ")
    result, score = desicion(Computer,player1)
  
    print (result)
    score1.append(score)
  final_score = reduce(lambda x,y: x+y,score1 )
  if (final_score >=2):
    print(f" Your points are {final_score} and You have Won the game")
  elif(final_score==1):
    print(f"  Your score is {final_score} and the game is tie")
  else:
    print(f" Your score is {final_score} and you have lost the game ")

  input()
except ValueError:
  print(" Follow the instructions given above ")
except IndexError:
  print(" Follow the instructions given above ")
except KeyError:
  print(" Follow the instructions given above ")
# print(final_score)
# print("You have won the game") if (final_score >= 2) else ("It's a tie") if final_score == 1 else print("You have Lost the game")
# import random

  # elif ((a == choices[0]) and (b == choices[1])) :
  #   print (f"Congrats!, You have got {points} point")
  # elif ((a == choices[0]) and (b == choices[2])) :
  #   print (f"Computer has got {points} point") 
  # elif ((a == choices[1]) and (b == choices[0])) :
  #  print (f"Computer has got {points} point") 
  # elif ((a == choices[1]) and (b == choices[2] )) :
  #   print (f"Congrats!, You have got {points} point")
  # elif ((a == choices[2]) and (b == choices[0] )) :
  #   print (f"Congrats!, You have got {points} point")
  # elif ((a == choices[2]) and (b == choices[1] )) :
  #   print (f"Computer has got {points} point")
# def get_user_choice():
#     print("Enter your choice: Rock, Paper, or Scissors")
#     user_choice = input().capitalize()
#     return user_choice

# def get_computer_choice():
#     choices = ["Rock", "Paper", "Scissors"]
#     computer_choice = random.choice(choices)
#     return computer_choice

# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "It's a tie!", 0
#     elif (user_choice == "Rock" and computer_choice == "Scissors") or \
#          (user_choice == "Paper" and computer_choice == "Rock") or \
#          (user_choice == "Scissors" and computer_choice == "Paper"):
#         return "You win!", 1
#     else:
#         return "Computer wins!", -1

# def play_game():
#     user_score = 0
#     computer_score = 0
#     rounds = 3

#     for _ in range(rounds):
#         user_choice = get_user_choice()
#         computer_choice = get_computer_choice()

#         print("You chose:", user_choice)
#         print("Computer chose:", computer_choice)

#         result, score = determine_winner(user_choice, computer_choice)
#         print(result)

#         user_score += score

#     print("\nGame Over!")
#     print("Your score:", user_score)
#     print("Computer's score:", computer_score)

# if __name__ == "__main__":
#     play_game()
