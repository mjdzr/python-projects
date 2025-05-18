# 🕹️ Tic Tac Toe – Python Terminal Game

A simple terminal-based implementation of the classic Tic-Tac-Toe game written in Python. Two players can take turns marking `X` and `O` on a 3x3 grid until one wins or the game ends in a tie.

## 📋 Features

- Terminal-based gameplay  
- Two-player (local turn-based)  
- Random player selection to start  
- Tie detection when the board is full  

## 🧠 How It Works

- The game randomly selects which player (`X` or `O`) starts first.  
- Players take turns choosing a cell (1–9) to place their marker.  
- The board updates and is displayed after each turn.  
- The game ends when a player wins or the board is full (tie).  

## 📦 Requirements

- Python 3.x  

## ▶️ How to Run

   ```bash
   python src/main.py
   ```

## 🎮 Controls

- Enter a number from `1` to `9` to choose a cell:

```
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

- You’ll be prompted again if you:
  - Enter a non-number  
  - Choose a cell outside 1–9  
  - Choose an already marked cell  

## 🧩 Example Gameplay

```
   |   |   
-----------
   |   |   
-----------
   |   |   

Player X turn!
Choose a cell (1-9):
>> 5

   |   |   
-----------
   | X |   
-----------
   |   |   
```

## 🔧 Code Overview

The main game logic is encapsulated in the `TicTacToe` class:

- `start()`: Starts and runs the game loop.  
- `show_board()`: Prints the current board.  
- `mark_spot(player, cell)`: Places a mark on the board.  
- `has_player_won(player)`: Checks if a player has won.  
- `is_board_full()`: Checks for tie condition.  
- `swap_player()`: Switches turns.  

## 📄 License

This project is open-source and free to use under the MIT License.
