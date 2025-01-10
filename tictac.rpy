#label tictactoe:
#    python: 
#                import math
#        import random
#        class player:
#            def __init__(self,letter):
#                self.letter= letter   
#                #Here player will either select a x or o for playing
#            def get_move(self,game):
#                pass
#        
#        class Computer_Player(player):
#            def __init__(self,letter):
#                super().__init__(letter)
#               
#            def get_move(self,game):
#                square = random.choice(game.available_moves())
#                return square
#        
#        
#        class Human_player(player):
#            def __init__(self,letter):
#                super().__init__(letter)   
#                
#            def get_move(self,game):
#                valid_square=False
#                val=None
#                while not valid_square:
#                    square= input(self.letter +"/'s turn.Input(0-9):")
#                    try:
#                        val=int(square)
#                        if val not in game.available_moves():
#                            raise ValueError
#                        valid_aquare= True    
#                    except ValueError:
#                        print("Enter a valid value, try Again!! ")    
#                return val
#        
#        
#        
#        
#        # from Tictactoe import Human_player,Computer_Player
#        import time
#        import pygame
#        from pygame.locals import *
#        
#        
#        # Create the constants (go ahead and experiment with different values)
#        BOARDWIDTH = 3  # number of columns in the board
#        BOARDHEIGHT = 3 # number of rows in the board
#        TILESIZE = 100
#        WINDOWWIDTH = 480
#        WINDOWHEIGHT = 480
#        FPS = 30
#        BLANK = None
#        
#        #                 R    G    B
#        BLACK =         (  0,   0,   0)
#        WHITE =         (255, 255, 255)
#        BRIGHTBLUE =    (  0,  50, 255)
#        DARKTURQUOISE = (  3,  54,  73)
#        GREEN =         (  0, 204,   0)
#        
#        BGCOLOR = DARKTURQUOISE
#        TILECOLOR = GREEN
#        TEXTCOLOR = WHITE
#        BORDERCOLOR = BRIGHTBLUE
#        BASICFONTSIZE = 20
#        
#        BUTTONCOLOR = WHITE
#        BUTTONTEXTCOLOR = BLACK
#        MESSAGECOLOR = WHITE
#        
#        BLANK = 10
#        PLAYER_O = 11
#        PLAYER_X = 21
#        
#        
#        PLAYER_O_WIN = PLAYER_O * 3
#        PLAYER_X_WIN = PLAYER_X * 3
#        
#        CONT_GAME         = 10
#        DRAW_GAME         = 20
#        QUIT_GAME         = 30
#        
#        XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
#        YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)
#        
#        choice = 0
#        
#        
#        class TicTacToe:
#            def __init__(self):
#                self.board= ['' for _ in range(9)] 
#                #Creating a board 
#                self.current_winner= None
#        
#            def print_board(self):
#                for row in [self.board[i*3:(i+1)*3]for i in range(3)]:
#                    print('|'+'|' .join(row) + '|' )
#                    
#            @staticmethod
#            def print_board_nums():
#                numberboard =[[str(i)for i in range((j*3),(j+1)*3)]for j in range(3)]
#                for row in  numberboard:
#                    print('|'+'|' .join(row) + '|' )
#        
#            def available_moves(self):
#                #return[]        
#                moves=[]
#                for(i,spot) in enumerate(self.board):
#                    if spot == '':
#                        moves.append(i)
#                return moves
#        
#        
#            def empty_squares(self):
#                return ' ' in self.board
#        
#            def num_empty_squares(self):
#                return self.board.count(' ')  
#        
#            def winner(self,square,letter):
#                row_ind = square// 3
#                row=self.board[row_ind*3: (row_ind+1)*3]
#                if all([spot == letter  for spot in row]):
#                    return True
#                column_ind= square%3
#                column =[self.board[column_ind+i*3]for i in range(3)]
#                if all([spot == letter  for spot in row]):
#                    return True
#                if square%2==0:
#                    diagona1= [self.board[i]for i in [0,4,8]]  
#                    if all([spot == letter  for spot in row]):
#                        return True 
#                    diagona2= [self.board[i]for i in [0,2,6]]
#                    if all([spot == letter  for spot in row]):
#                        return True
#                return False
#        
#        
#        
#            def make_move(self,square,letter):
#                if self.board[square]== ' ':
#                    self.board[square]= letter
#                    if self.winner(square,letter):
#                    self.current_winner = letter
#        
#                    return True
#                return False   
#        
#        
#        
#        
#        
#        def play(game, o_player, x_player,print_game=True):
#            if print_game:
#                game.print_board_nums()
#        
#        
#            letter= 'X' 
#            while game.empty_squares():
#                if letter == 'O':
#                    square= o_player.get_move(game)
#                else: 
#                    square=x_player.get_move(game)
#        
#                if game.make_move(square,letter):
#                    if print_game:
#                        print(letter + f'makes a move to {square}')
#                        game.printboard()
#                        print('')
#                    if game.current_winner:
#                        if print_game():
#                            print(letter + 'Wins!!!!!!')
#                        return letter
#                    letter = 'O' if  letter== 'X' else 'X'  
#                time.sleep(0.8)     
#        
#        # if print_game:
#        #     print('It\'s a tie!')
#        
#        if __name__ == '__main__':
#            x_player=Human_player('X')
#            o_player=Computer_Player('O')
#            t= TicTacToe()
#            play(t,x_player,o_player,print_game=True) 
#        
#           