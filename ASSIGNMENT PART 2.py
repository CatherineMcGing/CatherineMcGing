import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
key = 0
treasure = 0
gold = 0

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

print("Welcome to the Adventure Dungeon Text Game!\n\n")

name = input("What is your name? ") #Gathering info about user
age = int(input("What is your age? "))

health = 10

if age >= 12:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()

    if (wants_to_play == "yes") or (wants_to_play == "y"):
        print("Starting...\n")
        time.sleep(1)  # Adding delays for extra effects
        print("Please wait!")
        time.sleep(1)
        count = 0 #While loop for dots
        while count != 5:
            print(".", end="")
            time.sleep(2/5)
            count += 1

        print("\nYou are staring with", health, "health.")
        print("Let's play!\n")

        time.sleep(2)

    else:
      print("\nYou are not old enough to play...")
      print("\nExiting...")
      count = 0
    while count != 5:
        print(".", end="")
        time.sleep(2/5)
        count += 1
    print()

    
#broken into sections, starting with "intro"
def intro():
  print ("You are about to enter a dungeon,"
  "there is also a chance to collect gold and treasure (IF YOU CAN FIND IT!) "
  "There is a door, set of stairs or a box, which one will you do:")
  time.sleep(1)
  print (""" A. Open the box
  B. Go up the stairs
  C. Enter through the door""")
  choice = input(">>> ") #Here is the first choice.
  if choice in answer_A:
    option_box()
  elif choice in answer_B:
    print ("\n You slowly creep up the stairs...")
    option_upstairs()
  elif choice in answer_C:
    option_door4()
  else:
    print (required)
    intro()

def option_box(): 
  print ("\n You open the box and find a key... "
  "you have collected 1 key, where would you like to go now?")
  key = 1
  time.sleep(1)
  print ("""  A. open door
  B. Go upstairs""")
  choice = input(">>> ")
  if choice in answer_A:
          option_door()
  elif choice in answer_B:
    print ("\n You have chosen to go upstairs...") 
    option_upstairs()
  else:
    print (required)
    intro()

def option_upstairs():
  print ("\nAfter climbing all those stairs, there is a key on the floor,"
         "do you want to pick it up? Y/N?")
  choice = input(">>> ")
  if choice in yes:
    key = 1 #adds a key
  else:
    key = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  A. Go north
    B. Go right
  C. Go back down stairs """)
  choice = input(">>> ")
  if choice in answer_A:
    print ("\n THERE IS A DRAGON AT THE TOP WHO JUST SAW YOU!!")
    time.sleep(5)
    print ("\n THE DRAGON GOT YA! YOU ARE DEAD...")
    print("Sorry ", name)
    exit()
  elif choice in answer_B:
    print ("\n You are entering room 2..."
           "\n\n unlocking the door with the key...")
    time.sleep(3)
    option_2()
  if choice in no:
    key = 0
    print ("\nYou should of taken the key,"
            "you will have to "
            "make your way"
            "back to the entrance "
            "without getting KILLED!!")
    option_2()
    
  elif choice in answer_C:
      print (" You are making your way back down stairs...")
      Down_Stairs()

  else:
    print("GAME OVER")


def option_door4():
  print ("\nYou enter room 4, do you want to go left or right?")
  print ("""A. Turn left, B. Turn right or C. Exit the room""")
  choice = input(">>> ")
  if choice in answer_A:
        option_left()
  elif choice in answer_B:
        option_right()
  elif choice in answer_C:
    print("You have exit room 4...")
    time.sleep(4)
    option_enterance()
  else:
    print (required)
    
    
def Down_Stairs():
  print ("\n Back down stairs, there is a box with a "
         "key in it... do you take it? Y/N")
  choice = input(">>> ")
  if choice in yes:
    key = 1 #adds a key
  else:
    key = 0
  print (" you have just found a box of treasure...and open it with one of your keys...")
  time.sleep(1)
  if key > 0:
    print ("\n YOU MANAGED TO EXIT THE DUNGEON!!! YOU WON")
  else: #If the user didn't grab the treasure
     print ("\nMaybe you should have picked up the treasure. "
     "\n\n GAME OVER")


def option_2():
  input("Do you want to go left or right?")
  if input == "right":
    print("You have just turned right"
          "There is no sign of keys"
          "Would you like go downstairs?")
    direction = input("Yes \ No")
    if (direction == "yes") or (direction == "y"): 
       print("You are going back down stairs...")
       time.sleep(5)
       Down_Stairs()
  else:
      print("You have just turned left... this takes you back"
            "to the corridor"
            "You can only go north now..."
            "WAIT... A DRAGON HAS JUST WOKEN UP")
      print("Sorry" , name)
      time.sleep(5)
      print("IT HAS JUST EATEN YOU... YOUR DEAD!!!"
            "GAME OVER")
      exit()
      
def option_nextRoom():
  print("You have entered room 2. there is a collection of gold...")
  pick_up_gold == input(("Do you pick it up???"))
  if (pick_up_gold == "yes") or (pick_up_gold == "y"):
    print("You have found the gold, you can exit the dungeon now.. "
          "find your way out... WITHOUT GETTING KILLED")
    gold = 1
    time.sleep(4)
    RightLeft = input("Right or left?")
    if RightLeft == ("Right"):
      print("You are going right.. do you want to look or move?")
      

def option_enterance():
  print(" You are back at the entrance, do you want to count your keys?"
        "Y / N ")
  if input == "Y":
    print(keys)
    print("Ok... where do you want to do now?\n", name)
    move = input("Look or move")
    if move == ("Look"):
      print("You are standing at the entrance... There is a door and a set of stairs"
            "You need to find the treasure to exit the dungeon...")
      count = 0
      while count != 5:
            print(".", end="")
            time.sleep(2/5)
            count += 1
      print("What would you like to do now?", name)
      input("Go north or upstairs?")
      if input == ("upstairs"):
        option_upstairs()
      else:
        option_nextroom()
    else:
        print("Moving into the next room...")
        option_nextRoom()
  else:
    print("ok... do you want to go into room 2? Yes or No? ")
    if input == ("Yes"):
      option_nextRoom()

    else:
      Print("Do you want to go upstairs?  Yes or No? ")
      if input == ("Yes"):
        print("Climbing upstairs....")
        while count != 5:
            print(".", end="")
            time.sleep(2/5)
            count += 1

      else:
        print("You have been standing at the entrance for to long..."
              "Someone caught you... your DEAD!!!")
        print(" Bye Bye", name)


def option_left():
  input = ("North, left or right?")
  if input == ("North" or "north"):
    option_North()
  elif input == ("Right" or "right"):
    option_right()
  else:
    option_left()


def option_right():
  input = ("South, Straight or left?")
  if input == ("South" or "south"):
    option_South()
  elif input == ("Straight" or "straight"):
    option_North()
  else:
    option_left()


def option_North():
  input = ("Right, South, Left?")
  if input == ("Right" or "right"):
    option_right()
  elif input == ("Left" or "left"):
    option_left()
  else:
    option_South()

def option_South():
  input(" North, Left or right?")
  if input == ("North") or ("north"):
    option_North()
  elif input == ("Left") or ("left"):
    option_left()
  else:
    option_right()


intro()
