import time
startTime = time.time() #timer
#importing time module
#User answers varies USING LISTS
answer_left = ["Left", "left", "l", "go left"]
answer_right = ["Right", "right", "r", "go right"]
answer_north = ["North", "north", "n"]
answer_south = ["South", "south", "s", "go south"]
yes = ["Y", "y", "yes", "Yes"]
no = ["N", "n", "No", "no"]
#objects
key = 0  
treasure = 0
location = 0 
print("keys = ", key) #print function
required = ("\n Please answer left, right, North, yes or no")#\n new line syntax
requiredAGE = ("PLEASE ENTER YOUR AGE")


class Player:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        

print("\n\                          /"
     "\n\                          /"
     "\n \                        /"
       "\n ]                     |"
       "\n ]                     [   /  |"
       "\n ]___               ___[ ,'   |"
       "\n ]  ]\             /[  [ |:   |"
       "\n ]  ] \           / [  [ |:   |"
       "\n ]  ]  ]         [  [  [ |:   |"
       "\n ]  ]  ]__     __[  [  [ |:   |"
       "\n ]  ]  ] ]\ _ /[ [  [  [ |:   |"
       "\n ]  ]  ] ] | | [ [  [  [  :===="
       "\n ]  ]  ]_] | | [_[  [  ["
       "\n ]  ]  ]         [  [  ["
       "\n ]  ] /   `       \ [  ["
       "\n ]__]/             \[__["
       "\n ]                     ["
       "\n ]                     ["
       "\n ]                     ["
       "\n                        |"
      "\n/                        |"
     "\n/                         |")
name = input("What is your name?") #creating a variable
age = int(input("What is your age?")) #SETTING THE DATA TYPE TO INTEGER 
if age >= 12: #COMPARISON OPERATOR
    print("You are old enough to play!") 

    wants_to_play = input("do you want to play? ").lower()

    if (wants_to_play) in yes: #IN IS A PYTHON MEMBERSHIP OPERATOR. TESTS FOR A SEQUENCES SUCH AS TUPLES, STRINGS, LISTS.
        print("Starting...\n")
        time.sleep(1)
        print("Please wait!")
        time.sleep(1)
        count = 0
        while count != 5: #WHILE LOOP! #!= NOT EQUAL COMPARISON OPERATOR
            print(".", end="") #END PRINTS ON THE SAME LINE
            time.sleep(2/5)
            count += 1 #ASSIGNMENT OPERATOR

        print("Welcome to the text adventure dungeon game", name)
        print("Lets play!\n")

        time.sleep(2) #using the time module

    else:
        print("Ok... BYE") #finish this if statement 
        exit()
        

else:
    print("\nYou are not old enough to play...")#finish the first if statement
    print("\nExiting...")
    count = 0
    while count != 5:
        print(".", end="")
        time.sleep(2/5)
        count += 1
    exit()



        
print("Well, hello there...", name)
print(            
"\n    |------| "
"\n    |      | "
"\n----|------|---- "
"\n    | <> <>|     "
"\n    |   |  |     "
"\n    \______/     ")

def intro(): #DEFINE FUNCTION #first class object 
    print("You are about to enter a dungeon,"
          "Your job is to find the treasure for next level"
          "before the dragon wakes up!!!")

    print("There is a door to your left, "
          " A box to your right and "
          " A set of stairs facing north")
    time.sleep(1)

    print("\n      ___ "
   "\n  _______    [___]"
  "\n  |      |   [___]"
  "\n  |      |   [___]"
  "\n  |      |   [___]"
  "\n  |    o |   [___]     |------| "
  "\n  |      |   [___]     |      | "
  "\n  |      |   [___]     |      | "
  "\n  |      |   [___]     |______| "
  "\n  |______|   [___]")

    print(" Where would you like to go?")
    print(" Right, Left or North?")
    choice = input(">>> ") #Here is the first choice.
    if choice in answer_right:
        option_box() #call the function
    elif choice in answer_north: #ELIF IS A KEYWORD OF PYTHON TO SAY IF THE PREVIOUS ISNT TRUE THEN TRY THIS
        print ("\n You slowly creep up the stairs...")
        option_upstairs()
    elif choice in answer_left:
        option_door()
    else:
        print(required)
        intro()
    
def option_box(): # def function
    location = 1
    print("You have choose to open the box... but what is"
          "inside? would you like to open it?") #Drawing a graphic
    print("\n                    "
          "\n    ______________  "
          "\n   |              | "
          "\n   |              | "
          "\n   |              | "
          "\n   |              | "
          "\n   |   B  O  X    | "
          "\n   |              | "
          "\n   |              | "
          "\n   |______________| ")
    print("Yes or no? ") #user options
    choice = input(">>> ") #input variable
    if choice in yes:
        print("There is a key!!!")
        print("Would you like to take it? yes or no")
        answer = input(">>> ")
        if answer in yes:
            print("You have collected a key")
            global key
            key += 1
            print("keys = ", key)
            print("Where would you like to go now?")
            print(" Right, left or north?")
            choice = input(">>> ")
            if choice in answer_right:
                option_upstairs() #function
            elif choice in answer_north:
                option_door()
            else:
                executionTime = (time.time() - startTime)
                print('Execution time in seconds: ' + str(executionTime))
                exit()
        else:
            print("You will not be able to open all doors which means"
                  "there is a chance of you getting killed")
            print("Where would you like to go now?")
            InPutAns = input("Right or North?")
            if InPutAns in answer_right:
                option_upstairs()
            else:
                option_door()
                
    else:
        print("Ok... where would you like to go now then?")
        print(" Right, left or north")
        answer = input(">>> ")
        if answer in answer_right:
            option_upstairs()
        elif answer in answer_north:
            option_door()
        else:
            print("You just chosen to exit...")
            time.sleep(2)
            print("Good bye", name)
            exit()




def option_door():  #def function
    location = 3 
    print("You just entered through the first door...")
    print("There is a fireplace on the left, a window to the "
          "North including a desk and a hidden gate to the right")
    print("Where would you like to go? North, Left or Right?")
    choice = input(">>> ")
    if choice in answer_left:
        print("\n  -----------------       "
              "\n | |-----------|  |       "
              "\n | |           |  |       "
              "\n | |           |  |       "
              "\n | |   ####    |  |       "
              "\n | | #######   |  |       "
              "\n | |#########  |  |       "
              "\n | |###########|  |       ")
        print("there is nothing around the fireplace, where"
              "would you like to go now?")
        print("Right or north")
        answer = input(">>>")
        if answer in answer_right:
            hidden_gate()
        else:
            window1()
    elif choice in answer_north:
        print("\n    --------------       "
              "\n   ||    ||     ||      "
              "\n   ||    ||     ||      "
              "\n   ||    ||     ||      "
              "\n   ||____|| ____||      "
              "\n   ||____||_____||      "
              "\n   ||    ||     ||      "
              "\n   ||    ||     ||      "
              "\n   ||____||_____||      ")
        print("Would you like to look outside it? yes or no")
        answer = input(">>> ")
        if answer == yes:
            print("There is only trees, looking like a forest and a river but"
                  "You would need to find your way out of here...")
            time.sleep(2)
            print("\n W I T H O U T  "
                  "\n G E T T I N G  "
                  "\n K I L L E D    ")
            time.sleep(2)
            print("left or north?")
            command = input(">>>")
            if command == answer_left:
                hidden_gate()
            else: 
                enterance()
    else:
        hidden_gate()


                
                        

def option_upstairs():    #def function
    global key
    location = 2
    print("You have just creeped up all those stairs...")
    print("\n  ____                     "
          "\n |    |___                 "
          "\n |        |___             "
          "\n |            |___         "
          "\n |                |___     "
          "\n |                    |___ "
          "\n |                        |")
    print("There are 3 doors and 2 gates...")
    print("You also find a key hanging next to"
          "the fire stick on the wall... do you"
          "take it?")
    upchoice = input("Yes or no?")
    if upchoice in yes:
        key += 1
        print("you have collected", key," so far")
        print("Where would you like to go now?")
        print("Right, left or north?")
        moreChoice = input(">>> ")
        if moreChoice in answer_right:
            print("You are entering the door which says"
                  "\n D A N G E R    Z O N E ")
            print("3 broken windows... but there is a red"
                  "\n slimy colour outside... what could that be?"
                  "\n Would you want to go north and see what it is?"
                  "\n or quickly turn left and exit the room?")
            Dangerchoice = input(" North or left?")
            if Dangerchoice in answer_north:
                dragon()
            else:
                corridor()
        elif moreChoice in answer_left:
            print("There is only one door to the left which is hanging off")
            time.sleep(2)
            print("Entering room...")
            print("There is more stairs... would you like to go up?")
            ChoiceUp = input(" Yes or no")
            if ChoiceUp in yes:
                Second_Set()
            else:
                print("ok... back into the corridor")
                corridor()
        else:
            print("There is 2 gates, they look dark and scary"
                  "Would you like to open one?")
            GateChoice = input("Yes or no")
            if GateChoice in answer_yes:
                dragon()
            else:
                dragon()
    else:
        print("You have collected", key," so far")
        print("\n You could of picked that one up to help"
              "\n you exit this scary dungeon")
        print("\n Where would you like to go now?")
        ElseChoice = input("Right, left or north")
        if ElseChoice in answer_right:
            print("You are entering the door which says"
                  "\n D A N G E R    Z O N E ")
            print("3 broken windows... but there is a red"
                  "\n slimy colour outside... what could that be?"
                  "\n Would you want to go north and see what it is?"
                  "\n or quickly turn left and exit the room?")
            Dangerchoice = input(" North or left?")
            if Dangerchoice in answer_north:
                dragon()
            else:
                corridor()
        elif ElseChoice in answer_left:
            print("There is only one door to the left which is hanging off")
            time.sleep(2)
            print("Entering room...")
            print("There is more stairs... would you like to go up?")
            ChoiceUp = input(" Yes or no")
            if ChoiceUp in yes:
                Second_Set()
            else:
                print("ok... back into the corridor")
                corridor()
        else:
            print("There is 2 gates, they look dark and scary"
                  "Would you like to open one?")
            GateChoice = input("Yes or no")
            if GateChoice in yes:
                dragon()
            else:
                dragon()

