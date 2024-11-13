import turtle
import ball
import random

class BouncingBallSimulator:

    def __init__(self, num_ball):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.__canvas_width = turtle.screensize()[0]
        self.__canvas_height = turtle.screensize()[1]
        print(self.__canvas_width, self.__canvas_height)
        turtle.colormode(255)
        self.__ball_list = []
        self.__num_ball = num_ball

        # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
    def __create_ball(self):
        for i in range(self.__num_ball):
            ball_radius = 0.05 * self.__canvas_width
            x = (random.randint(-1*self.__canvas_width + ball_radius, self.__canvas_width - ball_radius))
            y = (random.randint(-1*self.__canvas_height + ball_radius, self.__canvas_height - ball_radius))
            vx = (2*random.uniform(-1.0, 1.0))
            vy = (2*random.uniform(-1.0, 1.0))
            color = ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            self.__ball_list.append(ball.Ball(color, ball_radius, x, y, vx, vy))
        print(self.__ball_list)

    def __draw_border(self):
        turtle.penup()
        turtle.goto(-self.__canvas_width, -self.__canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*self.__canvas_width)
            turtle.left(90)
            turtle.forward(2*self.__canvas_height)
            turtle.left(90)

    def run(self, dt: int=1):
        self.__create_ball()
        while (True):
            turtle.clear()
            self.__draw_border()
            for ball in self.__ball_list:
                ball.draw_ball()
                ball.move_ball(dt)
                ball.update_ball_velocity(self.__canvas_width, self.__canvas_height)
            turtle.update()

num_ball = int(input("Input the number of balls:"))
s = BouncingBallSimulator(num_ball)
s.run(1)
# hold the window; close it by clicking the window close 'x' mark
turtle.done()
