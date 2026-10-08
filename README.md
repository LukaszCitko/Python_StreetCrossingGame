# Street Crossing Game

A small desktop game made in 2021 with Python's built-in `turtle` module. Guide the turtle across the road while avoiding cars. Each successful crossing increases the level and the traffic speed.

## Run locally

You need Python 3 with Tkinter support and a desktop environment. The game has no third-party Python dependencies.

1. Clone this repository and open its directory in a terminal.
2. Run the game from the repository root so it can find the images in `gif/` and the high-score file `data.txt`:

   ```bash
   python3 main.py
   ```

   On Windows, use `py main.py` if `python3` is not available.
3. Click the game window, then use **Up** and **Down** to move. Reach the other side without touching a vehicle.

The best score is stored locally in `data.txt`. The game updates that file when you beat the record, so the directory must be writable.

## Project structure

- `main.py` — game loop, input, and collision handling.
- `player.py` — turtle movement.
- `car_manager.py` — traffic creation and movement.
- `scoreboard.py` — level display and high score.
- `gif/` — vehicle images used by the game.
