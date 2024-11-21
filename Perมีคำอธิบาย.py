def checkmate(board):
    """
    ตรวจสอบว่า King ถูกคุกคาม (in check) หรือไม่
    """
    rows = board.strip().split('\n')

    # ตรวจสอบว่ากระดานเป็นขนาด 4x4 หรือไม่
    if len(rows) != 4 or any(len(row) != 4 for row in rows):
        print("Chesstable is 4x4")
        return

    # ค้นหาตำแหน่งของตัว King (K) บนกระดาน
    kings = []
    for i in range(4):
        for j in range(4):
            if rows[i][j] == 'K':
                kings.append((i, j))

    if not kings:
        print("Not Found King")
        return

    # นิยามรูปแบบการเคลื่อนที่ของหมากแต่ละตัว
    moves = {
        'P': [(1, -1), (1, 1)],  # Pawn เดินทางแนวทแยงไปด้านหน้า
        'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],  # Rook เดินทางในแนวตรง
        'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],  # Bishop เดินทางแนวทแยง
        'Q': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],  # Queen เดินทางรวมของ Rook และ Bishop
    }

    # ฟังก์ชันช่วยตรวจสอบว่าตำแหน่งยังอยู่ในขอบเขตของกระดานหรือไม่
    def is_in_bounds(x, y):
        return 0 <= x < 4 and 0 <= y < 4

    # ตรวจสอบว่า King ตัวใดตัวหนึ่งอยู่ในสถานะถูกคุกคาม (check) หรือไม่
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
                            if (x, y) == (king_x, king_y):  # King อยู่ในตำแหน่งที่ถูกโจมตี
                                print("Success")
                                return True
                            if rows[x][y] != '.':  # มีหมากตัวอื่นขวางอยู่
                                break

    print("Fail")
    return False


def suggest_best_move(board):
    """
    แนะนำการเดินหมากที่ดีที่สุดเพื่อป้องกันหรือโจมตี King
    """
    rows = board.strip().split('\n')

    # ค้นหาตำแหน่งของหมากทั้งหมดและ King
    pieces = {}
    king_position = None

    for i in range(4):
        for j in range(4):
            piece = rows[i][j]
            if piece != '.':
                if piece == 'K':
                    king_position = (i, j)
                else:
                    pieces[(i, j)] = piece

    # หากไม่พบ King
    if not king_position:
        print("Not Found King")
        return

    # คำนวณการเดินที่ปลอดภัย
    safe_moves = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        x, y = king_position[0] + dx, king_position[1] + dy
        if 0 <= x < 4 and 0 <= y < 4 and rows[x][y] == '.':
            safe_moves.append((x, y))

    # ตรวจสอบการคุกคามในตำแหน่งใหม่
    for move in safe_moves:
        if not is_threatened(move, pieces, rows):
            print(f"Safe move King: {move}")
            return

    print("Not Found Safe move")


def is_threatened(position, pieces, rows):
    """
    ตรวจสอบว่าตำแหน่งเป้าหมาย (position) ถูกโจมตีโดยหมากตัวอื่นหรือไม่
    """
    x, y = position
    for (px, py), piece in pieces.items():
        moves = {
            'P': [(1, -1), (1, 1)],
            'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],
            'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
            'Q': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],
        }.get(piece, [])

        for dx, dy in moves:
            nx, ny = px, py
            while 0 <= nx < 4 and 0 <= ny < 4:
                nx += dx
                ny += dy
                if not (0 <= nx < 4 and 0 <= ny < 4):
                    break
                if (nx, ny) == (x, y):
                    return True
                if rows[nx][ny] != '.':  # หมากตัวอื่นขวาง
                    break
    return False


# ตัวอย่างการทดสอบ
if __name__ == "__main__":
    board = """\
..K.
PP..
..P.
....
"""
    # ตรวจสอบสถานะของ King
    is_check = checkmate(board)  
    if not is_check:
        # แนะนำการเดินหากไม่ถูกคุกคาม
        suggest_best_move(board)
