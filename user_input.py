from main import GalacticSpacecraft

def get_coordinate_input(prompt):
    while True:
        coordinate = input(prompt)
        if coordinate.isdigit():
            return int(coordinate)
        else:
            print("Invalid input. Please enter a valid digit.")


def get_initial_direction():
    while True:
        initial_direction = input("Enter the initial direction (N, S, E, W, Up/U, Down/D): ").strip().lower()
        if initial_direction in ('n', 's', 'e', 'w', 'up', 'down'):
            return initial_direction.capitalize()
        else:
            print("Invalid input. Please enter a valid direction.")


x = get_coordinate_input("Enter the starting x-coordinate: ")
y = get_coordinate_input("Enter the starting y-coordinate: ")
z = get_coordinate_input("Enter the starting z-coordinate: ")
initial_direction = get_initial_direction()

while True:
    commands = input("Enter the commands as a string (e.g., 'frubl'): ")

    valid_commands = "frubld"

    try:
        if not all(char in valid_commands for char in commands):
            raise ValueError("Invalid commands. Only 'f', 'r', 'u', 'b', 'l', and 'd' are allowed.")

        spacecraft = GalacticSpacecraft(x, y, z, initial_direction)
        spacecraft.execute_commands(commands)
    except ValueError as e:
        print("Error:", e)
    else:
        final_position = (spacecraft.x, spacecraft.y, spacecraft.z)
        final_direction = spacecraft.direction

        print("Final Position:", final_position)
        print("Final Direction:", final_direction)
        break
