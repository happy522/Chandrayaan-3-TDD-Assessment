import unittest

class GalacticSpacecraft:
    def __init__(self, x, y, z, direction):
        # Initialize the spacecraft's position (x, y, z) and direction (N, S, E, W, Up, Down)
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move_forward(self):
        # Move the spacecraft one step forward based on its current direction
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1
        elif self.direction == 'Up':
            self.z += 1
        elif self.direction == 'Down':
            self.z -= 1

    def move_backward(self):
        # Move the spacecraft one step backward based on its current direction
        if self.direction == 'N':
            self.y -= 1
        elif self.direction == 'S':
            self.y += 1
        elif self.direction == 'E':
            self.x -= 1
        elif self.direction == 'W':
            self.x += 1
        elif self.direction == 'Up':
            self.z -= 1
        elif self.direction == 'Down':
            self.z += 1

    def turn_left(self):
        # Turn the spacecraft 90 degrees to the left
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        # Turn the spacecraft 90 degrees to the right
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def turn_up(self):
        # Turn the spacecraft upwards
        if self.direction == 'N':
            self.direction = 'Up'
        elif self.direction == 'S':
            self.direction = 'Down'
        elif self.direction == 'Up':
            self.direction = 'S'
        elif self.direction == 'Down':
            self.direction = 'N'

    def turn_down(self):
        # Turn the spacecraft downwards
        if self.direction == 'N':
            self.direction = 'Down'
        elif self.direction == 'S':
            self.direction = 'Up'
        elif self.direction == 'Up':
            self.direction = 'N'
        elif self.direction == 'Down':
            self.direction = 'S'

    def execute_commands(self, commands):
        # Execute a sequence of commands to control the spacecraft
        for command in commands:
            if command == 'f':
                self.move_forward()  # Move the spacecraft forward
            elif command == 'b':
                self.move_backward()  # Move the spacecraft backward
            elif command == 'l':
                self.turn_left()  # Turn the spacecraft left
            elif command == 'r':
                self.turn_right()  # Turn the spacecraft right
            elif command == 'u':
                self.turn_up()  # Turn the spacecraft up
            elif command == 'd':
                self.turn_down()  # Turn the spacecraft down

# Implementation without TDD
starting_position = (0, 0, 0)
initial_direction = 'N'
commands = ['f', 'r', 'u', 'b', 'l']

spacecraft_without_tdd = GalacticSpacecraft(*starting_position, initial_direction)
spacecraft_without_tdd.execute_commands(commands)

print("Without TDD:")
print("Final Position:", (spacecraft_without_tdd.x, spacecraft_without_tdd.y, spacecraft_without_tdd.z))
print("Final Direction:", spacecraft_without_tdd.direction)

# Implementation with TDD
class TestGalacticSpacecraft(unittest.TestCase):
    def test_execute_commands(self):
        # Test the execute_commands method with example commands
        starting_position = (0, 0, 0)
        initial_direction = 'N'
        commands = ['f', 'r', 'u', 'b', 'l']

        # Create a spacecraft instance
        spacecraft_with_tdd = GalacticSpacecraft(*starting_position, initial_direction)
        # Execute the sequence of commands
        spacecraft_with_tdd.execute_commands(commands)

        # Verify the final position and direction
        final_position = (spacecraft_with_tdd.x, spacecraft_with_tdd.y, spacecraft_with_tdd.z)
        final_direction = spacecraft_with_tdd.direction

        # Check if the final position and direction match the expected values
        self.assertEqual(final_position, (-1,1,0))
        self.assertEqual(final_direction, 'N')

if __name__ == '__main__':
    print("\nWith TDD:")
    unittest.main()
