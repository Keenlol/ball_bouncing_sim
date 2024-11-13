import turtle

class Ball:

    def __init__(self, color, size, x, y, vx, vy) -> None:
        self.__color = color
        self.__size = size
        self.__x = x
        self.__y = y
        self.__vx = vx
        self.__vy = vy

    def draw_ball(self):
        """ Draw a circle of radius equals to size at x, y coordinates and paint it with color"""
        turtle.penup()
        turtle.color(self.__color)
        turtle.fillcolor(self.__color)
        turtle.goto(self.__x,self.__y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.__size)
        turtle.end_fill()

    def move_ball(self, dt):
        """ Update the x, y coordinates accordding to the vx and vy vector components"""
        self.__x += self.__vx*dt
        self.__y += self.__vy*dt


    def update_ball_velocity(self, canvas_width, canvas_height):
        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.__x) > (canvas_width - self.__size):
            self.__vx = -self.__vx

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.__y) > (canvas_height - self.__size):
            self.__vy = -self.__vy
