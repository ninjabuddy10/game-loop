from tkinter import *

window = Tk()
window.title("Main menu")
window.geometry("700x500+370+75")

def move_up(event):
    for i in range(len(map)):
        canvas.move(map[i],0,20)
      
def move_down(event):
    for i in range(len(map)):
        canvas.move(map[i],0,-20)
      
def move_left(event):
    for i in range(len(map)):
        canvas.move(map[i],20,0)
      
def move_right(event):
    for i in range(len(map)):
        canvas.move(map[i],-20,0)

def start():
    global canvas
    play.destroy()
    canvas = Canvas(window,width=700,height=500,bg='light blue')
    create_map()

def create_map():
    map = []
    canvas.pack()
    bush = PhotoImage(file='index\python\project\img\Tiny Adventure Pack\Other\Misc\Bush.png')
    print(bush)
    grass = PhotoImage(file='index\python\project\img\Tiny Adventure Pack\Other\Misc\Grass.png')
    print(grass)
    map_x = 5
    map_y = 5
    draw = [bush,bush,bush,bush,bush ,bush,grass,grass,grass,bush ,bush,grass,grass,grass,bush ,bush,grass,grass,grass,bush ,bush,bush,bush,bush,bush]
    x_coord = 0
    y_coord = 0
    z = 0
    # draws the map
    for i in range(map_y):
        for y in range(map_x):
            map.append(canvas.create_image(x_coord,y_coord,image=draw[z],anchor="nw"))
            z += 1
            i = i
            y = y
            x_coord += 32
        x_coord = 0
        y_coord += 32
    game_loop()

def game_loop():
    player = PhotoImage(file='index\python\project\img\Tiny Adventure Pack\Character\Char_one\Attack\Char_atk_down.png')
    player = canvas.create_image(450,250,image=player,anchor='nw')

    window.bind("<w>",move_up)
    window.bind("<s>",move_down)
    window.bind("<a>",move_left)
    window.bind("<d>",move_right)



play = Button(activebackground='grey',text='play',command=start)
play.pack()
window.mainloop()