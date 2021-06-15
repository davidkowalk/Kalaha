from Board import Board, code_to_list
from sys import argv

def print_layout():
    print("╔══╦══╦══╦══╦══╦══╦══╦══╗")
    print("║  ║ 6║ 5║ 4║ 3║ 2║ 1║  ║ <- Player 2")
    print("║  ╠══╬══╬══╬══╬══╬══╣  ║")
    print("║  ║ 1║ 2║ 3║ 4║ 5║ 6║  ║ <- Player 1")
    print("╚══╩══╩══╩══╩══╩══╩══╩══╝")

def lpad(str, length=2):
    num = len(str)
    return " "*(length-num)+str

def render(field):
    print("""
    ╔══╦══╦══╦══╦══╦══╦══╦══╗
    ║  ║{N}║{M}║{L}║{K}║{J}║{I}║  ║
    ║{A}╠══╬══╬══╬══╬══╬══╣{H}║
    ║  ║{B}║{C}║{D}║{E}║{F}║{G}║  ║
    ╚══╩══╩══╩══╩══╩══╩══╩══╝
    """.format(
            A = lpad(str(field[0])),
            B = lpad(str(field[1])),
            C = lpad(str(field[2])),
            D = lpad(str(field[3])),
            E = lpad(str(field[4])),
            F = lpad(str(field[5])),
            G = lpad(str(field[6])),
            H = lpad(str(field[7])),
            I = lpad(str(field[8])),
            J = lpad(str(field[9])),
            K = lpad(str(field[10])),
            L = lpad(str(field[11])),
            M = lpad(str(field[12])),
            N = lpad(str(field[13]))
        )
    )

def get_index(board):

    if board.game_ended():
        return 0

    while True:
        i = input(f"Player {board.current_player+1}:")

        if i == "exit":
            # Print board representation
            print(f"Continue with code \"{board.get_code()}\"")
            print("> python3 ./app.py <code>")
            exit()
        elif 0 < int(i) < 7:
            return int(i)+board.current_player*7
        else:
            #print("Please select number from 1 to 6 or exit via \"exit\"\r\033[A\033[A")
            print("Please select number from 1 to 6 or exit via \"exit\"")

def game_loop(b):
    while not b.ended:
        render(b.state)
        i = get_index(b)
        code = b.play(i)

        if code == 1:
            print("You can only play your own side.", end="")
        elif code == 2:
            print("You cannot play your Mancala.", end="")
        elif code == 3:
            print("The position you want to play must have a stone count higher than 0!", end="")
        elif code == 4:
            print("You ended in your Mancala. You may play again.", end="")
        elif code == 5:
            print(f"Player {(1-b.current_player)+1} took.", end="")
        elif code == -1:
            print(f"ERROR: Index {i} not on board....", end="")
        elif code == 6:
            print("Game Ended\n\n")
            winner = b.finalize()
            print(f"Player {winner+1} won!")
            render(b.state)
            break
        else:
            print(" "*90, end="")
            print(" "*30)
        #print("\r\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A") #Return to start

def main():
    #import colorama
    #colorama.init()

    if len(argv)>1:
        state = code_to_list(argv[1])
        b = Board(state)
    else:
        b = Board()

    print("Layout")
    print_layout()
    print("\nGAME")

    game_loop(b)



if __name__ == '__main__':
    main()
