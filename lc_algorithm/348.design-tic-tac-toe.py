"""
348. Design Tic-Tac-Toe Medium

1217

77

Add to List

Share Assume the following rules are for the tic-tac-toe game on an n x n board
between two players:

A move is guaranteed to be valid and is placed on an empty block. Once a winning
condition is reached, no more moves are allowed. A player who succeeds in
placing n of their marks in a horizontal, vertical, or diagonal row wins the
game. Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n. int move(int
row, int col, int player) Indicates that player with id player plays at the cell
(row, col) of the board. The move is guaranteed to be a valid move. Follow up:
Could you do better than O(n2) per move() operation?

Example 1:

Input
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output
[null, 0, 0, 0, 0, 0, 0, 1]

Explanation
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
 

Constraints:

2 <= n <= 100
player is 1 or 2.
0 <= row, col < n
(row, col) are unique for each different call to move.
At most n2 calls will be made to move.

"""


class TicTacToe:
    """
    Facts: In TTT, There are only two diagonal and n horizontal and vertical
    positions to check.

    During the play, we have to check if horizontal, vertical and diagonal (if
    happen to be on that diagonal). 

        0        1        2
    0   x(0,0)   x        x
    1   x        x(1,1)   x                => row == col for this diagonal
    2   x        x        x(2,2)

            0        1        2
    0   x        x        x(0,2)
    1   x        x(1,1)   x                => row = n - 1 - col
    2   x(2,0)   x        x

    There are two ways:

    1. define N x N board and mark players move and check if player wins 
       by checking if that horizontal, vertical or diagonal makes player win.
            (checkRow(row, player)) ||
            (checkColumn(col, player)) ||
            (row == col && checkDiagonal(player)) ||
            (col == n - row - 1 && checkAntiDiagonal(player)))

    2. Optimal: Instead of storing all the moves in board, just use two one
       dimensional array (for row and col) and two variables to store diagonal
       move sum.

       Use two move variables (1, -1) and increment array of row and col.

            0        1        2
        0   1        1        1
        1   x        x        x
        2   x        x        x

       [3, 0, 0]
       [1, 1, 1]


       diag = 0
       anti_diag = 0

       player 1 register 1 on  (0,0)  -> [1, 0, 0], [1, 0, 0]
       player 2 register -1 on (0,1) ->  [0, 0, 0], [1,-1, 0]
       player 1 register 1 on  (1,0)  -> [1, 1, 0], [2, 0, 0]
       player 1 register 1 on  (2,0)  -> [1, 1, 1], [3, 0, 0]  -> wins

       Using one dimension array, we can check if last marked position is size
       of n to decide if player wins.

        abs(self.horizontal[row]) == self.n or
        abs(self.vertical[col]) == self.n or
        abs(self.diagonal) == self.n or
        abs(self.anti_diagonal) == self.n

       abs -> player 2 has -1 so need sum would be -3.



    """

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        # one dimension array to store the player move
        self.horizontal = [0] * n
        self.vertical = [0] * n
        # diagonal and anti diagonal move tracker
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        # choose any 1 and -1 for player 1 and 2 resp.
        move = 1
        if player == 2:
            move = -1

        # mark the row and col of the two arrays (increment to indicate move)
        self.horizontal[row] += move
        self.vertical[col] += move

        # if row == col, increment left diagonal move
        if row == col:
            self.diagonal += move

        # if row + col == n - 1, increment right diagonal move
        if row+col == self.n-1:
            self.anti_diagonal += move

        # check if either horizontal, vertical, diag or anti diag was equal to
        # size n. if yes, return player. This works because player marks row
        # and col before checking it.
        if abs(self.horizontal[row]) == self.n or \
                abs(self.vertical[col]) == self.n or \
                abs(self.diagonal) == self.n or \
                abs(self.anti_diagonal) == self.n:
            return player

        # no one wins
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
