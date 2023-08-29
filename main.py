import unittest

class GalacticSpacecraft:
    def __init__(self, x, y, z, direction):
        # Initialize the spacecraft's position and direction
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move_forward(self):
        # Move the spacecraft forward based on its current direction
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
        # Move the spacecraft backward based on its current direction
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
        # Turn the spacecraft's angle upwards
        if self.direction == 'N':
            self.direction = 'Up'
        elif self.direction == 'S':
            self.direction = 'Down'
        elif self.direction == 'Up':
            self.direction = 'S'
        elif self.direction == 'Down':
            self.direction = 'N'

    def turn_down(self):
        # Turn the spacecraft's angle downwards
        if self.direction == 'N':
            self.direction = 'Down'
        elif self.direction == 'S':
            self.direction = 'Up'
        elif self.direction == 'Up':
            self.direction = 'N'
        elif self.direction == 'Down':
            self.direction = 'S'

    def execute_commands(self, commands):
        # Execute the sequence of commands to control the spacecraft
        for command in commands:
            if command == 'f':
                self.move_forward()
            elif command == 'b':
                self.move_backward()
            elif command == 'l':
                self.turn_left()
            elif command == 'r':
                self.turn_right()
            elif command == 'u':
                self.turn_up()
            elif command == 'd':
                self.turn_down()

class TestGalacticSpacecraft(unittest.TestCase):
   def test_execute_commands(self):
        # Test the execute_commands method with corrected example commands
        starting_position = (0, 0, 0)
        initial_direction = 'N'
        commands = ['f', 'r', 'u', 'b', 'l']

        spacecraft = GalacticSpacecraft(*starting_position, initial_direction)
        spacecraft.execute_commands(commands)

        final_position = (spacecraft.x, spacecraft.y, spacecraft.z)
        final_direction = spacecraft.direction

        # Verify the final position and direction after executing commands
        self.assertEqual(final_position, (0, 1, 0))
        self.assertEqual(final_direction, 'N')

if __name__ == '__main__':
    unittest.main()




