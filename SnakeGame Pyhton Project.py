import tkinter
import random

rows = 25
coloms = 25
size = 25
endgame = False
Width = size*rows
Height = size*coloms
points = 0
#sound


class Tile:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
        
def start(lvl):   
    global endgame,points,snake,food,body,speedx,speedy
    points = 0
    snake = Tile(5*size,5*size)
    food = Tile(5*size,10*size)
    body = []
    speedx = 0
    speedy = 0
    gameloop()


    
def gameloop():
    global snake,body,points,endgame
    if endgame:
        return
    move()
    draw()
       
window = tkinter.Tk()
window.title("Snake")
window.resizable(False,False)

canvas = tkinter.Canvas(window,bg = "black",width = Width,height= Height,borderwidth=0,highlightthickness=0)
canvas.pack()
window.update()

width2= window.winfo_width()
height2=window.winfo_height()
screenw= window.winfo_screenwidth()
screenh=window.winfo_screenheight()

windowX=int(screenw/2)-(width2/2)
windowY=int(screenh/2)-(height2/2)

window.geometry(f"{width2}x{height2}+{int(windowX)}+{int(windowY)}")

snake=Tile(5*size,5*size)
food =Tile(10*size,10*size)
body = []

speedx = 0
speedy = 0

def newDir(e):
   # print(e.keysym)
   global speedx,speedy,endgame
   if (endgame):
       return 
       
   if (e.keysym == "Up" and speedy != 1):
       speedx = 0
       speedy = -1
   elif (e.keysym == "Down" and speedy != -1):
        speedx = 0
        speedy = 1
    
   elif (e.keysym == "Left" and speedx != 1):
        speedx = -1
        speedy = 0
        
   elif (e.keysym == "Right" and speedx != -1):
        speedx = 1
        speedy = 0
        
def move():
    global snake,body,endgame,points
    if (endgame):
        return
    
    if(snake.x<0 or snake.x>=Width or snake.y<0 or snake.y >=Height):
        endgame = True
        return
    
    for ob in body:
        if(snake.x == ob.x and snake.y == ob.y):
            endgame = True
            return
    
    if (snake.x == food.x and snake.y == food.y):
        body.append(Tile(food.x,food.y))
        food.x = random.randint(0,coloms-1)*size
        food.y = random.randint(0,rows-1)*size
        points += 1
        
    for i in range(len(body)-1,-1,-1):
        ob = body[i]
        if(i == 0):
            ob.x = snake.x
            ob.y = snake.y
        else:
            lst_tile = body[i-1]
            ob.x = lst_tile.x
            ob.y=lst_tile.y
    
    snake.x += speedx*size;
    snake.y += speedy*size;
    
    
    
    

def draw():
    global snake,body,points,endgame
    move()
    canvas.delete("all")
    canvas.create_rectangle(food.x,food.y,food.x+size,food.y+size,fill = "green")

    canvas.create_rectangle(snake.x,snake.y,snake.x+size,snake.y+size,fill = "pink")
    for ob in body:
        canvas.create_rectangle(ob.x,ob.y,ob.x+size,ob.y+size,fill = "yellow")
    
    
    if(endgame):
        canvas.create_text(Width/2,Height/2,font = "Arial 20", text = f"YOU ARE DIE :{points}",fill = "red")
    else:
        canvas.create_text(30,20,font ="Arial 10",text =  f"Ponts : {points}",fill = "white")   
    #window.after(100,draw)
    
    if not endgame:
        window.after(100,draw)
draw()  

window.bind("<KeyRelease>",newDir)

window.mainloop()
