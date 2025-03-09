import tkinter as tk

click = 0
color = "red"

formes = []


def carre(event):

    global formes, click, color

    if click >= 8:
        for i in range(8):
            canva.itemconfig(formes[i], fill="yellow", outline="yellow")
        color = "yellow"

    cercle = canva.create_oval(event.x-50, event.y-50, event.x+50,
                               event.y+50, fill=color, width=0)

    formes.append(cercle)

    click += 1
    if click == 10:
        for i in range(10):
            canva.delete(formes[i])
        formes = []
        click = 0


window = tk.Tk()
window.title("click")
canva = tk.Canvas(window, width=500, height=500, bg="black")


canva.bind("<Button-1>", carre)

canva.grid()
window.mainloop()
