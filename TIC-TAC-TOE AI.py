import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe AI")
        self.current_player = 'X'  # Human player
        self.board = [''] * 9
        self.buttons = []

        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 24), width=5, height=2,
                                   command=lambda i=i, j=j: self.handle_click(i, j))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def handle_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == '' and not self.is_game_over():
            self.make_move(index, 'X')
            if not self.is_game_over():
                self.ai_move()

    def make_move(self, index, player):
        self.board[index] = player
        self.buttons[index // 3][index % 3].configure(text=player)
        if self.is_winner(player):
            messagebox.showinfo("Game Over", f"{player} wins!")
            self.reset_board()
        elif '' not in self.board:
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_board()

    def ai_move(self):
        best_score = -float('inf')
        best_move = None
        for move in self.get_possible_moves():
            self.board[move] = 'O'
            score = self.minimax(False)
            self.board[move] = ''
            if score > best_score:
                best_score = score
                best_move = move
        self.make_move(best_move, 'O')

    def minimax(self, is_maximizing):
        if self.is_winner('O'):
            return 1
        elif self.is_winner('X'):
            return -1
        elif '' not in self.board:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for move in self.get_possible_moves():
                self.board[move] = 'O'
                score = self.minimax(False)
                self.board[move] = ''
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.get_possible_moves():
                self.board[move] = 'X'
                score = self.minimax(True)
                self.board[move] = ''
                best_score = min(score, best_score)
            return best_score

    def get_possible_moves(self):
        return [i for i, x in enumerate(self.board) if x == '']

    def is_winner(self, player):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def is_game_over(self):
        return self.is_winner('X') or self.is_winner('O') or '' not in self.board

    def reset_board(self):
        self.board = [''] * 9
        for row in self.buttons:
            for button in row:
                button.configure(text='')

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
