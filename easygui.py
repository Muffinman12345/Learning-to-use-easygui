#Import the easygui module

import easygui

#At this point, we can just do a lot of things with easygui.
#Try easygui.msgbox("Hi!")
easygui.msgbox("hi!")
#The prompt can also be multi-choiced

flavors = easygui.buttonbox("What is your favorite ice cream flavor?", 
  choices = ['Vanilla', 'Chocolate', 'Strawberry'])
 
 #At the end, we can add a message box(msgbox)
 
 easygui.msgbox("You picked" + flavors)
 
 #But the problem is, that there are a lot of ice cream flavors! We can use the enterbox function
 
 flavor = easygui.enterbox("What is your favorite ice cream flavor?")
 easygui.msgbox("Your favorite ice cream flavor is " + flavor)
 
 
 #Now, let's make a game with easygui!
 
import random, easygui
secret = random.randint(1, 99)
guess = 0
tries = 0
easygui.msgbox("""AHOY! I'm the Dread Pirate Roberts, and I have a secret!
It is a number from 1 to 99. I'll give you 6 tries.""")
while guess != secret and tries < 6:
  guess = easygui.integerbox("What's yer guess, matey?") 
  if not guess: break
  if guess < secret:
   easygui.msgbox(str(guess) + " is too low, ye scurvy dog!")
  elif guess > secret:
   easygui.msgbox(str(guess) + " is too high, landlubber!")
   tries = tries + 1
  if guess == secret:
   easygui.msgbox("Avast! Ye got it! Found my secret, ye did!")
  else:
   easygui.msgbox("No more guesses! The number was " + str(secret))
   
   #It's kinda stupid, so try to change it some more.
