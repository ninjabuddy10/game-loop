from tkinter import *
import time

window = Tk()
window.title("Main menu")
window.geometry("700x500+370+75")

frame = 0

def start():
    play.destroy()
    game_loop()
    


def game_loop():
    frame = 0
    def frame_update(frame_n):
        current_frame = frame_n
        canvas.itemconfigure(avatar,player[current_frame])
        print(avatar)
    def move_up(event):
        for i in range(len(Map)):
           canvas.move(Map[i],0,20)
        
    def move_down(event):
        for i in range(len(Map)):
            canvas.move(Map[i],0,-20)
        
    def move_left(event):
        for i in range(len(Map)):
            canvas.move(Map[i],20,0)
        
    def move_right(event):
        for i in range(len(Map)):
            canvas.move(Map[i],-20,0)

    window.bind("<w>",move_up)
    window.bind("<s>",move_down)
    window.bind("<a>",move_left)
    window.bind("<d>",move_right)
    while True:
        frame_update(frame)
        frame += 1
        time.sleep(0.01)
        window.update()

play = Button(activebackground='grey',text='play',command=start,)
play.pack()

canvas = Canvas(window,width=700,height=500,bg='light blue')
Map = []
canvas.pack()
bush = PhotoImage(file='index\python\project\img\Tiny Adventure Pack\Other\Misc\Tree\Tree.png')
grass = PhotoImage(file='index\python\project\img\grass.png')
player = [PhotoImage(file='index\python\project\img\Tiny Adventure Pack\Character\Char_one\Idle\Char_idle_down1.png'),PhotoImage(file='index\python\project\img\Tiny Adventure Pack\Character\Char_one\Idle\Char_idle_down2.png'),PhotoImage(file='index\python\project\img\Tiny Adventure Pack\Character\Char_one\Idle\Char_idle_down3.png'),PhotoImage(file='index\python\project\img\Tiny Adventure Pack\Character\Char_one\Idle\Char_idle_down4.png'),PhotoImage(file='index\python\project\img\Tiny Adventure Pack\Character\Char_one\Idle\Char_idle_down5.png'),PhotoImage(file='index\python\project\img\Tiny Adventure Pack\Character\Char_one\Idle\Char_idle_down6.png')]
map_x = 5
map_y = 5
draw = [bush,bush,bush,bush,bush ,bush,grass,grass,grass,bush ,bush,grass,grass,grass,bush ,bush,grass,grass,grass,bush ,bush,bush,bush,bush,bush]
x_coord = 350
y_coord = 250
z = 0
# draws the Map
for i in range(map_y):
    for y in range(map_x):
        Map.append(canvas.create_image(x_coord,y_coord,image=draw[z],anchor='nw'))
        z += 1
        x_coord += 32
    x_coord = 350
    y_coord += 32

avatar = canvas.create_image(350,250,image=player[frame],anchor='nw')
window.mainloop()