# import random
import os


class TicTacToe:
    Xpc = "X"
    Opc = "O"
    cpc = Xpc

    cords = "a1,b1,c1,a2,b2,c2,a3,b3,c3".split(",")

    cells = {
        "a1": "*",
        "b1": "*",
        "c1": "*",
        "a2": "*",
        "b2": "*",
        "c2": "*",
        "a3": "*",
        "b3": "*",
        "c3": "*",
    }

    def switchTurn(self):
        if self.cpc == self.Xpc:
            self.cpc = self.Opc
        elif self.cpc == self.Opc:
            self.cpc = self.Xpc

    def isValidPlace(self, cell):
        if cell in self.cells.keys():
            if self.cells[cell] == "*":
                return True
            print("cell has already been occupied")
        else:
            print(f"'{cell}' is not a valid position")

        return False

    def check_board(self):
        def full():
            return "*" not in self.cells.values()

        if full():
            print("Draw, no more moves can be made")

    def win(self):
        combs = [
            "a1,b1,c1",
            "a2,b2,c2",
            "a3,b3,c3",
            "a1,a2,a3",
            "b1,b2,b3",
            "c1,c2,c3",
            "a1,b2,c3",
            "c1,b2,a3",
        ]

        for combination in combs:
            wcells = combination.split(",")

            if all(self.cells[c] == "X" for c in wcells) or all(
                self.cells[c] == "O" for c in wcells
            ):
                winner = self.cells[wcells[0]]
                print(f"{winner} WINS the game")
                return True

    def p_place(self, cell):
        if self.isValidPlace(cell):
            self.cells[cell] = self.cpc
            self.switchTurn()

    def render_board(self):
        cords = self.cords
        d = 0
        print("  a b c")
        for r, x in enumerate(range(0, 8, 3), start=1):
            print(
                f"{str(r)}|{self.cells[cords[x]]}|{self.cells[cords[x + 1]]}|{self.cells[cords[x + 2]]}"
            )

            d += 1
            if d != 3:
                print(" |-+-+-")

    def reset(self):
        self.cells = {
            "a1": "*",
            "b1": "*",
            "c1": "*",
            "a2": "*",
            "b2": "*",
            "c2": "*",
            "a3": "*",
            "b3": "*",
            "c3": "*",
        }

    def run(self):
        self.render_board()
        while True:
            place = input("type in a coordinate to place your piece: ")

            os.system("clear")
            self.p_place(place)
            print(f"It's {self.cpc}'s turn")
            self.render_board()
            self.check_board()
            if self.win():
                self.reset()
                break


if __name__ == "__main__":
    game = TicTacToe()
    print("TIC TAC TOE\n")
    print("X and O\n")
    game.run()
    while True:
        c = input("Would you like to play again (y/n): ")
        if c == "n":
            break
        elif c == "y":
            os.system("clear")
            game.run()

    os.system("clear")
    quit()
# He he he