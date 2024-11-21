def checkmate(board):
    
    rows = board.strip().split('\n')
    
    
    if len(rows) != 4 or any(len(row) != 4 for row in rows):
        print("Chesstable is 4x4")
        return

    
    kings = []
    for i in range(4):
        for j in range(4):
            if rows[i][j] == 'K':
                kings.append((i, j))

    if not kings:
        print("Not Found King")
        return

    
    moves = {
        'P': [(1, -1), (1, 1)],  
        'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],  
        'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],  
        'Q': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],  
    }

    
    def is_in_bounds(x, y):
        return 0 <= x < 4 and 0 <= y < 4

    
    for king_x, king_y in kings:
        for i in range(4):
            for j in range(4):
                piece = rows[i][j]
                if piece in moves:
                    for dx, dy in moves[piece]:
                        x, y = i, j
                        while is_in_bounds(x + dx, y + dy):
                            x += dx
                            y += dy
                            if (x, y) == (king_x, king_y):  
                                print("Success")
                                return
                            if rows[x][y] != '.':  
                                break

    print("Fail")



if __name__ == "__main__":
    board = """\
K...
....
....
....
"""
    checkmate(board)
