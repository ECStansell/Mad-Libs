# Starting file for Project 2 - Mad Libs
# Emily Stansell
# October 14th, 2023

#Greet the user and ask if they'd like to play of Mad Libs
print("Welcome to the 'Being your best self' Mad Libs Game!")
print()
game1 = input("Would you like to play a game (y/n)? ")
print()
# If the user agrees to play a game
if game1.lower() == "y":
  print("Great! Let's get started!")
  print()
  # Asks for the user's name
  player_name = input("What is your name? ")
  print()
  # Greets the user
  print("Hello, " + player_name.capitalize() + "!")
  print()
  #Set the default for the while loop
  repeatGame = "y"
  counter = 0
  while repeatGame.lower() == "y":
    counter += 1
    #Prompts the user to select a story
    print("Which story would you like to play? \n A. The Escaped Creature\n B. Follow Your Dreams.")
    print()
    story1 = input("Which story would you like to play (A/B)? ")
    print()
    # If the user chooses the first story
    if story1.lower() == "a":
      # Gather information for the blanks in the story
      print("Please enter some information for our story.")
      print()
      townName = input("Enter a town name: ")
      monster = input("Enter a kind of monster: ")
      adjective1 = input("Enter an adjective: ")
      name = input("Enter a name: ")
      pluralNoun = input("Enter a plural noun: ")
      verb = input("Enter a verb you do while happy: ")
      adjective2 = input("Enter another adjective: ")
      food = input("Enter the name of a food item: ")
      print()
      # Title of the story
      print("The Escaped Creature")
      print("====================")
      print()
      # Begin story using user input
      print("One night, in the sleepy town of " + townName.capitalize() + ", a(n) " + monster.lower() + " escaped from the lab of the local " + adjective1.lower() + " scientist, " + name.capitalize() + ".")
      print("The townspeople were afraid of the " + monster.lower() + " because the last creature to escape from the lab destroyed the town's supply of " + pluralNoun.lower() + ".")
      print("Before they could react, however, the " + monster.lower() + " began to " + verb.lower() + ".")
      print("The townspeople realized the " + monster.lower() + " was no threat and welcomed it to their town with a feast of " + adjective2.lower() + " " + food.lower() + ".")
      print("After the feast concluded, the " + monster.lower() + " changed into a human -- " + name.capitalize() + ".")
      print('"You thought I was "' + adjective1.lower() + '" and left me out of every party before this one. I just wanted to be accepted. Do better."')
      print("The scientist left, leaving the townspeople to think about how they treat others. " + name.capitalize() + " was included in all parties from that day on.")
      # Ask if the user would like to play again
      print()
      #display the counter
      print("You have created " + str(counter) + " tale(s)")
      repeatGame = input("Would you like to play again (y/n)? ")
      #If the user choose "n", they are told to have a good day. Loop does not repeat
      if repeatGame == "n":
        print("Have a good day!")
        #if the user chooses "y", they are taken back to the beginning of the loop
      elif repeatGame == "y":
        print()
        print("Great! Let's go again!")
        print()
      #If the user inputs something other than "y" or "n"
      else: 
        print("Invalid input. Try again.")
    #if the user chooses the second story
    elif story1.lower() == "b":
      # prompt the user to enter information for the story
      print("Please enter some information for our story.")
      print()
      maleName = input("Enter a male name: ")
      adjective3 = input("Enter an adjective: ")
      jobTitle = input("Enter a job title: ")
      collegeName = input("Enter the name of a college or university: ")
      verb2 = input("Enter a verb: ")
      nounPlural = input("Enter a plural noun: ")
      subject = input("Enter a school subject: ")  
      postiveAdjective = input("Enter a positive descriptive adjective: ")
      verb3 = input("Enter a verb ending in -ing: ")
      print()
      #Title of the story
      print("Follow Your Dreams")
      print("==================")
      print()
      #begin printing story with user input
      print("There was a monkey named " + maleName.capitalize() + " who wanted nothing more than to be a(n) " + adjective3 + " " + jobTitle + ", so he started attending his local college, " + collegeName.capitalize() + ".")
      print("He was the only monkey in campus, so people would stop and ask him to " + verb2 + " for " + nounPlural + ", and because of this, he was often late to class.")
      print("One day, in " + subject.capitalize() + " 101, his instructor told him if he was late once more, he'd fail the class due to his attendance, and that arriving late to class was disrespectful to her and the students that arrive on time. ")
      print("The next day, " + maleName.capitalize() + " raced to class, but as usual, was stopped by people who thought he was " + postiveAdjective.lower() + ".")
      print(maleName.capitalize() + " realized in that moment that he loved making people smile more than anything, but still he apologized and ran off to class, not wanting to be late.")
      print("He told his instructor that he wanted to be on time to show that he respected her, but that his passion was performance, not " + subject + ", so he would be dropping out of school to follow his dreams.")
      print(maleName.capitalize() + " thanked her, and turned to the door.")
      print("The instructor smiled and wished him luck as he ran out of the room, " + verb3.lower() + " away for joy.")
      # Ask if the user would like to play again
      print()
      #display the counter
      print("You have created " + str(counter) + " tale(s)")
      repeatGame = input("Would you like to play again (y/n)? ")
       #If the user choose "n", they are told to have a good day. Loop does not repeat
      if repeatGame == "n":
        print("Have a good day!")
      #if the user chooses "y", they are taken back to the beginning of the loop
      elif repeatGame == "y":
        print()
        print("Great! Let's go again!")
        print()
      #If the user inputs something other than "y" or "n"
      else: 
        print("Invalid input. Try again.")
    #if the user inputs something other than "A" or "B"
    else:
      print("Invalid input. Try again.")
      print()
#If the user decides not to play at this time
elif game1.lower() == "n":
  print("Okay, maybe next time.")
#If the user inputs something other that "y or n"
else:
  print("Invalid input. Try again.")
      