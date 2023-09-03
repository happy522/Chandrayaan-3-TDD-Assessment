from main import GalacticSpacecraft


# Implementation without TDD
starting_position = (0, 0, 0)
initial_direction = "N"
commands = ["f", "r", "u", "b", "l"]

spacecraft_without_tdd = GalacticSpacecraft(*starting_position, initial_direction)
spacecraft_without_tdd.execute_commands(commands)

print("\n--------------Default Input----------------------\n")

print("Without TDD:")
print(
    "Final Position:",
    (spacecraft_without_tdd.x, spacecraft_without_tdd.y, spacecraft_without_tdd.z),
)
print("Final Direction:", spacecraft_without_tdd.direction)

