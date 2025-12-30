# DISCLAIMER:
# This agent does NOT use reinforcement learning,
# supervised learning, or any data-driven methods.

from ai_player import AIPlayer
from config import *

class A_SHUVETA_JOVI(AIPlayer):

    def __init__(self, board):
        super().__init__(board)
        self.depth = 3  # Safe depth for bullet chess

    def get_best_move(self):
        best_score = -10**9
        best_move = None

        legal_moves = self.board.get_legal_moves()

        for move in legal_moves:
            self.board.make_move(move)
            score = self.minimax(self.depth - 1, False)
            self.board.undo_move()

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimax(self, depth, is_maximizing):
        game_state = self.board.get_game_state()
        if depth == 0 or game_state != "ongoing":
            return self.evaluate_board()

        legal_moves = self.board.get_legal_moves()

        if is_maximizing:
            best_value = -10**9
            for move in legal_moves:
                self.board.make_move(move)
                best_value = max(best_value,
                                 self.minimax(depth - 1, False))
                self.board.undo_move()
            return best_value
        else:
            best_value = 10**9
            for move in legal_moves:
                self.board.make_move(move)
                best_value = min(best_value,
                                 self.minimax(depth - 1, True))
                self.board.undo_move()
            return best_value

    def evaluate_board(self):
        score = 0

        for r in range(BOARD_HEIGHT):
            for c in range(BOARD_WIDTH):
                piece = self.board.board[r][c]
                if piece != EMPTY_SQUARE:
                    score += PIECE_VALUES[piece]

        # Small bonus for giving check (legal as per rules)
        if self.board.is_in_check():
            score += 2

        return score
