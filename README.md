# Chandrayaan 3 Lunar Craft: Galactic Space Craft Control

## Problem Statement

Welcome to the Chandrayaan 3 Lunar Craft project! As a scientist at ISRO, your mission is to develop a program that translates commands sent from Earth into instructions understood by the spacecraft. This cutting-edge lunar spacecraft, Chandrayaan 3, navigates through the galaxy using galactic coordinates represented by x, y, and z coordinates. The x-axis signifies east or west location, the y-axis denotes north or south location, and the z-axis represents the distance above or below the galactic plane.

## Requirements

You'll start with the spacecraft's initial position (x, y, z) and its facing direction (N, S, E, W, Up, Down). The spacecraft receives a character array of commands, and your task is to implement the following functionalities:

1. Move the spacecraft forward/backward (f, b): The spacecraft advances or reverses one step based on its current direction.
2. Turn the spacecraft left/right (l, r): The spacecraft rotates 90 degrees to the left or right, altering its facing direction.
3. Turn the spacecraft up/down (u, d): The spacecraft adjusts its angle by rotating upwards or downwards.

**Note:**

- The spacecraft’s initial direction (N, S, E, W, Up, Down) serves as the reference frame for movement and rotation.
- Diagonal movement or rotation is not allowed; the spacecraft moves only in its current facing direction.
- Assume that the spacecraft’s movements and rotations are rigid and bounded by the galactic boundaries.

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
