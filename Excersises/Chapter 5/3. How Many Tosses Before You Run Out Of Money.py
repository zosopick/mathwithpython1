'''
We have a simple game played with a fair coin toss. A player wins $1 for heads and loses $1.50 for tails.
The game is over when players balance reaches 0.

Given a certain starting amount specified by the user as input, your challenge is to write a program
that simulates this game.

Assume there is an unlimited cash reserve with the computer.

'''

import random

def play(start_amount):
     win_amount=1
     loss_amount=1.5

     cur_amount=start_amount
     tosses=0

     while cur_amount>0:
          tosses+=1
          toss=random.randint(0,1)
          if toss==0:
               cur_amount+=win_amount
               print('Heads! Current amount: {0} '.format(cur_amount))
          else:
               cur_amount-=loss_amount
               print('Tails! Current amount: {0} '. format(cur_amount))
     print('Game over!  For ${0} you have played {1} games, and your current amount is {2}'.format(start_amount,tosses,cur_amount))
if __name__=='__main__':

     while True:
          start_amount=float(input('Please enter the starting amount: '))
          play(start_amount)

          answer=input('Do you want to exit? (y) for yes, anything else for no.  ')
          if answer=='y':
               break