#def function
def hidden_gate():
    global key #CAN BE USED EVERYONE INSIDE AND OUTSIDE FUNCTIONS
    print("The hidden gate is locked...")
    print("You have ", key)
    if key >= 1:
        print("Yeeey you managed to open the gate to exit the dungeon...")
        print("\n W"
              "\n E"
              "\n L"
              "\n L"
              "\n   "
              "\n D"
              "\n O"
              "\n N"
              "\n E"
              "\n", name)
    else:
        print("You haven't collected enough keys to exit the dungeon!!!")
        print(" would you like to continue?")
        define = input("Yes or no")
        if define in yes:
            intro()
        else:
            exit()




def window1():
    print("You are at the window and see a river... where would you like to go?"
          "Right, Left or North?")
    print("\n        --------------       "
              "\n   ||    ||     ||      "
              "\n   ||    ||     ||      "
              "\n   ||    ||     ||      "
              "\n   ||____|| ____||      "
              "\n   ||____||_____||      "
              "\n   ||    ||     ||      "
              "\n   ||    ||     ||      "
              "\n   ||____||_____||      ")
    Valuechoice = input(" North, Left or right?")
    if Valuechoice in answer_left:
        hiddengate()
    elif Valuechoice in answer_north:
        enterance()
    else:
        corridor()
        
    
def enterance():
    print("You are back at the entrance of the dungeon...")
    print("There is a door to your left, "
          " A box to your right and "
          " A set of stairs facing north")
    time.sleep(1)

    print("\n      ___ "
  "\n  _______    [___]"
  "\n  |      |   [___]"
  "\n  |      |   [___]"
  "\n  |      |   [___]"
  "\n  |    o |   [___]     |------| "
  "\n  |      |   [___]     |      | "
  "\n  |      |   [___]     |      | "
  "\n  |      |   [___]     |______| "
  "\n  |______|   [___]")

    print(" Where would you like to go?")
    print(" Right, Left or North?")
    EnterChoice = input("Right, Left or North?")
    if EnterChoice in answer_right:
        option_door()
    elif EnterChoice in answer_left:
        option_box()
    else:
        option_upstairs()




def Second_Set():
    global treasure
    print("You creep up these spiral set of stairs and reach the top."
          "\n There is a bed but underneath there is a light"
          "\n Would you like to go and see what it is?")
    finalChoice = input("Yes or No")
    if finalChoice in yes:
        print("As you walk towards the bed"
              "\n You lift up the sheet"
              "\n it is a gold box shining")
        time.sleep(2)
        print("YOU FOUND THE TREASURE!!!!!!!!")
        print("GET OUT OF HERE BEFORE THE DRAGON WAKES UP")
        treasure = 1
        print("BACK DOWN STAIRS?")
        AnthrChoice = input("Yes or no?")
        if AnthrChoice in yes:
            corridor()
        else:
            dragon()
    else:
        print("ok, back down stairs?")
        ElseChoice = input(" Yes or no?")
        if ElseChoice in yes:
            corridor()
        else:
            dragon()


    

def corridor():
    print("Back to the corridor"
          "There are 2 gates to the left, the stairs to the right and 2 doors to the north...")
    doorChoice = input("Right, Left or North?")
    if doorChoice in answer_right:
        entrance()
    elif doorChoice in answer_left:
        print(key)
        if key >= 1:
            dragon()
        else:
            print("You don't have a key to open the gate...")
            print("Would you like to go in the other door to the right or downstairs to the north?")
            AnothChoice = input("Right or North?")
            if AnothChoice is answer_right:
                option_door()
            else:
                entrance()
    else:
        print("You are entering a small back room that has no windows... As you moved there"
              "The building started shaking!!! MAYBE THE DRAGON HAS WOKEN UP!!!")
        print("YOU NEED TO RUN NOW!!! WHAT WAY ARE YOU GOING?")
        Runchoice = input("LEFT FOR DOWNSTAIRS OR NORTH FOR THE OTHER ROOM")
        if Runchoice in answer_left:
            print("As you run down the stairs, you are coming back to the corridor. You are safe!!!")
            enterance()
        else:
            print("AS YOU HAVE ENTERERED THE OTHER ROOM!! THE DRAGON CAN SEE YOU THROUGH THE GATES!!"
                  "\n OH NOOOO ITS GOT YOU"
                  "\n SORRY", name)
            executionTime = (time.time() - startTime)
            print('Execution time in seconds: ' + str(executionTime))
            exit()
                  
    

def dragon():
    print("THE DRAGON IS COMING AFTER YOU!!!!")
    print("THE DRAGON IS SO FAST....")
    time.sleep(2)
    print(name, "sorry.... you are dead"
          " G A M E O V E R ")
    exit()
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))
    
intro()
