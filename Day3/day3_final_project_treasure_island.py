print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("When typing your answer, write only the word between the asterisks (*)")

intersection_choice = input("\n You start walking on a sandy trail until you come across an intersection, it's dark and you can only hear the sounds of the forest,where do you choose to go? *left* or *right?* ")

if intersection_choice.lower() == "left":
  print("\n *******************************************************************************")
  lake_choice = input("\n You turn left and go straight ahead, after a few minutes of walking you come across a lake with crystal clear blue waters, do you decide to try *swim* or *wait* for a boat? ")
  
  if lake_choice.lower() == "wait":
    print("\n *******************************************************************************")
    door_choice = input("\n After a few minutes you notice a small wooden boat coming towards you, the boat, although empty, seems to be somehow being led towards you. When you get on the boat you realize that it doesn't have any type of oar or even an engine, but even so it starts to cross the lake and leaves you on the other side where you come across a large stone structure with 3 carved doors, one *red*, one *yellow* and one *blue* which one do you choose? ")
    
    if door_choice.lower() == "red":
      print("\n *******************************************************************************")
      print("\n As you enter the room the door behind you closes with a thud and disappears into the wall, you run to where the door should be when the room starts to heat up, and flames appear everywhere burning you alive. Game over")
    elif door_choice.lower() == "yellow":
      print("\n *******************************************************************************")
      print("\n Entering the door, a large room lights up revealing a large treasure chest in the middle of the room. \n YOU WIN!!!!!")
    elif door_choice.lower() == "blue":
      print("\n *******************************************************************************")
      print("\n You enter the room and feel the breath of a beast that hasn't eaten for days, when you try to turn back you realize that it's too late, because in the room there wasn't just one beast waiting for you, but more than you could count. Game over")
    else:
      print("\n *******************************************************************************")
      print("\n The mountain into which the structure was carved begins to collapse and you are caught in the debris, crushed. Game over")
      
  else:
    print("\n *******************************************************************************")
    print("\n You enter the lake and start swimming to get to the other side, when suddenly you feel a bite on your leg, when you feel the pain you look around and see yourself surrounded by trout that attack you until you can no longer defend yourself, and sink, half dead to the bottom of the lake where you will remain for the rest of eternity. Game Over")
  
else:
  print("\n *******************************************************************************")
  print("\nYou carefully turn to the right, paying attention to the sounds of the forest, as you take a few steps forward you feel the lack of a ground beneath your feet and realize that you are falling into a hole that seems to have no end. until you had yours. Game over.")