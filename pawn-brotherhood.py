def safe_pawns(pawns):
    count = 0
    temp_tuple = ()
    for pawn in pawns:
        temp_tuple = chr(ord(pawn[0])+1)+str(int(pawn[1])-1), chr(ord(pawn[0])-1)+str(int(pawn[1])-1)
        if (temp_tuple[0] in pawns) or (temp_tuple[1] in pawns):
            count += 1
    return count