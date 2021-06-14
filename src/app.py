from Board import Board

def print_layout():
    print("╔══╦══╦══╦══╦══╦══╦══╦══╗")
    print("║  ║ 6║ 5║ 4║ 3║ 2║ 1║  ║ <- Player 2")
    print("║0 ╠══╬══╬══╬══╬══╬══╣ 0║")
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

def get_index(player):
    while True:
        i = int(input(f"Player {player+1}:"))

        if 0 < i < 7:
            return i+player*7
        else:
            print("Please select number from 1 to 6")

def main():
    print("Layout")
    print_layout()
    print("\nGAME")

    b = Board()
    while not b.ended:
        render(b.state)
        i = get_index(b.current_player)
        code = b.play(i)

        if code == 1:
            print("You can only play your own side.")
        elif code == 2:
            print("You cannot play your chest.")
        elif code == 3:
            print("The position you want to play must have a stone count higher than 0!")
        elif code == 4:
            print("You ended in your chest. You may play again.")
        elif code == 5:
            print(f"Player {(1-b.current_player)+1} took.")
        elif code == -1:
            print(f"ERROR: Index {i} not on board....")



if __name__ == '__main__':
    main()
