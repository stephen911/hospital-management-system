"""

~    15-112: Principles of Programming and Computer Science
~    Project: Chess Program
~    Name      : Muhammad Nahin Khan
~    AndrewID  : mnk1
~    File Created: 07/11/2016
~    Modification History:
~    Start             End
~    07/11 12:52       07/11 13:20
~    07/11 18:00       07/11 21:06
~    09/11 03:13       09/11 05:49
~    09/11 15:38       09/11 16:19
~    10/11 15:51       10/11 16:31
~    10/11 20:17       10/11 21:34
~    11/11 23:50       12/11 05:19
~    13/11 00:01       13/11 01:34
~    15/11 16:19       15/11 17:00
~    16/11 01:00       16/11 01:49
~    16/11 12:50       16/11 13:31
~    17/11 21:20       17/11 22:21
~    18/11 00:15       18/11 01:15
~    18/11 19:01       19/11 20:20
~    21/11 00:56       21/11 02:01
~    21/11 19:36       21/11 20:30
~    22/11 18:10       22/11 20:02
~    23/11 01:00       23/11 02:30
~    23/11 18:05       23/11 20:03
~    25/11 04:10       25/11 04:50
~    25/11 13:00       25/11 14:35
~    25/11 18:35       25/11 19:25
~    26/11 08:04       26/11 08:31
~    26/11 21:44       26/11 23:31
~    27/11 02:24       27/11 03:08
~

~Ensure that Pygame is installed

~GUI inspired by:
~https://en.lichess.org/

~Chess board image was taken from lichess website as well.
~The images for the pieces came from:
~https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Chess_Pieces_Sprite.svg/2000px-Chess_Pieces_Sprite.svg.png

~AI ideas from:
~https://chessprogramming.wikispaces.com/

~ An online lecture that helped me understand alpha-beta pruning:
~ Winston, P. [MIT OpenCourseWare]. (2010) 6. Search: Games, Minimax,
~ and Alpha-Beta. [Video File]. Retrieved from https://www.youtube.com/watch?v=STjW3eH0Cik

~Special thanks to professor Saquib for being so amazing.

~ This program is a chess game. The user may play against a friend or the
~ computer.
~
~ The game state is mainly stored as a 2D list of strings, and most of the
~ processing is thus done on a list of strings.
~
~ The GUI takes the current state and displays it on the screen. The GUI allows
~ drag and drop movement of pieces as well as click-click movement.
~
~ The AI that plays against the human evaluates all possible moves made by either
~ player up to a certain level of depth. The AI evaluates each position by giving
~ it a score. The higher the value of the score, the more favourable a position
~ is for white and the lower the value of the score, the more favourable the
~ position is for black. Knowing that white will try to get the score to be higher
~ and black will try and get the score to be lower, the AI assumes best play from
~ either side as it traverses up the search tree and chooses the best move to be
~ played. A problem that may arise is the number of postions that need to be
~ evaulated. Even at 3 levels of depth, thousands of positions have to be
~ evaluatd.
~ Several methods are used in this program to reduce positions that are searched:
~ 1. Alpha-beta pruning: As a result of  evaluating a position it can be found
~ that a portion of the search tree can be ignored as no further evaluations can




"""