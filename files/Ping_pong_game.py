# Ping pong game using python tkinter
# a prompt generated

import tkinter as tk
import random

class PingPongGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Ping Pong Game")
        self.canvas = tk.Canvas(master, width=600, height=400, bg="black")
        self.canvas.pack()
        self.ball = self.canvas.create_oval(290, 190, 310, 210, fill="white")
        self.paddle1 = self.canvas.create_rectangle(20, 150, 40, 250, fill="blue")
        self.paddle2 = self.canvas.create_rectangle(560, 150, 580, 250, fill="red")
        self.ball_dx = random.choice([3, -3])
        self.ball_dy = random.choice([3, -3])
        self.paddle_speed = 20
        self.score1 = 0
        self.score2 = 0
        self.score_label = tk.Label(master, text="Player 1: 0 - Player 2: 0", font=("Arial", 16))
        self.score_label.pack()
        

        self.master.bind("<w>", self.move_paddle1_up)
        self.master.bind("<s>", self.move_paddle1_down)
        self.master.bind("<Up>", self.move_paddle2_up)
        self.master.bind("<Down>", self.move_paddle2_down)
        
        self.update_game()
    
    def update_game(self):
        self.move_ball()
        self.check_collisions()
        self.check_score()
        self.master.after(10, self.update_game)
    
    def move_ball(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)

        ball_coords = self.canvas.coords(self.ball)
        if ball_coords[1] <= 0 or ball_coords[3] >= 400:  # Ball hits top/bottom
            self.ball_dy = -self.ball_dy
        
    def check_collisions(self):

        ball_coords = self.canvas.coords(self.ball)
        paddle1_coords = self.canvas.coords(self.paddle1)
        paddle2_coords = self.canvas.coords(self.paddle2)
        
        if ball_coords[0] <= paddle1_coords[2] and paddle1_coords[1] < ball_coords[3] < paddle1_coords[3]:
            self.ball_dx = -self.ball_dx
        

        if ball_coords[2] >= paddle2_coords[0] and paddle2_coords[1] < ball_coords[3] < paddle2_coords[3]:
            self.ball_dx = -self.ball_dx
    
    def check_score(self):
        # Get ball position
        ball_coords = self.canvas.coords(self.ball)
        
        if ball_coords[0] <= 0:
            self.score2 += 1
            self.update_score()
            self.reset_ball()
        elif ball_coords[2] >= 600:
            self.score1 += 1
            self.update_score()
            self.reset_ball()
    
    def update_score(self):
        self.score_label.config(text=f"Player 1: {self.score1} - Player 2: {self.score2}")
    
    def reset_ball(self):
        # Reset ball position
        self.canvas.coords(self.ball, 290, 190, 310, 210)
        self.ball_dx = random.choice([3, -3])
        self.ball_dy = random.choice([3, -3])
    
    def move_paddle1_up(self, event):
        self.canvas.move(self.paddle1, 0, -self.paddle_speed)
    
    def move_paddle1_down(self, event):
        self.canvas.move(self.paddle1, 0, self.paddle_speed)
    
    def move_paddle2_up(self, event):
        self.canvas.move(self.paddle2, 0, -self.paddle_speed)
    
    def move_paddle2_down(self, event):
        self.canvas.move(self.paddle2, 0, self.paddle_speed)

root = tk.Tk()
game = PingPongGame(root)
root.mainloop()


