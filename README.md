
# CeeLo Game

This project is a console-based implementation of the traditional dice game, CeeLo. The game is developed in Python and does not include any graphical interface.

## Features
- **Simple Dice Rolling Mechanics**: Simulates the rolling of three dice.
- **Game Rules Implementation**: Follows the traditional rules of CeeLo.
- **Console Output**: Displays the results of each round in the console.

## Requirements
- Python 3.x

## How to Play
1. Clone the repository:
   ```sh
   git clone https://github.com/GiannisTsochlas/CeeLo_Game.git
   ```
2. Navigate to the project directory:
   ```sh
   cd CeeLo_Game
   ```
3. Run the game:
   ```sh
   python ceelo.py
   ```

## Game Rules
- **Rolling Dice**: Players take turns to roll three dice.
- **Winning Combinations**:
  - **4-5-6**: Automatic win.
  - **1-2-3**: Automatic loss.
  - **Triple (e.g., 2-2-2)**: Player with the highest triple wins.
  - **Pair + Single (e.g., 5-5-3)**: The single die is the score. Higher scores win.
- **Non-Winning Combinations**: If no winning combination is rolled, players reroll until a winning combination is achieved.
- **Ties**: In case of a tie, players reroll.
- **Specific Scenarios**:
  - **Highest Double**: When a player rolls two dice with the same number and the third die is different, the value of the third die determines the score. If both players have the same highest double, they reroll.
  - **Sequential Rolls**: If a player rolls three sequential numbers (e.g., 1-2-3 or 4-5-6), it can either result in an automatic win or loss depending on the sequence.

