# 🚀 Space Gamez

A simple 2D arcade-style space shooter built with Python. This project focuses on core game development concepts such as player movement, enemy spawning, collision detection, scoring, and sound effects.

## 🎮 Overview

Space Gamez is a classic shoot-'em-up where the player controls a spaceship and eliminates incoming enemies while trying to achieve the highest score possible. The game includes sound effects, multiple enemy types, and a persistent high score system.

## Live Demo

Live Link : [View Live Demo]()

![SpaceGame](/SpaceGamepic.png)

## 🧩 Features

* Player-controlled spaceship movement
* Multiple enemy sprites (EnemyA, EnemyB, EnemyC)
* Shooting mechanics
* Collision detection system
* Sound effects and background music
* Game over screen
* High score tracking (stored locally)

## 🛠️ Tech Stack

* Python
* Pygame

## 📁 Project Structure

```
SpaceGamez/
│── Game.py              # Main game file
│── EnemyA.png          # Enemy sprite
│── EnemyB.png
│── EnemyC.png
│── yellow.png          # Player sprite
│── backgroundspace.png # Background image
│── gameoverss.png      # Game over screen
│── high_score.txt      # Stores high score
│── *.mp3               # Sound effects and music
```

## ▶️ How to Run

1. Install Python (3.x recommended)
2. Install Pygame:

   ```bash
   pip install pygame
   ```
3. Navigate to the project folder:

   ```bash
   cd SpaceGamez
   ```
4. Run the game:

   ```bash
   python Game.py
   ```

## 🎯 Controls

* Arrow Keys → Move spaceship
* Spacebar → Shoot

## 💡 Notes

* Make sure all image and sound files remain in the same directory as `Game.py`.
* The game stores the highest score in `high_score.txt`.