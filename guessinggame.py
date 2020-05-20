#!/usr/bin/env python
# coding: utf-8

# In[ ]:



 
import random
  
hidden = random.randrange(1,1000)

#print(hidden)
def guess():
 guess = int(input("Please enter your guess Hrishikesh Hatimuria: "))
 if guess == hidden:
     print("Hit!,you guessed correct")
 elif guess < hidden:
     print("Your guess is too low")
 else:
     print("Your guess is too high")
     
     
guess()


# In[ ]:





# In[ ]:




