class GalacticSpacecraft:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move_forward(self, steps=1):
        # Move the spacecraft one step forward based on its current direction
        if self.direction == "N":
            self.y += steps
        elif self.direction == "S":
            self.y -= steps
        elif self.direction == "E":
            self.x += steps
        elif self.direction == "W":
            self.x -= steps
        elif self.direction == "Up":
            self.z += steps
        elif self.direction == "Down":
            self.z -= steps

    def move_backward(self, steps=1):
        # Move the spacecraft one step backward based on its current direction
        if self.direction == "N":
            self.y -= steps
        elif self.direction == "S":
            self.y += steps
        elif self.direction == "E":
            self.x -= steps
        elif self.direction == "W":
            self.x += steps
        elif self.direction == "Up":
            self.z -= steps
        elif self.direction == "Down":
            self.z += steps

    def turn_left(self):
        # Turn the spacecraft 90 degrees to the left
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"
        elif self.direction == "W":
            self.direction = "S"

    def turn_right(self):
        # Turn the spacecraft 90 degrees to the right
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "W":
            self.direction = "N"

    def turn_up(self):
        # Turn the spacecraft upwards
        if self.direction == "N":
            self.direction = "Up"
        elif self.direction == "S":
            self.direction = "Down"
        elif self.direction == "Up":
            self.direction = "S"
        elif self.direction == "Down":
            self.direction = "N"

    def turn_down(self):
        # Turn the spacecraft downwards
        if self.direction == "N":
            self.direction = "Down"
        elif self.direction == "S":
            self.direction = "Up"
        elif self.direction == "Up":
            self.direction = "N"
        elif self.direction == "Down":
            self.direction = "S"

    def execute_commands(self, commands):
        i = 0
        while i < len(commands):
            command = commands[i]

            print(f"Executing command: {command}")  # Print the executed command

            if command == "f":
                count = 1
                while i + 1 < len(commands) and commands[i + 1] == "f":
                    count += 1
                    i += 1
                self.move_forward(count)
            elif command == "b":
                count = 1
                while i + 1 < len(commands) and commands[i + 1] == "b":
                    count += 1
                    i += 1
                self.move_backward(count)
            elif command == "l":
                self.turn_left()
            elif command == "r":
                self.turn_right()
            elif command == "u":
                self.turn_up()
            elif command == "d":
                self.turn_down()
            i += 1


            print(f"Current Direction: {self.direction}")  # Print current direction
            print(f"Current Position (X, Y, Z): ({self.x}, {self.y}, {self.z})")  # Print current position

