def checkmate(board):
    # แปลงกระดานให้อยู่ในรูปแบบของรายการ (list) ที่ประกอบด้วยแต่ละแถว
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
                                return
                            if rows[x][y] != '.':  # มีหมากตัวอื่นขวางอยู่
                                break

    print("Fail")


# ตัวอย่างข้อมูลกระดาน 4x4
if __name__ == "__main__":
    board = """\
K...
....
....
....
"""
    checkmate(board)
