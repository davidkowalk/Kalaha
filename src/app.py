def print_layout():
    print("╔═╦═╦═╦═╦═╦═╦═╦═╗")
    print("║ ║D║C║B║A║9║8║ ║")
    print("║0╠═╬═╬═╬═╬═╬═╣7║")
    print("║ ║1║2║3║4║5║6║ ║")
    print("╚═╩═╩═╩═╩═╩═╩═╩═╝")

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

def main():
    print("Layout")
    print_layout()
    print("\nGAME")

    render([6]*14)

if __name__ == '__main__':
    main()
