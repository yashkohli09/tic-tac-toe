import turtle
import sys

SIZE = 600
turn = 0
XO = {0:'X', 1:'O'} 
matrix = [[None for r in range(3)] for c in range(3)]

game_over = False

SCREEN = turtle.Screen()
SCREEN.title('TIC-TAC-TOE')
SCREEN.bgcolor('black')
SCREEN.setup(SIZE, SIZE)
SCREEN.tracer(0)

pen = turtle.Turtle()
pen.color('white')
pen.width(10)
pen.up()

pen.goto(-SIZE/2, SIZE/6)
pen.down()
pen.forward(SIZE)
pen.up()
pen.goto(-SIZE/2, -SIZE/6)
pen.down()
pen.forward(SIZE)
pen.up()
pen.hideturtle()

pen.left(90)
pen.goto(-SIZE/6, -SIZE/2)
pen.down()
pen.forward(SIZE)
pen.up()
pen.goto(SIZE/6, -SIZE/2)
pen.down()
pen.forward(SIZE)
pen.up()
pen.right(90)
pen.hideturtle()

while not game_over:

    SCREEN.update()

    def winning_turn():
        for r in range(3):
            if (matrix[r][0] != None) and (matrix[r][1] != None) and (matrix[r][2] != None): 
                if (matrix[r][0] == matrix[r][1]) and (matrix[r][1] == matrix[r][2]):
                    SCREEN.bye()
        for c in range(3):
            if (matrix[0][c] != None) and (matrix[1][c] != None) and (matrix[2][c] != None):
                if (matrix[0][c] == matrix[1][c]) and (matrix[1][c] == matrix[2][c]):
                    SCREEN.bye()
        if (matrix[0][0] != None) and (matrix[1][1] != None) and (matrix[2][2] != None):
            if (matrix[0][0] == matrix[1][1]) and (matrix[1][1] == matrix[2][2]):
                SCREEN.bye()
        if (matrix[0][2] != None) and (matrix[1][1] != None) and (matrix[2][0] != None):
            if (matrix[0][2] == matrix[1][1]) and (matrix[1][1] == matrix[2][0]):
                SCREEN.bye()
    
    def draw_cross(x,y):
        pen.goto(x + SIZE/30, y + SIZE/30)
        pen.down()
        pen.goto(x + SIZE*0.3, y + SIZE*0.3)
        pen.up()
        pen.goto(x + SIZE/30, y + SIZE*0.3)
        pen.down()
        pen.goto(x + SIZE*0.3, y + SIZE/30)
        pen.up()
        winning_turn()

    def draw_circle(x,y):
        pen.goto(x + SIZE/6, y + SIZE/30)
        pen.down()
        pen.circle(SIZE/6 - SIZE/30)
        pen.up()
        winning_turn()

    def draw(x,y):
        
        global turn
        if ((x >= -SIZE/2) and (x <= -SIZE/6)):
            if ((y <= SIZE/2) and (y >= SIZE/6)):
                if (matrix[0][0] == None):
                    matrix[0][0] = XO[turn]
                    draw_cross(-SIZE/2, SIZE/6) if(XO[turn] == 'X') else draw_circle(-SIZE/2, SIZE/6)
            elif ((y <= SIZE/6) and (y >= -SIZE/6)):
                if (matrix[0][1] == None):
                    matrix[0][1] = XO[turn]
                    draw_cross(-SIZE/2, -SIZE/6) if(XO[turn] == 'X') else draw_circle(-SIZE/2, -SIZE/6)
            if ((y <= -SIZE/6) and (y >= -SIZE/2)):
                if (matrix[0][2] == None):
                    matrix[0][2] = XO[turn]
                    draw_cross(-SIZE/2, -SIZE/2) if(XO[turn] == 'X') else draw_circle(-SIZE/2, -SIZE/2)
        elif ((x >= -SIZE/6) and (x <= SIZE/6)):
            if ((y <= SIZE/2) and (y >= SIZE/6)):
                if (matrix[1][0] == None):
                    matrix[1][0] = XO[turn]
                    draw_cross(-SIZE/6, SIZE/6) if(XO[turn] == 'X') else draw_circle(-SIZE/6, SIZE/6)
            elif ((y <= SIZE/6) and (y >= -SIZE/6)):
                if (matrix[1][1] == None):
                    matrix[1][1] = XO[turn]
                    draw_cross(-SIZE/6, -SIZE/6) if(XO[turn] == 'X') else draw_circle(-SIZE/6, -SIZE/6)
            if ((y <= -SIZE/6) and (y >= -SIZE/2)):
                if (matrix[1][2] == None):
                    matrix[1][2] = XO[turn]
                    draw_cross(-SIZE/6, -SIZE/2) if(XO[turn] == 'X') else draw_circle(-SIZE/6, -SIZE/2)
        elif ((x >= SIZE/6) and (x <= SIZE/2)):
            if ((y <= SIZE/2) and (y >= SIZE/6)):
                if (matrix[2][0] == None):
                    matrix[2][0] = XO[turn]
                    draw_cross(SIZE/6, SIZE/6) if(XO[turn] == 'X') else draw_circle(SIZE/6, SIZE/6)
            elif ((y <= SIZE/6) and (y >= -SIZE/6)):
                if (matrix[2][1] == None):
                    matrix[2][1] = XO[turn]
                    draw_cross(SIZE/6, -SIZE/6) if(XO[turn] == 'X') else draw_circle(SIZE/6, -SIZE/6)
            if ((y <= -SIZE/6) and (y >= -SIZE/2)):
                if (matrix[2][2] == None):
                    matrix[2][2] = XO[turn]
                    draw_cross(SIZE/6, -SIZE/2) if(XO[turn] == 'X') else draw_circle(SIZE/6, -SIZE/2)
    
        turn += 1
        turn %= 2

    SCREEN.onscreenclick(draw)
    SCREEN.mainloop()
