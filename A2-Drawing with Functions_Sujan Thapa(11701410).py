import turtle
import threading
import random
from random import randint

turtle.setup(750,800) #setup window screen 
turtle.hideturtle() #this line hides the head of the turtle
turtle.tracer(4,0) #this line has two arguments (n=none,speed), n is set for the animation time

#for title
def title(): #function for the title is defined
    title=turtle.Turtle() #this line where turtle.Turtle() is the constructor method of the class Turtle which returns an instance of the class
    title.penup() #penup method is used to move pen without tracing any line within the screen
    title.goto(-350,345) #goto method helps turtle to move in the desired x and y coordinates location
    title.hideturtle()
    title.write('Square Hunt', False, align='left', font=('Arial', 20, 'normal')) #write method/function is used to write the text in the screen


#for start button
def start_button(): #we define the function for the start button of our game, when we press start, game will run
    button = turtle.Turtle()
    button.hideturtle()
    button.penup()
    button.goto(0,345)
    button.pendown() #pendown is another method which is used to draw in the screen
    button.pensize(2) #this will help to desired size of pen to draw 
    button.color('black','sky blue') #color mfunction is used to draw turtle using different color
    button.begin_fill() #turtle first draw the line and within the shap it creates according to the coordinate axes, it will begin to fill the color
    button.forward(100) #forward with 100 pixels helps to move turtle 100 pixels in same direction
    button.left(90) #left(angle), here angle=90 degrees, turtle head turns 90 degree angle to the left
    button.forward(25)
    button.left(90)
    button.forward(100)
    button.left(90)
    button.forward(25)
    button.end_fill() #end_fill method is called to finalize the filling of color
    button.penup()
    button.goto(50,345)
    button.pendown()
    start = button.write('START', False, align='center', font=('Arial', 20, 'normal')) #text START is written in the desired location (50,345)
    
title() #after function  is defined, we need to call the function so that actual work will be starting, title function is called, here this function will print title in  the screen
start_button() #start_button function is called, it will print the start button with Text labelled as START in sky blue color
user_input_grid = turtle.textinput('Grid Size', 'Enter desired grid size 3 to 8') #turtle.textinput(), is the function that can be used in order to generate the prompt dialog box in order to get the input entered by the user
user_input_level = turtle.textinput('Level', 'Enter level 1,2,3')

N = int(user_input_grid)  # N is defined as a global variable which has scope towards local function, and int() is used because turtle.textinput itself is a string, and we need integer value to give the condition
L= int(user_input_level)    #L is defined as level variable and string is converted into integer

def square(t,start_x,start_y,grid_size): #this function has 4 paramters, t=constructor method for turtle.Turtle(), start_x= starting position of drawing square- x-coordinates, start_y=starting position for y coordinates and grid_size will be the final sqaure we will be drawing
    t.hideturtle()
    t.penup() # no drawing!
    t.pensize(3)
    t.pencolor('crimson')
    t.goto(start_x,start_y) # move the pen to a different position
    t.pendown() # resume drawing
        
        
    for i in range(4): #for loop set up to increment the value for i 
        grid_size_function() #grid_size_function is called, the grid_size_function evaluates the size of the grid by mathematical formula
        t.forward(grid_size) # move forward
        t.left(90) # turn pen left 90 degrees
start_x = -350 # starting x position of the grid
start_y = -375# starting y position of the grid
t = turtle.Turtle()
    
def grid_size_function(): #this is the function that is called in recent call history
    global grid_size
    if N >= 3 and N<=8:
        grid_size = 700/N# pixel size of each box in the grid

    else:
        print('user has input wrong grid size')
    
def grid(): #grid is the function which has the size of each grid or sqaure within the total number of grids present in the game, grid size is determined according to the grid_size_function
    grid_size_function() #grid_size_function is called to get the conditions and values from that function to be used in grid function calculation
    for i in range(N): # NxN grid, i is increment to N times
        for j in range(N): #j is increment N times
            square(t,start_x+j*grid_size, start_y+i*grid_size, grid_size) #main mathematical equation that will differentiated the x-cordinates and y-coordinates based on the grid_size_function
def game(): #game function is defined to set up the final look of the game, which calls title, start_button, our grid and score:
    grid_size_function()
    square(t,start_x,start_y,grid_size)
    grid()
    turtle.penup()
    turtle.setposition(350,345) #setposition helps to set the position to the location x and y coordinates
    turtle.write('Score: ', False, align='right', font=('Arial', 20, 'normal'))

interval=0 #variable interval is defined with the initial value to be zero, this variable cam be used to detrmine the interval in our threading

#for level of difficulty in game
if L==1: #condition set up, if for the levelof difficulty, L denotes the variable for user input level choice
    interval=2
elif L==2:
    interval=1.5
elif L==3:
    interval=1
else:
    invalid_level=turtle.textinput('Wrong Level','You have entered the wrong level, Please enter valid level from 1 to 3') #if user inputs the wrong level rather than L<=3, this message will be displayed in next window prompt and allowing user to input again as try again
    I_L=int(invalid_level)
    if I_L<=L: #if condition is true game function will be called so that user can enter again his/her desired level, else if again , they put invalid inoput, then user has input invalid level will be printed
        game()
    else:
        print('user has input invalid level')

