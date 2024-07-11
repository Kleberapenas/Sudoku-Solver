#sudoku solve no tutorial
#this function will check for each row and collum from a given grid if the position is equal to a given number
def is_number_possible(grid,row,col,num):
    #check row
    for x in range(9):
        if grid[row][x] == num:
            return False
    #check col
    for y in range(9):
        if grid[col][y] == num:
            return False
    #Check if there are any other equal numbes in each 3x3 grid
    for x in range(3):
        for y in range(3):
            if grid[(row - row%3)+x][(col - col%3)+y]==num:
                return False
    return True
#this function will solve the sudoku
def Solver(grid,row,col):
    #checks if the grid is already over if not, goes up one row and restarts
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0
    #checks if there is already a value in the grid cel
    if grid[row][col]>0:
        return Solver(grid,row,col+1)
    #checks every number from 0 to 9 in every grid using the possible move function
    for num in range(1,10):
        #if the function returns positive it changes the cell value to that of the possible number
        if is_number_possible(grid,row,col,num):
            grid[row][col]=num
        #call the Solver function adding one to the collun, and if its the last row and the last collum then it returns true
        if Solver(grid,row,col+1):
            return True
        #tell the funcion from where to start from
        grid[row][col]=0
    return False
grid = [[0,0,2,3,5,0,9,8,0],
        [5,4,0,0,8,7,0,0,0],
        [0,0,0,0,0,0,0,0,7],
        [0,0,0,0,4,0,8,3,2],
        [0,9,6,1,2,8,7,0,0],
        [0,0,0,0,7,0,1,0,6],
        [0,0,0,6,0,0,3,0,0],
        [7,6,3,8,0,5,0,2,0],
        [9,2,8,7,0,4,5,6,0]]

#Allows user input to writte the sudoku grid
print("Writte the sudoku grid, row per row")
for i in range(9):
    line = list(input())
    for j in range(9):
        grid[i][j] = int(line[j])

#if the function retuns true, it follows
if Solver(grid,0,0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end = ' ')
        print()
else:
    print("no solution")