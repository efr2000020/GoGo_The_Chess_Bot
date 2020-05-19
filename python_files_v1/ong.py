import io
import chess
import chess.svg
import pandas as pd
import numpy as np
import os
import sys
from Chessnut import Game
import chess
import chess.svg

def board_to_fen(board):
    # Use StringIO to build string more efficiently than concatenating
    with io.StringIO() as s:
        for row in board:
            empty = 0
            for cell in row:
                c = cell[0]
                if c in ('w', 'b'):
                    if empty > 0:
                        s.write(str(empty))
                        empty = 0
                    s.write(cell[1].upper() if c == 'w' else cell[1].lower())
                else:
                    empty += 1
            if empty > 0:
                s.write(str(empty))
            s.write('/')
        # Move one position back to overwrite last '/'
        s.seek(s.tell() - 1)
        # If you do not have the additional information choose what to put
        s.write(' w KQkq - 0 1')
        return s.getvalue()
df = pd.read_excel('D:\msa courses\project\imageclassfication\imageclassify.xlsx', sheet_name='Sheet1')
a = np.array(df)

print(a)
print(board_to_fen(a))

board1 = chess.Board(board_to_fen(a))
print(board1)
board1


board= chess.Board(board_to_fen(a))
squares = board1.attacks(chess.E4)



svg_code =SVG(chess.svg.board(board=board, squares=squares))

