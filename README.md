# Mario Bros Arcade Recreation

A 2D recreation of the classic Mario Bros. arcade gameplay developed in Python using the Pyxel game engine.

The project was created as an academic team project and focuses on object-oriented programming, game-state management, collision detection, enemy behavior, level progression, and procedural object creation.

## Features

- Four progressively more difficult levels
- Bonus coin-collection stage
- Multiple enemy types with different behaviors
- Player movement, jumping, gravity, and collisions
- Platform and obstacle interactions
- Coin collection
- Lives and scoring system
- Persistent high-score tracking
- Game-over and victory screens
- Object-oriented game architecture
- Factory-based creation of enemies, platforms, and coins

## Gameplay

The player progresses through several levels while defeating enemies and collecting points.

Different enemy types appear as the game advances:

- Turtles
- Crabs
- Flies

Each enemy has its own movement characteristics, dimensions, speed, and score value.

After completing the main levels, the player reaches a bonus stage focused on collecting coins.

The game also keeps track of the player's best score between sessions.

## Controls

The game uses keyboard input through Pyxel.

Movement and actions are handled directly by the player controller, while menu transitions allow the player to start the game, restart after losing, and progress through the different screens.

## Architecture

The project follows an object-oriented structure that separates the main game systems into different modules.

### Player

`Marioplayer` manages:

- Player movement
- Jumping
- Gravity
- Lives
- Score
- Enemy collisions
- Platform interactions

### Enemies

All enemies inherit from a common `Enemigo` base class.

```text
Enemigo
├── Tortuga
├── Cangrejo
└── Mosca
```

The base class stores common properties such as:

- Position
- Dimensions
- Speed
- Direction
- Score value
- Movement state
- Life state

Each enemy subclass implements its own movement and rendering behavior.

### Levels and Screens

The game separates level data from screen-specific behavior.

The different screens include:

- Start screen
- Level 1
- Level 2
- Level 3
- Level 4
- Bonus stage
- Game-over screen
- Victory screen

The main application controls transitions between these states.

### Object Factory

The `Fabrica` class is responsible for creating groups of:

- Enemies
- Platforms
- Coins

Configuration values such as enemy speeds, sizes, spawn positions, platform positions, and score values are centralized in the factory so they can be modified without changing the creation logic throughout the project.

## Project Structure

```text
.
├── Assets/
│   └── .gitkeep
├── Constantes/
│   ├── dimensiones.py
│   └── point.py
├── Enemigos/
│   ├── enemigos.py
│   ├── tortugas.py
│   ├── cangrejos.py
│   └── moscas.py
├── Fondos/
│   ├── niveles.py
│   ├── pantallas.py
│   ├── plataformas.py
│   ├── monedas.py
│   ├── tuberias.py
│   └── pow.py
├── Players/
│   └── marioplayer.py
├── Main.py
├── requirements.txt
├── score.txt
├── .gitignore
└── README.md
```

## Technologies

- Python
- Pyxel
- Object-Oriented Programming
- 2D game development

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

## Game Assets

The Pyxel resource file used during development is intentionally not included in this repository because it contains third-party game assets.

The application expects the resource file at:

```text
Assets/marioassets.pyxres
```

To run the game locally, a compatible Pyxel resource file must be placed at that location.

If the file is missing, the application will display an error explaining that the required game assets are not available.

The source code, game logic, architecture, and gameplay systems are included in this repository.

## Running the Game

Once the required resource file has been placed inside the `Assets` directory, run:

```bash
python Main.py
```

## High Score

The best score is stored locally in:

```text
score.txt
```

The file starts at:

```text
0
```

When the player finishes a game with a score higher than the current record, the value is automatically updated.

## Design

The project uses small reusable classes to represent common game concepts.

For example:

```text
Point
├── x
└── y

Dimension
├── velocity
├── width
└── height
```

Game objects combine these structures with their own behavior instead of storing all gameplay logic inside a single main file.

This approach keeps responsibilities separated between the player, enemies, levels, screens, and object creation logic.

## Possible Improvements

Future improvements could include:

- Replacing the original third-party assets with a completely original sprite set
- Adding automated tests for collision and scoring logic
- Moving additional gameplay constants into centralized configuration
- Improving screen and level reuse to reduce duplicated code
- Adding sound and music configuration
- Adding configurable controls
- Packaging the game as a standalone executable

## Academic Context

This project was developed as an academic team project to practice Python programming and object-oriented software design through the implementation of a complete 2D game.

The repository has been cleaned for portfolio use while preserving the original gameplay architecture and functionality.

## Disclaimer

This is a non-commercial academic project inspired by the classic Mario Bros. arcade game.

The original copyrighted game resource file used during development is not distributed with this repository.
