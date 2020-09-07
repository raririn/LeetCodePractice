class TicTacToe(object):

    def __init__(self, n: int) -> None:
        self.n = n
        self._board = [['.']*n for _ in range(n)]
        # Turn player: self.turn % 2
        self._turn = 0
        self._winning_conditions_cols = [[0, 0] for _ in range(n)]
        self._winning_conditions_rows = [[0, 0] for _ in range(n)]
        self._winning_conditions_diagons = [
            [0, 0],
            [0, 0],
        ]


    def __str__(self) -> str:
        n = self.n
        line_string = ("{} " * (n-1) + "{}\n")
        board_string = ""
        for i in range(n):
            board_string += line_string.format(*self._board[i])
        return board_string


    def getTurnPlayer(self) -> int:
        return self._turn % 2


    def _turnPass(self) -> None:
        self._turn += 1


    @staticmethod
    def player2mark(player: int) -> str:
        if player:
            return 'O'
        return 'X'


    def _increment_winning_counter(self, player: int, r: int, c: int) -> bool:
        self._winning_conditions_cols[c][player] += 1
        self._winning_conditions_rows[r][player] += 1

        if self._winning_conditions_cols[c][player] == self.n:
            return True
        if self._winning_conditions_rows[r][player] == self.n:
            return True
        if r == c:
            # Main diagon
            self._winning_conditions_diagons[0][player] += 1
            if self._winning_conditions_diagons[0][player] == self.n:
                return True
        if r + c == 2:
            # Sub diagon
            self._winning_conditions_diagons[1][player] += 1
            if self._winning_conditions_diagons[1][player] == self.n:
                return True
        

    def _move(self, player: int, r: int, c: int) -> bool:
        n = self.n
        if not (0 <= r <= n-1) or not (0 <= c <= n-1):
            raise IndexError('Out of range!')

        if self._board[r][c] != '.':
            raise Exception('Illegal move!')
        
        self._board[r][c] = self.player2mark(player)
        self._turnPass()


        return self._increment_winning_counter(player, r, c)


    def run(self):
        gameover = False
        while not gameover and self._turn < self.n * self.n:
            print("Turn {}: it is player {}'s turn.".format(self._turn, self.player2mark(self.getTurnPlayer())))
            print(self)

            input_row = input("Please input rol: ")
            input_col = input("Please input column: ")


            try:
                input_row = int(input_row)
                input_col = int(input_col)
            except:
                raise TypeError("Invalid input.")


            gameover = self._move(self.getTurnPlayer(), input_row, input_col)
        if self._turn == self.n * self.n:
            print("Game Over. Draw.")
        else:
            print(self)
            print("Game over. Player {} wins.".format(self.getTurnPlayer()))


if __name__ == "__main__":
    game = TicTacToe(3)
    game.run()