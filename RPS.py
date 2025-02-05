#RPS.py
#Name: Ella Falk
#Date: 2/5/25
#Assignment: Lab 3
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  play = "Y"
  while play == "Y":
    #Randomly choose the computer between 'R', 'P', or 'S'
    computer = random.choice( [ "R", "P", "S"] )
    #Prompt the user for their RPS selection
    personChoice = input("Pick rock, paper, or scissors (R/P/S): ")
    if (personChoice == "R"):
      print("Player chose rock.")
    elif (personChoice == "P"):
      print("Player chose paper.")
    elif (personChoice == "S"):
      print("Player chose scissors.")

    if (computer == "R"):
      print("Computer chose rock.")
    elif (computer == "P"):
      print("Computer chose paper.")
    elif (computer == "S"):
      print("Computer chose scissors.")

    #Determine winner and state what happened to the user
    if (computer == personChoice):
      ties = ties + 1
      print("TIE")
    elif (computer == "R" and personChoice == "P"):
      wins = wins + 1
      print("WIN")
    elif (computer == "R" and personChoice == "S"):
      losses = losses + 1
      print("LOSS")
    elif (computer == "P" and personChoice == "R"):
      losses = losses + 1
      print("LOSS")
    elif (computer == "P" and personChoice == "S"):
      wins = wins + 1
      print("WIN")
    elif (computer == "S" and personChoice == "R"):
      wins = wins + 1
      print("WIN")
    elif (computer == "S" and personChoice == "P"):
      losses = losses + 1
      print("LOSS")
      
    #Ask the user if they would like to play again.
    play = input("Would you like to play again (Y/N): ")
  
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
