import turtle
from math import pi, dist
from vector import Vector

class Ball:

    def __init__(self, color, radius, x, y, vx, vy, e: float=1, on_col: int=0) -> None:
        self.__color = color
        self.__radius = radius
        self.__x = x
        self.__y = y
        self.__velocity = Vector(vx, vy)
        self.__mass = pi * radius**2
        self.__e = e
        self.__on_col = on_col

    def draw_ball(self):
        """ Draw a circle of radius equals to radius at x, y coordinates and paint it with color"""
        turtle.penup()
        turtle.color(self.__color)
        turtle.fillcolor(self.__color)
        turtle.goto(self.__x,self.__y - self.__radius)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.__radius)
        turtle.end_fill()

    def move_ball(self, dt):
        """ Update the x, y coordinates accordding to the vx and vy vector components"""
        self.__x += self.__velocity.x*dt
        self.__y += self.__velocity.y*dt


    def check_wall_collision(self, canvas_width, canvas_height):
        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.__x) > (canvas_width - self.__radius):
            self.__velocity.x = -self.__velocity.x

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.__y) > (canvas_height - self.__radius):
            self.__velocity.y = -self.__velocity.y

    def check_ball_collision(self, other):
        #Check for other balls
        if self.__on_col == 0 and dist(self.position, other.position) <= self.radius + other.radius:
            ms = self.mass
            mo = other.mass
            vs = self.velocity
            vo = other.velocity
            n = Vector(self.position[0], self.position[1]) - Vector(other.position[0], other.position[1])
            n = n / n.length

            vsni = vs.dot(n)
            voni = vo.dot(n)
            
            vsnf = (vsni * (ms + mo) + 2*mo*voni) / (ms + mo)
            self.__velocity = vs + (vsnf - vsni)*n
            self.__on_col = 1

        if self.__on_col == 1 and dist(self.position, other.position) > self.radius + other.radius:
            self.__on_col = 0
    
    @property
    def radius(self):
        return self.__radius
    
    @property
    def position(self):
        return [self.__x, self.__y]
    
    @property
    def mass(self):
        return self.__mass
    
    @property
    def velocity(self):
        return self.__velocity