import random

class TicTacTeo:
    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('_')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0,1)

    def fix_spot(self, row, col, player):
        if self.board[row][col] != '_':
            print("The spot is already occupied enter another spot")
            row, col = list(map(int, input("Enter row and column number to fix spot:").split()))
            self.board[row][col] = player
        else:
            self.board[row][col] = player

    def is_player_win(self,player):
        n = len(self.board)
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        for i in range(n):
            win = True
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '_':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'x' if player == 'o' else 'o'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()
        player = 'x' if self.get_random_first_player() == 1 else 'o'
        while True:
            print(f"Player {player} turn")
            self.show_board()
            row,col = list(map(int,input("Enter row and column number to fix spot:").split()))
            print()
            row = row-1
            col = col-1

            self.fix_spot(row, col, player)

            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            if self.is_board_filled():
                print("Match Draw!")
                break

            player = self.swap_player_turn(player)
        print()
        self.show_board()

tic_tac_teo = TicTacTeo()
tic_tac_teo.start()