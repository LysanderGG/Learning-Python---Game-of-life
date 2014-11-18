# Conway's Game of Life in Python 2.7.X for learning purpose
# Guillaume George

# #####################################

from time import sleep

# #####################################

def printLife(_board, _width, _height):
    for y in xrange(_height):
        for x in xrange(_width):
            v = _board[x][y]
            if( v == 0 ):
                print ' ',
            else:
                print 0,
        print 

def init(_board, _width, _height):
    for y in xrange(_height):
        for x in xrange(_width):
            _board[x][y] = 0;
    # TODO: other initialization - this is used just for test.
    _board[1][2] = 1;
    _board[2][3] = 1;
    _board[2][4] = 1;
    _board[3][2] = 1;
    _board[3][3] = 1;
    

def getNbNeighbours(_board, _width, _height, _x, _y):
    if( _x < 0 or _x >= _width or _y < 0 or _y >= _height ):
        return 0
        
    n = 0
        
    if( _y > 1 ):
        if( _x > 1        and _board[_x-1][_y-1] == 1 ): n += 1
        if(                   _board[_x  ][_y-1] == 1 ): n += 1
        if( _x < _width-1 and _board[_x+1][_y-1] == 1 ): n += 1
    
    if( _x > 1        and _board[_x-1][_y] == 1 ): n += 1
    if( _x < _width-1 and _board[_x+1][_y] == 1 ): n += 1
    
    if( _y < _height-1 ):
        if( _x > 1        and _board[_x-1][_y+1] == 1 ): n += 1
        if(                   _board[_x  ][_y+1] == 1 ): n += 1
        if( _x < _width-1 and _board[_x+1][_y+1] == 1 ): n += 1
    
    return n
    
def computeNextGeneration(_board_src, _board_dst, _width, _height):
    for x in xrange(_width):
        for y in xrange(_height):
            nb_neighbours = getNbNeighbours(_board_src, _width, _height, x, y)
            if( _board_src[x][y] == 0 ):
                if( nb_neighbours == 3 ):
                    _board_dst[x][y] = 1
                else:
                    _board_dst[x][y] = 0
            else: 
                if( nb_neighbours == 2 or nb_neighbours == 3 ):
                    _board_dst[x][y] = 1
                else:
                    _board_dst[x][y] = 0

# #####################################
# Init 
board_width  = 20
board_height = 20
generation = 0

boards = [[[0 for x in xrange(board_width)] for x in xrange(board_height)] for x in range(2)]

init(boards[0], board_width, board_height)
i_board = 0
i_next_board = 1

# Life
while 1 :
    print '----- Generation {} -----'.format(generation)
    printLife(boards[i_board], board_width, board_height)
    computeNextGeneration(boards[i_board], boards[i_next_board], board_width, board_height)
    
    i_board, i_next_board = i_next_board, i_board
    generation += 1
    sleep(0.2)
