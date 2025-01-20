# Functional Game Room

This project is a collection of fun and interactive Python games that run within the Python shell. All games are included in a single Python script, offering a unified gaming experience.

## Features
1. **Blackjack**
   - Fully functional card game with:
     - Randomized shuffling (using the `random` package).
     - Modular functions for deck creation, card dealing, and game logic.
     - Cumulative score tracking.
     - "Play again" functionality using global variables.

2. **Hangman**
   - Classic word-guessing game:
     - Randomly selects from six CSCI 220-themed words.
     - Tracks guesses and remaining attempts.

3. **High-Low**
   - Number comparison game:
     - Generates two random numbers.
     - Players guess if the displayed number is higher or lower than a hidden one.
     - Scoring adjusts based on guess difficulty.

4. **Slots**
   - Simulates a slot machine:
     - Randomly generates three numbers.
     - Scores based on matching patterns.

## Challenges
- **Threading and Graphics:** Attempted to incorporate a graphical element in other games, but threading issues caused unresponsiveness.
- **Complex Mechanics:** Explored advanced features, such as difficulty levels and timers, but deferred implementation for future updates.

## Lessons Learned
- Importance of pseudocode for planning complex games.
- Value of debugging through paired programming.
- Practical insights into Python features:
  - Global vs. local variables.
  - Random number generation (`random` package).
  - Efficient data handling with dictionaries.

## How to Play
1. Clone the repository:
   ```bash
   git clone https://github.com/emmanoonan/game-room.git
