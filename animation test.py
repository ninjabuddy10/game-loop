from tkinter import*
import time
frame = 0
window = Tk()
window.title("animation test")
window.geometry("700x500+370+75")
canvas = Canvas(window,width=700,height=500,bg='light blue')
canvas.pack()
player_w = ["index\python\project\img\Tiny Adventure Pack\Character\Char_one\Walk\Char_walk_down.png"]
player_i = ["index\python\project\img\Tiny Adventure Pack\Character\Char_one\Idle\Char_idle_down1.png","index\python\project\img\Tiny Adventure Pack\Character\Char_one\Idle\Char_idle_down2.png","index\python\project\img\Tiny Adventure Pack\Character\Char_one\Idle\Char_idle_down3.png","index\python\project\img\Tiny Adventure Pack\Character\Char_one\Idle\Char_idle_down4.png","index\python\project\img\Tiny Adventure Pack\Character\Char_one\Idle\Char_idle_down5.png","index\python\project\img\Tiny Adventure Pack\Character\Char_one\Idle\Char_idle_down6.png"]
player_a = ["index\python\project\img\Tiny Adventure Pack\Character\Char_one\Attack\Char_atk_down1.png","index\python\project\img\Tiny Adventure Pack\Character\Char_one\Attack\Char_atk_down2.png","index\python\project\img\Tiny Adventure Pack\Character\Char_one\Attack\Char_atk_down3.png","index\python\project\img\Tiny Adventure Pack\Character\Char_one\Attack\Char_atk_down4.png","index\python\project\img\Tiny Adventure Pack\Character\Char_one\Attack\Char_atk_down5.png","index\python\project\img\Tiny Adventure Pack\Character\Char_one\Attack\Char_atk_down6.png"]
def Attack(event):
    frame = 0
    for i in range(6):
        player = PhotoImage(file=player_a[frame])
        avatar = canvas.create_image(350,250,image=player,anchor="nw")
        window.update()
        time.sleep(0.08)
        frame = (frame + 1)
def Walk(event):
    frame = 0
    player = PhotoImage(file=player_w[frame])
    avatar = canvas.create_image(350,250,image=player,anchor="nw")
    window.update()
    time.sleep(0.08)
while True:
    frame = (frame + 1)
    if frame > 5:
        frame = 0
    player = PhotoImage(file=player_i[frame])
    avatar = canvas.create_image(350,250,image=player,anchor="nw")
    window.update()
    time.sleep(0.16)
    window.bind("<Up>",Attack)
    window.bind("<w>",Walk)

window.mainloop()