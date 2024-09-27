<h1>Rock Paper Scissors Game</h1>
<h3>Instructions</h3>
Welcome to the Rock, Paper, Scissors game! Follow the simple instructions below to play.

<h3>Rules of the Game:</h3>
Rock beats Scissors
Scissors beats Paper
Paper beats Rock
If both the player and the computer choose the same, it's a draw.
<h3>How to Play:</h3>
When the game starts, the player will be asked:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

Input the corresponding number to make your choice:

Type 0 for Rock
Type 1 for Paper
Type 2 for Scissors
The computer will randomly generate its choice of Rock, Paper, or Scissors.

The result will be compared, and feedback will be provided on whether you win, lose, or if it’s a draw.

<h3>Steps Involved in the Code:</h3>
Store the user's input:

The user’s choice will be stored as an integer (0 for Rock, 1 for Paper, 2 for Scissors).<br>

Generate a random choice for the computer:
Use the random module to generate a random integer between 0 and 2 for the computer's choice.<br>

Compare choices to determine the winner:
Compare the user's choice and the computer's choice based on the rules above to decide the result.<br>

Provide feedback:
Display the corresponding ASCII art for Rock, Paper, or Scissors.
Announce the winner or if it’s a draw.
