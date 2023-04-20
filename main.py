import tkinter as tk


class MyGame:
    def __init__(self):
        self.game_board = [1, 1, 2, 1, 1,]
        self.user_score = 0
        self.comp_score = 0
        self.first_move=0  # not made
        self.start()

    # define min-max algorithm to determine computer move
    def min_max_algorithm(self,board, is_maximizing, user_score, comp_score):
        if len(board) == 0:
            return user_score, comp_score
        if is_maximizing:
            best_score = -1000 
            for i in range(len(board)):
                new_board = board[:i] + board[i+1:]
                score, _ = self.min_max_algorithm(new_board, False, user_score, comp_score + board[i])
                if score > best_score:
                    best_score = score
                    best_move = board[i]
            return best_score, best_move
        else:
            best_score = 1000
            for i in range(len(board)):
                new_board = board[:i] + board[i+1:]
                score, _ = self.min_max_algorithm(new_board, True, user_score + board[i], comp_score)
                if score < best_score:
                    best_score = score
                    best_move = board[i]
            return best_score, best_move

    # define functions to handle user moves
    def take_one(self):
        if self.first_move==0:
            self.first_move=1
        if self.first_move==1:
            self.comp_start.destroy()
        self.game_board = self.game_board[1:]
        self.user_score += 1
        self.board_label.config(text=" ".join(str(i) for i in self.game_board))
        self.user_score_label.config(text=f"Your Score: {self.user_score}")
        self.comp_score_label.config(text=f"Computer Score: {self.comp_score}")
        
        if len(self.game_board) == 0:
           self.end_game()

        self.make_computer_play()

        if 1 not in self.game_board:
            self.take_one_button.config(state=tk.DISABLED)


    def divide(self):
        if self.first_move==0:
            self.first_move=1
        if self.first_move==1:
            self.comp_start.destroy()
        if 2 not in self.game_board:
            return 
        self.game_board.extend([1, 1])
        self.game_board=list(filter (lambda a: a != 2, self.game_board))
        
        self.board_label.config(text=" ".join(str(i) for i in self.game_board))
        self.take_one_button.config(state=tk.NORMAL)
        self.divide_button.config(state=tk.DISABLED)

        self.make_computer_play()

    # define function to handle end of game
    def end_game(self):
        if self.user_score > self.comp_score:
            text_outpout = "You win!"
        elif self.user_score < self.comp_score:
            text_outpout = "Computer wins!"
        else:
            text_outpout = "Draw!"
        self.winner_label.config(text=text_outpout)
        self.take_one_button.config(state=tk.DISABLED)
        self.divide_button.config(state=tk.DISABLED)
    
    def make_computer_play(self):
        
        
        self.comp_move = self.min_max_algorithm(self.game_board, True, self.user_score,self. comp_score)[1]
        self.game_board.remove(self.comp_move)
        if self.comp_move==1:
            self.comp_score += self.comp_move
        if self.comp_move==2:
            self.game_board.extend([1,1])
            self.divide_button.config(state=tk.DISABLED)

        self.board_label.config(text=" ".join(str(i) for i in self.game_board))
        self.comp_score_label.config(text=f"Computer Score: {self.comp_score}")
        if len(self.game_board) == 0:
            self.end_game()

    # create Tkinter window
    def computer_start(self):
        self.make_computer_play()
        self.comp_start.destroy()

    def restart(self):
        self.root.destroy()
        MyGame()

    def start(self):
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title("Min-Max Game")

        # create labels for game board and scores
        self.board_label = tk.Label(self.root, text=" ".join(str(i) for i in self.game_board))
        self.board_label.pack()
        self.user_score_label = tk.Label(self.root, text=f"Your Score: {self.user_score}")
        self.user_score_label.pack()
        self.comp_score_label = tk.Label(self.root, text=f"Computer Score: {self.comp_score}")
        self.comp_score_label.pack()
        self.winner_label = tk.Label(self.root)
        self.winner_label.pack()

        # create buttons for user moves
        self.take_one_button = tk.Button(self.root, text="Take One", command=self.take_one)
        self.take_one_button.pack(side=tk.LEFT)
        self.divide_button = tk.Button(self.root, text="Divide", command=self.divide)
        self.divide_button.pack(side=tk.LEFT)

        self.comp_start = tk.Button(self.root, text="Computer Starts", command=self.computer_start)
        self.comp_start.pack(side=tk.LEFT)
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart)
        self.restart_button.pack(side=tk.LEFT)

        # allow computer to make first move
            
        self.root.mainloop()

my_game=MyGame()