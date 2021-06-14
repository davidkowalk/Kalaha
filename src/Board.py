class Board():

    def __init__(self, state=[0]+[6]*6+[0]+[6]*6, current_player = 0):
        self.state = state
        self.current_player = current_player

    def play(self, index):

        """
        Takes index and modifies board accordingly.
        Return Codes:
        0: A-Ok
        1: Player tried to play other players position
        2: Player tried to play chest
        3: Number not on board
        """

        #if self.current_player == 0 and 1 <= index <= 6:
        #    pass
        if self.current_player == 0 and 7 <= index <= 13:
            return 1
        elif self.current_player == 0 and index == 0:
            return 2

        #elif self.current_player == 1 and 8 <= index <= 13:
        #    pass
        elif self.current_player == 1 and 0 <= index <= 6:
            return 1
        elif self.current_player == 1 and index == 7:
            return 2
        elif index > 13:
            return 3

        amount = self.state[index]
        self.state[index] = 0

        while amount > 0:

            if (self.current_player == 0 and index == 7) or (self.current_player == 1 and index == 0):
                continue

            index = (index+1)%14
            self.state[index]+=1
            amount -= 1
