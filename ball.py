from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.delta_x = 10
        self.delta_y = 10
        self.direction = 1
        self.speed = 1

    def move(self):
        new_x = self.xcor()+self.delta_x*self.speed
        new_y = self.ycor()+self.delta_y*self.speed
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.delta_y *= -1

    def bounce_x(self):
        self.delta_x *= -1

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.speed = 1

    def speed_bump(self):
        """Increases ball speed"""
        self.speed *= 1.05

