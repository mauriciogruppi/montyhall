# Monty Hall simulation

This problem shows how counterintuitive the aspects of probability can be.

Simulates the Monty Hall game (from the game show Let's Make a Deal) in which a contestant is presented to 3 doors behind one of which there is a prize, and behind the others there are goats (which are not prizes, for that matter).
The contestant chooses one of the three doors.
The game host opens one of the remaining doors hiding a goat.
The contestant is given a chance to change to the other door that has not been opened.
After choosing whether or not they'll change, the selected door is opened and prize (or goat) revealed.

## The Monty Hall problem
The Monty Hall problem became famous after being addressed to as a question to "Ask Marilyn" column in Parade magazine in 1990.
"Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?"
Marilyn von Savant (Parade's columnist) said there was a 2/3 chance of winning if the contestant changed doors against 1/3 if they did not change.
On the occasion, many specialists and PhD's wrote to Marilyn clamining that she was wrong.
As it turns out, she was right all along. Formal proofs had been developed back in 1975 for similar problems and the proof can be shown in a relatively easy manner.
You can also use this simulation to see the results for this version of the problem and to generalizations of it (by changing numbers of doors, prizes, opened doors).

More info: https://en.wikipedia.org/wiki/Monty_Hall_problem


##Usage
This program runs in simulation (sim) or play mode.
Sim mode runs a certain number of simulations automatically.
Play mode allows a human player to play the game.

### Simulation mode
Default parameters: games (1000), doors (3), prizes (1), opened (1).
Example: montyhall -mode sim -games 10000 -doors 3 -prizes 1 -opened 1

### Play mode
Usage: montyhall -play
