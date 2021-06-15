from binascii import hexlify, unhexlify

chest = {
    0: 7,
    1: 0
}

takes = {
    1: 13,
    2: 12,
    3: 11,
    4: 10,
    5: 9,
    6: 8,
    8: 6,
    9: 5,
    10: 4,
    11: 3,
    12: 2,
    13: 1
}

playable_range = {
    0: [1,2,3,4,5,6],
    1: [8,9,10,11,12,13]
}

def code_to_list(code):
    return list(unhexlify(code.encode("utf-8")))

class Board():

    def __init__(self, state=None, current_player = 0):

        if state == None:
            state = [0]+[6]*6+[0]+[6]*6
            #state = [0]*6+[1]+[1]*6+[0]

        self.state = state
        self.current_player = current_player
        self.ended = False

    def get_code(self):
        return hexlify(bytearray(self.state)).decode()

    def finalize(self):
        """
        Adds up all the stones on each side and returns the winning player.
        """

        for i in range(8,14):
             self.state[0] += self.state[i]
             self.state[i] = 0

        for i in range(1, 7):
            self.state[7] += self.state[i]
            self.state[i] = 0

        return int(self.state[0]>self.state[7])

    def game_ended(self):
        # Check if player can play
        for i in playable_range[self.current_player]:
            #print("Checking", i,":", self.state[i])
            if self.state[i] != 0:
                return False
        else:
            return True

    def play(self, index):

        """
        Takes index and modifies board accordingly.
        Return Codes:
        0: A-Ok
        1: Player tried to play other players position
        2: Player tried to play chest
        3: Player tried to play empty position
        4: Player may play again
        5: Player took
        6: Game Ended
        -1: Index not on board
        """

        #if self.current_player == 0 and 1 <= index <= 6:
        #    pass
        #elif self.current_player == 1 and 8 <= index <= 13:
        #    pass

        if self.game_ended():
            return 6

        #Illegal Moves
        if index in playable_range[1-self.current_player]:
            return 1
        elif index == chest[self.current_player]:
            return 2
        elif index > 13:
            return -1

        if self.state[index] == 0:
            return 3

        amount = self.state[index]
        self.state[index] = 0

        while amount > 1:

            index = (index+1)%14

            if index == chest[1-self.current_player]:
                #print("Skipping", index)
                continue

            self.state[index]+=1
            amount -= 1


        # Last stone
        index = (index+1)%14

        if index == chest[1-self.current_player]:
            index = (index+1)%14

        if index == chest[self.current_player]:
            #Player may play again
            self.state[index]+=1
            return 4
        elif self.state[index] == 0 and self.state[takes[index]] > 0 and index in playable_range[self.current_player]:
            #Take other player stones

            self.state[index]+=1
            self.state[chest[self.current_player]] += self.state[index]+self.state[takes[index]]

            self.state[index] = 0
            self.state[takes[index]] = 0

            self.current_player = 1-self.current_player

            return 5


        else:
            self.state[index]+=1
            self.current_player = 1-self.current_player
            return 0
