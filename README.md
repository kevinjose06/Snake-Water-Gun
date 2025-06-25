# 🔫 Gun-Water-Snake Game (Python)

A simple command-line Python game based on the classic *Gun-Water-Snake* logic. Think of it as the edgy cousin of Rock-Paper-Scissors.

---

## 🎮 How to Play

- Run the Python script.
- Choose one of the following options:
  - `g` for Gun
  - `w` for Water
  - `s` for Snake
  - `x` to Exit the game
- The computer will randomly pick its move.
- The winner is decided based on the following rules:

---

## 🧠 Game Rules

| Player | Computer | Result         |
|--------|----------|----------------|
| Gun    | Water    | Computer wins  |
| Gun    | Snake    | Player wins    |
| Water  | Gun      | Player wins    |
| Water  | Snake    | Computer wins  |
| Snake  | Water    | Player wins    |
| Snake  | Gun      | Computer wins  |
| Same   | Same     | It's a tie     |

---

## 🚀 Features

- Simple and beginner-friendly
- Uses Python's `random` module
- Clean terminal interface
- Infinite play loop until exit
- Error-handling for invalid input

---

## 🛠 Requirements

- Python 3.x
- No external libraries needed

---

## ▶️ How to Run

```bash
python gun_water_snake.py
