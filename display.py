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
~ guarantee better results. This can happen because white and black area against
~ one another. White plays what is best for it and black plays what is best for it,
~ so it would make sense for white to ignore any portion of the tree where black
~ has a clear upperhand that it can choose to play.
~ 2. Transposition table: Often, two different pathways in a search tree can result
~ in the same board being evaluated. Instead of evaluating the same board several
~ times, the program stores a table of values in a dictionary where the keys are
~ the positions. This way, repeated positions can have their evaluations looked up
~ fairly quickly, as the board state is hashed.
~ 3. Opening Book - The opening book is again a dictionary that stores board
~ positions often seen in the beginning few moves in chess. Appropraite moves that
~ can be played at such positions is stored in the dictionary. A random move is
~ selected and played from the list of suggested moves wihtout searching if the AI
~ finds itself confronting a such a board postion. Note that this opening book was
~ recorded by myself and so it does not have many positions stored in it.
~
~ In order to traverse the search tree as above, the AI needs to know how to evaluate the
~ board at any position to decide if white or black has the advantage. My evaluation
~ function currently looks at three main things when evaluating the board:
~    a) Material for white and black. Each piece has a value and the more pieces you have,
~        the better off your position is likely to be. For example, if white has an extra
~        queen, it has an advantage over black.
~    b) Piece-square table values - for each piece, there is a table that stores the best
~        squares that the particular piece should occupy. So if white has a knight at a
~        good square that controls the centre of the board, whereas black has a knight
~        at the corner of the board, the situation is evaluated as being more favourable
~        for white.
~    c) Reduction in points for doubled pawns, isolated pawns, and blocked pawns. If any
~        side has a set of pawns with the above features their points are slightly lower
~        to indicate a slight disadvantage in such a position.
~    d) A checkmate: a position where this has occured gets a very high point, so that the
~        AI moves towards this if it can. (or avoids it).
~
~ There are also several ways in which this program may be improved:
~ 1. Move ordering: Given a certain position and the AI needs to search a few layers
~ deep from it, somehow pre-sorting each move by ranking them in their likelihood of
~ being good moves allows for earlier cut-offs to be made by alpha-beta pruning.
~ 2. Iterative Deepening: Instead of going directly to a given depth when searching,
~ the A.I. may evaluate the best move at depth 1, then depth 2, then depth 3, etc.
~ until it reaches the final depth it needed to calculate at depth n. The reason for
~ this is that it may be mathematically shown that this does not dignificantly increase
~ computation and allows the A.I. to make its best move if it needs to abide by a
~ time limit.
~ 3. Better data structure - I believe the structure I have used to keep the state of
~ the board (list of a list) may be slowing down accessing its elements or assigning
~ its elements. Improvement in efficiency of my code by changing data structures may
~ potentially improve the speed at which my AI makes its move.
~ 4. Import of large opening tables: There are databases available online that store
~ the best moves played by grandmasters at various key opening positions of the chess
~ game. Although my AI does make use of an opening table that I recorded for it myself,
~ it is not able to respond to many opening positions using the table since the table
~ only convers few positions. If an opening table with millions of positions could be
~ imported to this program, the AI's moves would improve in the beginning. It would also
~ give it more variety in terms of the move it plays. Furthermore, using good openings
~ allows the AI to make the best moves in the field it is best at: middle game tactics.
~ 5. Better evaluation of positions - The current features evaluated by the evaluation
~ function when judging a positoin to give it a score allows for good opening games and
~ tactics that often allow it to gain advantage over the opponents that I have tested it
~ against. However, there are many aspects of playing good chess that it does not
~ consider: like having good mobility of your pieces (eg a trapped bishop should be bad
~ for the AI but it doesn't know that). Other aspects include king safety, pawn structure,
~ etc. It could also use different evaluation for each game phase. For example, a pawn is
~ not worth much at the opening phase of the game but in the endgame it is very important
~ and so should be evaulated as a valuable piece.
~ 6. Endgame tables - As good as my AI may be in middle games, given a queen and a king to
~ attempt checkmate against a lone king, it would be unlikely for it to succeed. This is
~ because such checkmates, despite being simple, require a large number of combination of
~ moves to occur, the depth of which my AI would not be able to see. So endgame table allows
~ it to know (for a very large number of endgame positions) the best move to play in order
~ to attempt a win or a draw (or try its best to avoid a loss).


~Note about coordinates:
~Normally, algebraic notation is used to specify a box on a chess board. In this
~program, coordinates will be index referecnes to the 2_D array that stores the
~state of the board. Thus, e4 in algebraic notation would be expressed as (4,4)
~in this program.

~Import dependencies:
import pygame ~Game library
from pygame.locals import * ~For useful variables
import copy ~Library used to make exact copies of lists.
import pickle ~Library used to store dictionaries in a text file and read them from text files.
import random ~Used for making random selections
from collections import defaultdict ~Used for giving dictionary values default data types.
from collections import Counter ~For counting elements in a list effieciently.
import threading ~To allow for AI to think simultaneously while the GUI is coloring the board.



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~Class Definitions:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~There are three classes used in this program:
~ 1. GamePosition - This class stores a chess position. A chess position constitutes several
~ features that specify the state of the game, such as the the player that has to play next,
~ castling rights of the players, number of irreversible moves played so far, the positions of
~ pieces on the board, etc.
~ 2. Shades - This is used for GUI. A shade is a transparent colored image that is displayed on
~ a specific square of the chess board, in order to show various things to the user such as
~ the squares to which a piece may move, the square that is currently selected, etc. The class
~ stores a reference to the image that the instance of the class should display when needed. It
~ also stores the coordinates at which the shade would be applied.
~ 3. Piece - This is also used for GUI. A Piece object stores the information about the image
~ that a piece should display (pawn, queen, etc.) and the coordinate at which it should be
~ displayed on thee chess board.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class GamePosition:
        def __init__(self,board,player,castling_rights,EnP_Target,HMC,history = {}):
                    self.board = board ~A 2D array containing information about piece postitions. Check main
                            ~function to see an example of such a representation.
                                    self.player = player ~Stores the side to move. If white to play, equals 0. If black to
                                            ~play, stores 1.
                                                    self.castling = castling_rights ~A list that contains castling rights for white and
                                                            ~black. Each castling right is a list that contains right to castle kingside and queenside.
                                                                    self.EnP = EnP_Target ~Stores the coordinates of a square that can be targeted by en passant capture.
                                                                            self.HMC = HMC ~Half move clock. Stores the number of irreversible moves made so far, in order to help
                                                                                    ~detect draw by 50 moves without any capture or pawn movement.
                                                                                            self.history = history ~A dictionary that stores as key a position (hashed) and the value of each of
                                                                                                    ~these keys represents the number of times each of these positions was repeated in order for this
                                                                                                            ~position to be reached.
                                                                                                                    
                                                                                                                        def getboard(self):
                                                                                                                                    return self.board
                                                                                                                                        def setboard(self,board):
                                                                                                                                                    self.board = board
                                                                                                                                                        def getplayer(self):
                                                                                                                                                                    return self.player
                                                                                                                                                                        def setplayer(self,player):
                                                                                                                                                                                    self.player = player
                                                                                                                                                                                        def getCastleRights(self):
                                                                                                                                                                                                    return self.castling
                                                                                                                                                                                                        def setCastleRights(self,castling_rights):
                                                                                                                                                                                                                    self.castling = castling_rights
                                                                                                                                                                                                                        def getEnP(self):
                                                                                                                                                                                                                                    return self.EnP
                                                                                                                                                                                                                                        def setEnP(self, EnP_Target):
                                                                                                                                                                                                                                                    self.EnP = EnP_Target
                                                                                                                                                                                                                                                        def getHMC(self):
                                                                                                                                                                                                                                                                    return self.HMC
                                                                                                                                                                                                                                                                        def setHMC(self,HMC):
                                                                                                                                                                                                                                                                                    self.HMC = HMC
                                                                                                                                                                                                                                                                                        def checkRepition(self):
                                                                                                                                                                                                                                                                                                    ~Returns True if any of of the values in the history dictionary is greater than 3.
                                                                                                                                                                                                                                                                                                            ~This would mean a position had been repeated at least thrice in order to reach the
                                                                                                                                                                                                                                                                                                                    ~current position in this game.
                                                                                                                                                                                                                                                                                                                            return any(value>=3 for value in self.history.itervalues())
                                                                                                                                                                                                                                                                                                                                def addtoHistory(self,position):
                                                                                                                                                                                                                                                                                                                                            ~Generate a unique key out of the current position:
                                                                                                                                                                                                                                                                                                                                                    key = pos2key(position)
                                                                                                                                                                                                                                                                                                                                                            ~Add it to the history dictionary.
                                                                                                                                                                                                                                                                                                                                                                    self.history[key] = self.history.get(key,0) + 1
                                                                                                                                                                                                                                                                                                                                                                        def gethistory(self):
                                                                                                                                                                                                                                                                                                                                                                                    return self.history
                                                                                                                                                                                                                                                                                                                                                                                        def clone(self):
                                                                                                                                                                                                                                                                                                                                                                                                    ~This method returns another instance of the current object with exactly the same
                                                                                                                                                                                                                                                                                                                                                                                                            ~parameters but independent of the current object.
                                                                                                                                                                                                                                                                                                                                                                                                                    clone = GamePosition(copy.deepcopy(self.board), ~Independent copy
                                                                                                                                                                                                                                                                                                                                                                                                                                                 self.player,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                              copy.deepcopy(self.castling), ~Independent copy
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           self.EnP,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        self.HMC)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                return clone
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                class Shades:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ~Self explanatory:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            def __init__(self,image,coord):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        self.image = image
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                self.pos = coord
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    def getInfo(self):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                return [self.image,self.pos]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ))



"""