game() #if above condition will be true, game function will be called

square_count=0
def random_square(): #this is the main function which generates the random sqaue within the grid in the display screen. Here, nested function is also defined to handle the click so that if we click in random_sqaure, score will be added or deducted.
    global square_count
    turtle.penup()
    turtle.goto(0,345)
    square_count=square_count+1 #after every successfull hit in the random_square, score_count increment its value by 1
    squarestring = "[%s]" %square_count #variable squarestring is defined where %s is used to call the value of the score_count
    turtle.write(squarestring, False, align='right', font=('Arial', 20, 'italic'))  #squarestring is printed on the screen

    rand_x=random.randint(0,N-1) #rand_x variable is defined which has values ranging from 0 to N-1, 0 to N-1 is used so that x coordinate always lie within the grid
    rand_y=random.randint(0,N-1) #rand_y variable is defined which has values ranging from 0 to N-1, 0 to N-1 is used so that y coordinate always lie within the grid
    
    a=start_x+rand_x*grid_size #a,b,c,d is defined in order to find the edge of the random sqaure
    b=start_y+rand_y*grid_size
    c=a+grid_size
    d=b+grid_size
       
    turtle.penup()
    turtle.goto(a,b)
    turtle.pendown()
    turtle.fillcolor('green')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(grid_size)
        turtle.left(90)   
    turtle.end_fill()
    
    def handle_random_square(x,y): #nested function is created so that the variable defined within random_sqaure function will have the scope to the handle_random_square function
        global score_count #global score_count variable is defined because score_count is not within the scope of handle function. Global variable is always defined within any function in an entire program
        if x>a and x<c and y>b and y<d: #condition set up for clicking location, these are the values from the edge which makes square so that we may always click inside the square
            print('Successful hit') #if we hit the random square, this will print
            turtle.onscreenclick(None) #this line prevents from clicking in the same square
            turtle.penup()
            turtle.setposition(355,345) #this line is the location set up for our score
            score_count=score_count+1 #after every successfull hit in the random_square, score_count increment its value by 1
            scorestring = "Score: %s" %score_count #variable scorestring is defined where %s is used to call the value of the score_count
            turtle.write(scorestring, False, align='right', font=('Arial', 20, 'normal'))  #scorestring is printed on the screen

            #this line is used to create a blue color square after every succesfull hit on the random square
            turtle.penup()
            turtle.goto(a,b)
            turtle.pendown()
            turtle.fillcolor('blue')
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(grid_size)
                turtle.left(90)   
            turtle.end_fill()
            
               
            
        else: #condtion if we miss the hit on the random_square
            turtle.onscreenclick(None) #this will prevent from hitting in the same spot multiple times
            print('Unsuccessful hit') #if we hit other than random_sqaure in the screen, this message will be printed
            if score_count==0: #this line validate if the score value is 0, if it is less than 0 after deduction by unsuccessful hit, it prevents not to get the negative values like -1, -2, -3
                score_count=0
            else:
                score_count=score_count-1 #this line deducts the score_count by 1 if we miss the hit by hitting on the screen rather than random_square
                
    turtle.onscreenclick(handle_random_square) #this is the mouse click handler, it will listen to the on screen click



num=0 #num=0 is defined for the thread that we will be creating in order to set up the timer of the loop
score_count=0 #score_count variable is defined here


def next_square(): #this is the function that wil call itself wihiin certain interval of time
    global num #global num is defined because threading function cannot deterimine either num is local or global variable
    
    if num<10: #this is the condition, that will allow the random sqaure to be printed for only 10 times     
        
        random_square() #random_square function is called to draw the random_square
        num=num+1 #num value increment by 1
        threading.Timer(interval,next_square).start() # this is the main thread which enables schedulingof the job. this function calls next_square function in an interval corresponding to the level that are chosen by the users
        threading.Timer(interval,turtle.clear).start() #this line clears a random_sqaure that is drawn from above function call
       
        
        
    else: #if condition i like num has greater value than 10, then thread will be canceled. This is actaully stopping the infinite loop of thread which is calling itself for n times
        
        threading.Timer(interval,next_square).cancel()
        turtle.setposition(0,345)
        turtle.write('Game Finished', False, align='center', font=('Arial', 20, 'normal')) #text START is written in the desired location (50,345)
        
       
        print('GAme over') #after successfull iteration of 10 repetition of next_square function, the game is finished
    
      

def handle_click(x,y): #this is the main function to handle the mouse click
    global score_count #score_count is set up to global in order to defined it in the functions in an entire program whether it is nested too.
    
    if x>0 and x<100 and y>345 and y<395: #this is the coordinates for the start button, this enables clicking boundary within the start_button only.
        turtle.clearscreen() #this will clear up the screen with erasing everything
        turtle.tracer(4,0)
        turtle.hideturtle()
        title()
        game()
        next_square() #after clicking the start function, our will started by calling next_sqaure function
        
          
        
turtle.listen() #this will listen the mouse clicks
turtle.onscreenclick(handle_click) #handle_click has coordinates x and y, it enables clicking on x and y coordinates

                 
                
turtle.done()

