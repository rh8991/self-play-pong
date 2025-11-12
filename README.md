# Self-Play Pong

An AI-powered Pong game where artificial intelligence learns to play against itself using reinforcement learning. This project is currently in development.

## Project Status

🚧 **Work in Progress** - Currently implementing the base game mechanics before adding AI self-play capabilities.

## Current Features

- Two-player local gameplay (manual controls)
- Smooth paddle movement
- Ball physics with collision detection
- Paddle collision detection with bounce mechanics
- Score tracking and display
- Pause functionality (P key)
- Visual center line divider
- ESC key to quit game

## Requirements

- Python 3.x
- Pygame

## Installation

1. Install Python from [python.org](https://www.python.org/)
2. Clone or download this repository
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Or install Pygame directly:

   ```bash
   pip install pygame
   ```

## How to Play

Run the game:

```bash
python game.py
```

### Controls

**Left Paddle (Right side):**

- `↑` - Move up
- `↓` - Move down

**Right Paddle (Left side):**

- `W` - Move up
- `S` - Move down

**Game Controls:**

- `P` - Pause/Resume game
- `ESC` - Quit game

## Game Components

- **Screen Size:** 800x600 pixels
- **Paddle Speed:** 10 pixels per frame
- **Ball Speed:** 7 pixels per frame (horizontal and vertical)
- **Frame Rate:** 60 FPS
- **Score Display:** Large white numbers at top of screen

## License

Open source - feel free to modify and distribute.
