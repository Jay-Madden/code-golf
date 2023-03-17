# The Challenge:  Pachinko

This problem is inspired by Pachinko, a popular game in Japan. A traditional Pachinko machine is a cross between a vertical pinball machine and a slot machine. The player launches small steel balls to the top of the machine using a plunger as in pinball. A ball drops through a maze of pins that deflect the ball, and eventually the ball either exits at a hole in the bottom and is lost, or lands in one of many gates scattered throughout the machine which reward the player with more balls in varying amounts. Players who collect enough balls can trade them in for prizes.

For the purposes of this problem, a Pachinko machine is a sequence of one or more of the following: holes ("."), floor tiles ("_"), walls ("|"), and mountains ("/\"). 
A wall or mountain will never be adjacent to another wall or mountain. To play the game, a ball is dropped at random over some character within a machine.
A ball dropped onto a hole will fall through and be counted.
A ball dropped onto a floor tile stops immediately and is out of play. 
A ball dropped onto the left side of a mountain rolls to the left across any number of consecutive floor tiles until it falls into a hole, falls off the left end of the machine, or stops by hitting a wall or mountain. 
A ball dropped onto the right side of a mountain behaves similarly. 
A ball dropped onto a wall behaves as if it were dropped onto the left or right side of a mountain, with a 50% chance for each. If a ball is dropped at random over the machine. 
A ball that falls off the end is out of play
With all starting positions being equally likely, what is the probability that the ball will fall through a hole?
For example, consider the following machine, where the numbers just indicate character positions and are not part of the machine itself:
123456789
/\.|__/\.

So if the ball is dropped randomly:
- position 1 (the left side of the mountain) will roll out of the machine so it has 0% chance of going into the hole, 
- position 2 (right side of the mountain) will roll into a hole so it has a 100% chance of going into a hole, 
- position 3 (the hole) it has a 100% chance of going into the hole, 
- position 4 (the wall) it has a 50% chance of going into the hole
    - there is a 50% chance it could fall on the left or right of a wall so
	    - if it falls on the left, it has a 100% chance of going in the hole
	    - if it falls on the right, it will roll along all the floors and hit the mountain meaning it has 0% chance of going into the hole 
	- so as a whole, 100 + 0 / 2 gives me 50%
- position 5 (a floor) will stay in place so has 0% chance of going into a hole, 
- position 6 (a floor) will stay in place so it has 0% chance of going into a hole, 
- position 7 (left side of mountain) it has 0% chance of going into a hole, 
- position 8 (right side of mountain) will roll into a hole so it has 100% chance of going into a hole, 
- position 9 (a hole) it has a 100% chance of going into a hole.
So as a whole, the overall average is all of the percentages divided by the total number of positions so (0 + 100 + 100 + 50 + 0 + 0 + 0 + 100 + 100) / 9 so it would be 50%. More can be seen about the math here https://en.wikipedia.org/wiki/Law_of_total_probability
Do remember however that if we were to end up with an overall average of 61.61% the result, we're looking for is 61% as we only want the integer percentage
Inputs & Outputs
Input: The input consists of a string containing 1 – 99 characters.
Output: For each machine, compute as accurately as possible the probability that a ball will fall through a hole or off the end when dropped at random, then output that percentage truncated to an integer by dropping any fractional part (do not round).
Scoring
The solution must pass all tests for the score to be considered.
Test program
Test cases [Pachinko.txt file] are provided to help screen entries.
Any script that passes the test cases can be submitted. If you are surprised that your solution passed the test cases, please submit it anyway! 
Your score can be determined by using the linux command 
	wc -m filename

Coding GOLF - How To Play
Most importantly, anybody can play
The object in "real" golf is to hit the ball in the hole in the fewest strokes. The object in Coding Golf is to get from input (tee) to target (hole) in the fewest keystrokes.
Example: How many positive elements are in array $a?
Array $a could be of structure $a=[1, 2 ,-3, 4, -5, -7, 8, 9]
One approach:
for $b=0 to ubound($a)
  if $a[$b]>0
    $c=$c+1
  endif
next
for a score of 61.

Another solution is:
DO
  $b=$b+1
  if $a[$b]>0
    $c=$c+1
  endif
UNTIL $b>(UBOUND($a)+1)
for a score of 70.
Better approach: Code sample 1

Coding GOLF - The Rules
1)	The goal of Coding Golf is to score the lowest (key)strokes.
2)	This challenge must be done in Python.
3)	Strokes are all characters in a piece of code including space and carriage returns. 
a.	Example: 
i.	$arr.vortex = [1,1,1,1]  would have a score of 23
ii.	$=[1,1,1,1] would have a score of 11
4)	Code can be constructed any way you like if it does not generate syntax or other errors when running the script.
5)	The final solution MUST pass all test scripts that are part of the Coding golf challenge.
6)	During the private coding phase, no code is allowed to be posted. Violations result in disqualification of said player.
7)	During the public coding phase, code should be posted, reused, and borrowed from other players.
8)	You can submit scores as often as you want. 
9)	If you get a score lower than what has been posted, you are obligated to post your score immediately so others can try to compete with you. 
10)	You may assume ASCII as character set. 
11)	Tokenizing the script, or portions thereof is not allowed. 
12)	External Libraries are not allowed, all data manipulation must be present in your script.
13)	If something is not explicitly denied by the rules, it's allowed.
14)	If Confusion arises, arranger of the Golf round has the final say.

Coding GOLF - The Duration of the Competition

1)	The challenge will be released at 9:30 AM to the selected pairs – where you will have till 1:00 PM to find a solution and begin the golfing of your code.
2)	At 2:00 Central a mob session will begin where all private code is to be made public and the team will work as a single entity to get to the smallest score possible.
The Winner as determined by the judges will get to pick out the inspiration for Waynes next hair coloring.
The #devex-coding-golf Slack channel will be open for clarification of rules or questions to the challenge.


Most importantly HAVE FUN!
