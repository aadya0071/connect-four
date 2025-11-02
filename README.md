# 🎮 Connect Four - Console Game

A simple two-player Connect Four game that runs in your terminal! No external libraries needed - just pure Python.

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

## 📋 Table of Contents
- [About](#about)
- [Demo](#demo)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Code Structure](#code-structure)
- [Features](#features)

---

## 🎯 About

Connect Four is a classic two-player connection game where players take turns dropping colored discs into a vertical grid. The objective is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs.

**Game Specifications:**
- Board: 6 rows × 7 columns
- Player 1: X
- Player 2: O
- Win Condition: 4 in a row (any direction)

---

## 🎬 Demo

```
 0 1 2 3 4 5 6
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | |O| | | |
| | |X|O| | | |
| |X|X|O|X| | |
---------------

Player 1's turn (X)
Choose a column (0-6): 3

🎉 Player 1 (X) wins! 🎉
```

---

## 💾 Installation

### Prerequisites
- Python 3.x

### Setup
1. Download or clone this repository

2. Navigate to the project directory:
```bash
cd connect-four
```

3. Run the game:
```bash
python connect_four.py
```

---

## 🕹️ How to Play

1. The game displays an empty 6×7 board with column numbers (0-6)
2. Player 1 (X) starts first
3. Enter a column number to drop your piece
4. Pieces fall to the lowest available position in that column
5. Players alternate turns
6. First player to connect 4 pieces wins!
7. Game ends in a draw if the board fills completely

### Valid Moves
- Enter a number between 0-6
- Column must not be full
- Invalid inputs will prompt you to try again

---

## 📁 Code Structure

```
connect_four.py
├── create_board()          # Creates empty 6×7 game board
├── print_board(board)      # Displays current board state
├── drop_piece()            # Places piece in selected column
├── winning_move()          # Checks for win conditions
├── is_board_full()         # Checks for draw condition
└── play_game()             # Main game loop
```

### Key Functions

#### `create_board()`
Creates and returns a 6×7 grid filled with empty spaces.

#### `print_board(board)`
Displays the current state of the board in the console with column numbers and borders.

#### `drop_piece(board, col, piece)`
Attempts to place a piece in the specified column. Returns `True` if successful, `False` if column is full.

#### `winning_move(board, piece)`
Checks all possible winning combinations:
- Horizontal (4 in a row)
- Vertical (4 in a column)
- Diagonal ascending (↗)
- Diagonal descending (↘)

#### `is_board_full(board)`
Returns `True` if the top row is completely filled (indicating a draw).

#### `play_game()`
Main game loop that:
- Manages player turns
- Handles user input
- Validates moves
- Checks win/draw conditions
- Displays results

---

## ✨ Features

- ✅ **Two-Player Gameplay** - Play with a friend locally
- ✅ **Input Validation** - Prevents invalid moves and handles errors gracefully
- ✅ **Win Detection** - Automatically detects all winning patterns
- ✅ **Draw Detection** - Recognizes when board is full
- ✅ **Clean UI** - Simple, easy-to-read console interface
- ✅ **Zero Dependencies** - No external libraries required
- ✅ **Beginner Friendly** - Well-commented code for learning

---

## 🎓 Learning Concepts

This project demonstrates:

| Concept | Usage |
|---------|-------|
| **Lists & 2D Arrays** | Board representation |
| **Functions** | Code organization and reusability |
| **Loops** | Game loop, board iteration |
| **Conditionals** | Move validation, win checking |
| **Exception Handling** | Input error management |
| **String Formatting** | Display messages |
| **Modulo Operator** | Turn alternation |

---

## 🚀 Future Enhancements

Possible improvements:
- [ ] Add single-player mode with AI opponent
- [ ] Implement minimax algorithm for smart AI
- [ ] Add color support using `colorama`
- [ ] Track game statistics (wins, losses, draws)
- [ ] Add undo/redo functionality
- [ ] Create GUI version with pygame
- [ ] Add difficulty levels
- [ ] Implement save/load game feature

---

## 👨‍💻 Authors

**Aadya Gupta**  
**Khushi Prasad**  
**Anika Nair**

---

## 🙏 Acknowledgments

- Inspired by the classic Connect Four board game
- Built as an educational project for learning Python fundamentals
- Thanks to the Python community for excellent documentation

---

**⭐ If you found this project helpful, please give it a star!**
