# Chandrayaan 3 TDD Assessment

## Problem Statement

As a scientist at ISRO controlling the latest lunar spacecraft Chandrayaan 3, your task is to develop a program that translates commands sent from Earth into instructions understood by the spacecraft. The spacecraft navigates through the galaxy using galactic coordinates, represented by x, y, z coordinates (x for east or west location, y for north or south location, and z for distance above or below the galactic plane).

### Requirements

You will be given the initial starting point (x, y, z) of the spacecraft and the direction it is facing (N, S, E, W, Up, Down). The spacecraft receives a character array of commands, and you are required to implement the following functionalities:

- Move the spacecraft forward/backward (f, b): The spacecraft moves one step forward or backward based on its current direction.
- Turn the spacecraft left/right (l, r): The spacecraft rotates 90 degrees to the left or right, changing its facing direction.
- Turn the spacecraft up/down (u, d): The spacecraft changes its angle, rotating upwards or downwards.

**Note:**

- The spacecraft’s initial direction (N, S, E, W, Up, Down) represents the reference frame for movement and rotation.
- The spacecraft cannot move or rotate diagonally; it can only move in the direction it is currently facing.
- Assume that the spacecraft’s movement and rotations are rigid, and it cannot move beyond the galactic boundaries.

**Changes:**
- Initial direction is Up and command provided is Up then the direction will be Down.
- Initial direction is Down and command provided is Down then the direction will be Up.

## Example

Given the starting point (0, 0, 0) with initial direction N, the following commands result in the indicated final position and direction:

Commands: ["f", "r", "u", "b", "l"]

Starting Position: (0, 0, 0)

Initial Direction: N

1. "f" - (0, 1, 0) - N
2. "r" - (0, 1, 0) - E
3. "u" - (0, 1, 0) - Up
4. "b" - (0, 1, -1) - Up
5. "l" - (0, 1, -1) - N

Final Position: (0, 1, -1)

Final Direction: N

## Files and Usage

1. **default_input.py** - This file contains the default input provided in the problem statement.

2. **main.py** - This is the main logic file where the spacecraft's behavior is implemented.

3. **pytest_test.py** - This file contains pytest tests for the spacecraft's functionality.

4. **unittest_test_default_input.py** - This file contains unittest tests for the spacecraft's functionality using the default input.

5. **user_input.py** - This file allows the user to input coordinates and directions with validation.

**Commands for testing using terminal:**
- python -m unittest unittest_test_default_input.py
- pytest pytest_test.py



