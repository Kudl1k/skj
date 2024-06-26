import time

def cached(func):
    """
    Create a decorator that caches up to 3 function results, based on the same parameter values.

    When `f` is called with the same parameter values that are already in the cache, return the
    stored result associated with these parameter values. You can assume that `f` receives only
    positional arguments (you can ignore keyword arguments).

    When `f` is called with new parameter values, forget the oldest accessed result in the cache
    if the cache is already full.

    Example:
        @cached
        def fn(a, b):
            return a + b # imagine an expensive computation

        fn(1, 2) == 3 # computed
        fn(1, 2) == 3 # returned from cache, `a + b` is not executed
        fn(3, 4) == 7 # computed
        fn(3, 5) == 8 # computed
        fn(3, 6) == 9 # computed, (1, 2) was now forgotten
        fn(1, 2) == 3 # computed again, (3, 4) was now forgotten
    """
    cache_order = []
    cache = {}
    def fn(*args):
        if args in cache:
            cache_order.remove(args)
            cache_order.append(args)
            return cache[args]     
        else:
            if len(cache_order) >= 3:
                last_item = cache_order.pop(0)
                del cache[last_item]
            value = func(*args)
            cache[*args] = value
            cache_order.append(args)
            return value
    return fn

class GameOfLife:
    """
    Implement "Game of life" (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

    The game board will be represented with nested tuples, where '.'
    marks a dead cell and 'x' marks a live cell. Cells that are out of bounds of the board are
    assumed to be dead.

    Try some patterns from wikipedia + the provided tests to test the functionality.

    The GameOfLife objects should be immutable, i.e. the move method will return a new instance
    of GameOfLife.

    Example:
        game = GameOfLife((
            ('.', '.', '.'),
            ('.', 'x', '.'),
            ('.', 'x', '.'),
            ('.', 'x', '.'),
            ('.', '.', '.')
        ))
        game.alive()    # 3
        game.dead()     # 12
        x = game.move() # 'game' doesn't change
        # x.board:
        (
            ('.', '.', '.'),
            ('.', '.', '.'),
            ('x', 'x', 'x'),
            ('.', '.', '.'),
            ('.', '.', '.')
        )

        str(x)
        ...\n
        ...\n
        xxx\n
        ...\n
        ...\n
    """

    def __init__(self, board):
        """
        Create a constructor that receives the game board and stores it in an attribute called
        'board'.
        """
        self.board = board
        pass

    def move(self):
        """
        Simulate one iteration of the game and return a new instance of GameOfLife containing
        the new board state.
        """
        newboard = []
        for i in range(len(self.board)):
            row = []
            for j in range(len(self.board[i])):
                number_of_neighbors = self.check_neighbors(i,j)
                if self.board[i][j] == 'x':
                    if number_of_neighbors == 2 or number_of_neighbors == 3:
                        row.append('x')
                    else:
                        row.append('.')
                else:
                    if number_of_neighbors == 3:
                        row.append('x')
                    else:
                        row.append('.')
            newboard.append(tuple(row))
        return GameOfLife(tuple(newboard))
        

    def check_neighbors(self,y, x):
        counter = 0
        row_min = max(0, y - 1)
        row_max = min(y + 2, len(self.board))
        col_min = max(0, x - 1)
        col_max = min(x + 2, len(self.board[0]))
        for i in range(row_min, row_max):
            for j in range(col_min, col_max):
                if (i, j) != (y, x) and self.board[i][j] == 'x':
                    counter += 1
        return counter        


    def alive(self):
        """
        Return the number of cells that are alive.
        """
        counter = 0
        for i in self.board:
            for j in i:
                if j == 'x':
                    counter += 1
        return counter

    def dead(self):
        """
        Return the number of cells that are dead.
        """
        counter = 0
        for i in self.board:
            for j in i:
                if j == '.':
                    counter += 1
        return counter

    def __repr__(self):
        """
        Return a string that represents the state of the board in a single string (with newlines
        for each board row).
        """
        result = ""
        for i in self.board:
            for j in i:
                result += j
            result += '\n'
        return result


def play_game(game, n):
    """
    You can use this function to render the game for n iterations
    """
    for i in range(n):
        print(game)
        game = game.move()
        time.sleep(0.25)  # sleep to see the output


# this code will only be executed if you run `python tasks.py`
# it will not be executed when tasks.py is imported
if __name__ == "__main__":
    play_game(GameOfLife((
        ('.', '.', '.'),
        ('.', 'x', '.'),
        ('.', 'x', '.'),
        ('.', 'x', '.'),
        ('.', '.', '.'),
    )), 10)