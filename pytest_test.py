import pytest
from main import GalacticSpacecraft

# Define test cases using parameterization
test_cases = [
    # Test case: (initial_x, initial_y, initial_z, initial_direction, commands, expected_final_position, expected_final_direction)
    (0, 0, 0, 'N', 'f', (0, 1, 0), 'N'),  # Move forward in the N direction
    (0, 0, 0, 'S', 'b', (0, 1, 0), 'S'),  # Move backward in the S direction
    (0, 0, 0, 'E', 'f', (1, 0, 0), 'E'),  # Move forward in the E direction
    (0, 0, 0, 'W', 'b', (1, 0, 0), 'W'),  # Move backward in the W direction
    (0, 0, 0, 'Up', 'u', (0, 0, 0), 'Down'),  # Turn up in the Up direction
    (0, 0, 0, 'Down', 'd', (0, 0, 0), 'Up'),  # Turn down in the Down direction
    (0, 0, 0, 'N', 'frubl', (0, 1, -1), 'N'),  # A sequence of commands
]

@pytest.mark.parametrize("initial_x, initial_y, initial_z, initial_direction, commands, expected_final_position, expected_final_direction", test_cases)
def test_spacecraft(initial_x, initial_y, initial_z, initial_direction, commands, expected_final_position, expected_final_direction):

    # Create a spacecraft instance
    spacecraft = GalacticSpacecraft(initial_x, initial_y, initial_z, initial_direction)

    # Execute the sequence of commands
    for command in commands:
        spacecraft.execute_commands(command)

    # Check the final position and direction
    assert (spacecraft.x, spacecraft.y, spacecraft.z) == expected_final_position
    assert spacecraft.direction == expected_final_direction
