from tkinter import *
from random import randint
#
cell_size = 20 #pixels
ms = 50 # rows and columns = maze size
visited_cells = []
walls = []


map = [['w' for _ in range(ms)]for _ in range(ms)]


def create():
    for row in range(ms):
        for col in range(ms):
            if map[row][col] == 'P':
                color = 'White'
            elif map[row][col] == 'w':
                color = 'black'
            draw(row, col, color)

def draw(row, col, color):
    x1 = col*cell_size
    y1 = row*cell_size
    x2 = x1+cell_size
    y2 = y1+cell_size
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)


#ccr = current cell row 
#ccc = current cell column
def check_neighbours(ccr, ccc):
    neighbours = [[ccr, ccc-1, ccr-1, ccc-2, ccr, ccc-2, ccr+1, ccc-2, ccr-1, ccc-1, ccr+1, ccc-1], #left
                [ccr, ccc+1, ccr-1, ccc+2, ccr, ccc+2, ccr+1, ccc+2, ccr-1, ccc+1, ccr+1, ccc+1], #right
                [ccr-1, ccc, ccr-2, ccc-1, ccr-2, ccc, ccr-2, ccc+1, ccr-1, ccc-1, ccr-1, ccc+1], #top
                [ccr+1, ccc, ccr+2, ccc-1, ccr+2, ccc, ccr+2, ccc+1, ccr+1, ccc-1, ccr+1, ccc+1]] #bottom
    visitable_neighbours = []           
    for i in neighbours:                                                                        #find neighbours to visit
        if i[0] > 0 and i[0] < (ms-1) and i[1] > 0 and i[1] < (ms-1):
            if map[i[2]][i[3]] == 'P' or map[i[4]][i[5]] == 'P' or map[i[6]][i[7]] == 'P' or map[i[8]][i[9]] == 'P' or map[i[10]][i[11]] == 'P':
                walls.append(i[0:2])                                                                                               
            else:
                visitable_neighbours.append(i[0:2])
    return visitable_neighbours

#StartingPoint

#scr = starting_cell row
#scc = starting_cell column

scr = randint(1, ms)
scc = randint(1, ms)
start_color = 'Green'
ccr, ccc = scr, scc

map[ccr][ccc] = 'P'
finished = False
while not finished:
    visitable_neighbours = check_neighbours(ccr, ccc)
    if len(visitable_neighbours) != 0:
        d = randint(0, len(visitable_neighbours) - 1) #this ensures only one neighbor from possible visitable neigbors becomes a path
        #ncr = new cell row
        #ncc = new cell column
        ncr, ncc = visitable_neighbours[d]
        map[ncr][ncc] = 'P'
        visited_cells.append([ncr, ncc])
        ccr, ccc = ncr, ncc
    if len(visitable_neighbours) == 0:
        try:
            ccr, ccc = visited_cells.pop()
        except:
            finished = True


window = Tk()
window.title('Maze')
canvas_side = ms*cell_size
canvas = Canvas(window, width = canvas_side, height = canvas_side, bg = 'grey')
canvas.pack()


create()
draw(scr, scc, start_color)
window.mainloop()
