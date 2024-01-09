import turtle as t

cellSize = 10
height = 500
width = 500
size = abs(height*width)

turtles = [t.Turtle() for x in range(1)]

print(t.window_height())
print(t.window_width())

def gridMaker(size,cellSize):

    numCells = size / cellSize
    

    numRows = 50
    squaresInRow = 50
    rowNumber = 0
    numSquaresRow = 0
    
    while rowNumber != numRows:

        for turtle in turtles:
            turtle.penup()
            turtle.pos = (width,height)
            turtle.degrees(fullcircle=360)
            turtle.speed(0)

            if numSquaresRow != squaresInRow:

                turtle.penup()
                turtle.goto(-width + cellSize * numSquaresRow, height - cellSize * rowNumber)
                turtle.setheading(0)
                turtle.pendown()
                turtle.forward(cellSize)
                turtle.setheading(270)
                turtle.forward(cellSize)
                turtle.setheading(180)
                turtle.forward(cellSize)
                turtle.setheading(90)
                turtle.forward(cellSize)        

                numSquaresRow += 1

            else:
                numSquaresRow = 0
                rowNumber += 1
    
    t.done()

gridMaker(size,cellSize)