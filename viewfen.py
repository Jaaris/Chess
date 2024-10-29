import sys

def main():
    # if len(sys.argv) != 2:
    #     print('Enter the correct number of arguments e.g. $ python viewfen.py "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"')
    #     sys.exit(1)
    states = (parsing_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq e3 0 1"))
    game_states(states)
    # print ('the states',states)
    

def parsing_board(fen):
    places, colour, castling_rights, en_passant, half_move, full_move = fen.split()

    # The board
    # "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    board = []
    for row in places.split('/'):
        # print(row)
        board_row = []
        for j in row:
            # print(j)
            if j.isdigit():
                board_row.extend(['#'] * int(j)) # should print hastag to see the empty space are there
                # print(board_row)
            else:
                board_row.append(j)
        board.append(board_row)
    # print('the board', board)
    
    # for row in board:
    #     print(' '.join(row))
        
    game_state = {
        'board'             : board,
        'active colour'     : colour,
        'castling rights'   : castling_rights,
        'en passant'        : en_passant,
        'halfmove_clock'    : half_move,
        'fullmove_clock'    : full_move,
    }
    
    return game_state

def game_states(game_state):
    print("The Chess Game: \n")
    current_board = game_state['board']
    for row in current_board:
        print(' '.join(row))
        
    print('\n')
    
    # if game_state['active colour'] == 'w':
    
    # #have to correct still
    # print(f"\n {'White' if game_state['active colour'] == 'w' else 'Black'} to move")
    # print(f"{True: 'White to move', False: 'Black to move'} [game_state['active colour'] == 'w']")
    
    # Castling right try to use Ternary Operator
    castling = game_state['castling rights']

    if 'K' in castling and 'Q' in castling:
        print("White can castle both sides")
    elif 'K' in castling:
        print("White can castle king side")
    elif 'Q' in castling:
        print("White can castle queen side")

    if 'k' in castling and 'q' in castling:
        print("Black can castle both sides")
    elif 'k' in castling:
        print("Black can castle king side")
    elif 'q' in castling:
        print("Black can castle queen side")

    if game_state['en passant'] == '-':
        print("No en passant square")
    else:
        print(f"En passant target square: {game_state['en passant']}")

    print(f"Halfmove clock: {game_state['halfmove_clock']}")
        
        
if __name__=="__main__":
    main()
