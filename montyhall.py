#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 12:08:07 2018

@author: mgruppi
Simulates the Monty Hall game

Given N shuffle doors behind some (usually one) of which there is a prize and behind the remaining there are goats.
Player wins if they choose the door which contains the prize.
Once a door is chosen, the game host opens some (again, usually one) goat doors 
and asks the player if they want to change to one of the unopened doors.
Finally, open the chosen door and check what's behind it.
"""

import random
import sys

#0 is goat, 1 is car
def get_shuffle(n=3,prizes=1):
    doors = [0]*n
    for i in range(0,prizes):
        doors[i] = 1
    random.shuffle(doors)
    return doors


def show_door(doors,chosen,notchosen):
    to_open = random.choice(notchosen)
    while doors[to_open] == 1:
        to_open = random.choice(notchosen) #open any of the not chosen doors (both goats)
    return to_open


def print_doors(strshow):
    print("|%s| |%s| |%s|" % (strshow[0],strshow[1],strshow[2]))

def play():
    choices = [0,1,2]
    strshow = ['D','D','D']
    shuffle = get_shuffle()
    print_doors(strshow)
    chosen = int(input("Pick a door (0, 1, 2): "))
    choices.remove(chosen)
    
    strshow[chosen] = 'X'
    to_open = show_door(shuffle,chosen,choices)
    choices.remove(to_open)
    strshow[to_open] = 'G'
    print_doors(strshow)
    
    change = int(input("Change (0/1)? "))
    
    if change == 1:
        chosen = choices[0]
    
    if shuffle[chosen] == 1:
        print("You win!")
    else:
        print("You lose!")
    print(shuffle)
    
def sim(change=0,n_doors = 3,prizes=1,open_doors = 1):
    #Generate list of choices and shuffle doors
    choices = list(range(0,n_doors))
    shuffle = get_shuffle(n_doors,prizes)
    
    #Choose a door at random
    chosen = random.choice(choices)
    choices.remove(chosen)
    
    #Choose a door to open
    for i in range(0,open_doors):
        to_open = show_door(shuffle,chosen,choices)
        choices.remove(to_open)
   
    #Random change (decide randomly to choose or not)
    if change == 2:
        change = random.randint(0,1)
    #Always change, no matter what, change doors 
    if change == 1:
        chosen = random.choice(choices)
    
    #Win or lose
    if shuffle[chosen] == 1:
        return 1
    else:
        return 0
    

def simulate(games,doors,prizes,opened):
    k_wins = 0
    c_wins = 0
    r_wins = 0
    print("Simulating Monty Hall with %d doors, %d prize(s), %d open doors for %d rounds." %(doors,prizes,opened,games))
      
    for i in range(0,games):
        k_wins += sim(0,doors,prizes,opened)
        c_wins += sim(1,doors,prizes,opened)
        r_wins += sim(2,doors,prizes,opened)
    
    print(">>> Never change: %d wins (%.3f) \n>>> Always change: %d wins (%.3f) \n>>> Random change: %d wins (%.3f)" %(k_wins,float(k_wins/games),c_wins,float(c_wins/games),r_wins,float(r_wins/games)))
    

#Main function
#Arguments: montyhall_sim -mode (sim | play) -samples (number of games, if sim) -doors (number of doors) -prizes (number of prizes)
        # -opened (number of doors opened by the host)
def main():
    random.seed()
    
    args = {} #stores arguments from CLI
    args["games"] = 1000 #games played in simulation mode
    args["doors"] = 3 #number of doors available for choosing
    args["opened"] = 1 #doors opened by the host
    args["prizes"] = 1 #numbero of prizes behind doors
    
    
    
    if len(sys.argv) < 3:
        print_usage()
        sys.exit(1)
    
    #Parse args
    for i in range(1,len(sys.argv),2):
        arg = sys.argv[i].lstrip('-')
        args[arg] = sys.argv[i+1]
    
    if not 'mode' in args.keys():
        print("Error: -mode argument is required.",file=sys.stderr)
        print_usage()
        sys.exit(1)
    
    if args["doors"] - args["opened"] < args["prizes"]:
        print("Error: cannot opend more doors than it is possible.")
        print_usage()
        sys.exit(1)
        
    if args['mode'] == 'sim':
        simulate(int(args["games"]),int(args["doors"]),int(args["prizes"]),int(args["opened"]))
    elif args['mode'] == 'play':
        play()
    else:
        print("Error: invalid mode: %s"%(args['mode']),file=sys.stderr)
        print_usage()
        sys.exit(1)
  
def print_usage():
       print("Usage:\n\tmontyhall -mode <play> (play the game in human friendly mode).",file=sys.stderr)
       print("\tmontyhall -mode <sim or play> -samples <#of games> (1000) -doors <# of doors>(3) -prizes <#of prizes>(1) -opened <#of opened>(1).",file=sys.stderr)

if __name__ == '__main__':
    main()
    

        