import unittest
from main import GalacticSpacecraft

class TestGalacticSpacecraft(unittest.TestCase):
    def test_move_forward(self):
        # Create a spacecraft instance with an initial position (0, 0, 0) and facing North (N)
        spacecraft = GalacticSpacecraft(0, 0, 0, 'N')

        # Move forward and check the final position
        spacecraft.move_forward()
        self.assertEqual((spacecraft.x, spacecraft.y, spacecraft.z), (0, 1, 0))

        # Additional test cases with different initial conditions and directions
        spacecraft = GalacticSpacecraft(1, 2, -1, 'S')
        spacecraft.move_forward()
        self.assertEqual((spacecraft.x, spacecraft.y, spacecraft.z), (1, 1, -1))

        spacecraft = GalacticSpacecraft(-2, 3, 0, 'E')
        spacecraft.move_forward()
        self.assertEqual((spacecraft.x, spacecraft.y, spacecraft.z), (-1, 3, 0))

    def test_move_backward(self):
        # Create a spacecraft instance with an initial position (0, 0, 0) and facing South (S)
        spacecraft = GalacticSpacecraft(0, 0, 0, 'S')

        # Move backward and check the final position
        spacecraft.move_backward()
        self.assertEqual((spacecraft.x, spacecraft.y, spacecraft.z), (0, 1, 0))

        # Additional test cases with different initial conditions and directions
        spacecraft = GalacticSpacecraft(1, -2, 3, 'E')
        spacecraft.move_backward()
        self.assertEqual((spacecraft.x, spacecraft.y, spacecraft.z), (0, -2, 3))

        spacecraft = GalacticSpacecraft(-1, 1, 1, 'W')
        spacecraft.move_backward()
        self.assertEqual((spacecraft.x, spacecraft.y, spacecraft.z), (0, 1, 1))

    def test_turn_left(self):
        # Create a spacecraft instance with an initial position (0, 0, 0) and facing North (N)
        spacecraft = GalacticSpacecraft(0, 0, 0, 'N')

        # Turn left and check the final direction
        spacecraft.turn_left()
        self.assertEqual(spacecraft.direction, 'W')

        # Additional test cases with different initial directions
        spacecraft = GalacticSpacecraft(0, 0, 0, 'E')
        spacecraft.turn_left()
        self.assertEqual(spacecraft.direction, 'N')

    def test_turn_right(self):
        # Create a spacecraft instance with an initial position (0, 0, 0) and facing North (N)
        spacecraft = GalacticSpacecraft(0, 0, 0, 'N')

        # Turn right and check the final direction
        spacecraft.turn_right()
        self.assertEqual(spacecraft.direction, 'E')

        # Additional test cases with different initial directions
        spacecraft = GalacticSpacecraft(0, 0, 0, 'S')
        spacecraft.turn_right()
        self.assertEqual(spacecraft.direction, 'W')

    def test_turn_up(self):
        # Create a spacecraft instance with an initial position (0, 0, 0) and facing North (N)
        spacecraft = GalacticSpacecraft(0, 0, 0, 'N')

        # Turn up and check the final direction
        spacecraft.turn_up()
        self.assertEqual(spacecraft.direction, 'Up')

        # Additional test cases with different initial directions
        spacecraft = GalacticSpacecraft(0, 0, 0, 'S')
        spacecraft.turn_up()
        self.assertEqual(spacecraft.direction, 'Down')

    def test_turn_down(self):
        # Create a spacecraft instance with an initial position (0, 0, 0) and facing North (N)
        spacecraft = GalacticSpacecraft(0, 0, 0, 'N')

        # Turn down and check the final direction
        spacecraft.turn_down()
        self.assertEqual(spacecraft.direction, 'Down')

        # Additional test cases with different initial directions
        spacecraft = GalacticSpacecraft(0, 0, 0, 'S')
        spacecraft.turn_down()
        self.assertEqual(spacecraft.direction, 'Up')

    def test_execute_commands(self):
        # Create a spacecraft instance with an initial position (0, 0, 0) and facing North (N)
        spacecraft = GalacticSpacecraft(0, 0, 0, 'N')

        # Execute a sequence of commands and check the final position and direction
        spacecraft.execute_commands('frubl')
        self.assertEqual((spacecraft.x, spacecraft.y, spacecraft.z), (0, 1, -1))
        self.assertEqual(spacecraft.direction, 'N')

        # Additional test cases with different initial conditions and commands


if __name__ == '__main__':
    unittest.main()
