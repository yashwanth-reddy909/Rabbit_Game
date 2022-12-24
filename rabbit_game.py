import random
import os
import time

if os.name == "nt":
    import msvcrt


def clear_screen():
    _ = os.system("cls" if os.name == "nt" else "clear")


class Game:
    def __init__(self):
        self.map = self.generate_map()
        self.has_carrot = False

    def generate_map(self):
        map = "-" * 47 + "rcO"
        map = list(map)
        random.shuffle(map)
        self.rabbit_pos = map.index("r")
        self.carrot_pos = map.index("c")
        self.hole_pos = map.index("O")
        return map

    def move_rabbit(self, direction):
        if direction == "left":
            if self.rabbit_pos == 0:
                return
            elif self.rabbit_pos == self.hole_pos + 1:
                return
            elif self.has_carrot:
                self.rabbit_pos -= 1
                self.map[self.rabbit_pos] = "R"
                self.map[self.rabbit_pos + 1] = "-"
            elif self.rabbit_pos == self.carrot_pos + 1:
                return
            else:
                self.rabbit_pos -= 1
                self.map[self.rabbit_pos] = "r"
                self.map[self.rabbit_pos + 1] = "-"
        elif direction == "right":
            if self.rabbit_pos == 49:
                return
            elif self.rabbit_pos == self.hole_pos - 1:
                return
            elif self.has_carrot:
                self.rabbit_pos += 1
                self.map[self.rabbit_pos] = "R"
                self.map[self.rabbit_pos - 1] = "-"
            elif self.rabbit_pos == self.carrot_pos - 1:
                return
            else:
                self.rabbit_pos += 1
                self.map[self.rabbit_pos] = "r"
                self.map[self.rabbit_pos - 1] = "-"
        else:
            return

    def pick_up_carrot(self):
        if (
            self.rabbit_pos == self.carrot_pos - 1
            or self.rabbit_pos == self.carrot_pos + 1
        ) and self.has_carrot == False:
            self.map[self.rabbit_pos] = "R"
            self.has_carrot = True
            self.map[self.carrot_pos] = "-"

    def drop_carrot(self):
        if (
            self.rabbit_pos == self.hole_pos - 1 or self.rabbit_pos == self.hole_pos + 1
        ) and self.has_carrot == True:
            self.map[self.rabbit_pos] = "O"
            self.has_carrot = False
            self.map[self.carrot_pos] = "c"
            return True
        return False

    def jump(self):
        if self.rabbit_pos == self.hole_pos - 1:
            if self.hole_pos != 49:
                self.map[self.rabbit_pos] = "-"
                self.rabbit_pos += 2
                if self.has_carrot:
                    self.map[self.rabbit_pos] = "R"
                else:
                    self.map[self.rabbit_pos] = "r"
        elif self.rabbit_pos == self.hole_pos + 1:
            if self.hole_pos != 0:
                self.map[self.rabbit_pos] = "-"
                self.rabbit_pos -= 2
                if self.has_carrot:
                    self.map[self.rabbit_pos] = "R"
                else:
                    self.map[self.rabbit_pos] = "r"

    def play(self):
        while True:
            clear_screen()
            print("".join(self.map))
            if os.name == "nt":
                user_input = msvcrt.getch().decode("utf-8")
            else:
                user_input = input()
            if user_input == "a":
                self.move_rabbit("left")
            elif user_input == "d":
                self.move_rabbit("right")
            elif user_input == "p":
                if self.has_carrot:
                    if self.drop_carrot():
                        print("You won!")
                        time.sleep(2)
                        break
                else:
                    self.pick_up_carrot()
            elif user_input == "j":
                self.jump()
            else:
                continue
        print()

    def start_game(self):
        des = """--------------------------------
Welcome to the Rabbit Hole Game!
You are a rabbit who has to get a carrot from the other side of the field.
You can move left and right using the 'a' and 'd' keys.
You can pick up the carrot using the 'p' key.
You can jump across the rabbit hole using the 'j' key.
You can drop the carrot at the rabbit hole using the 'p' key.
--------------------------------"""
        print(des)
        input("Press enter to start the game...")
        while True:
            self.play()
            choice = input("Do you want to play again? (y/n): ")
            if choice == "y":
                self.map = self.generate_map()
                clear_screen()
            else:
                print("Thanks for playing!")
                break


game = Game()
game.start_game()
