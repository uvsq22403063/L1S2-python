import tkinter as tk

click = 0

formes = []
coord = []


def carre(event):

    global formes, coord

    if event.x <= 250:
        color = "blue"
    else:
        color = "red"

    carre = canva.create_rectangle(event.x-1, event.y-1, event.x+1,
                                   event.y+1, fill=color, width=0)

    formes.append(carre)
    coord.append(canva.coords(carre))
    print(coord)

    if len(coord) == 2:
        if (coord[0][0] <= 250 and coord[1][0] <= 250):
            canva.create_line(coord[-1][0], coord[-1][1], coord[-2][0],
                              coord[-2][1], fill="blue")
            coord = []
            formes = []
        elif (coord[0][0] > 250 and coord[1][0] > 250):
            canva.create_line(coord[-1][0], coord[-1][1], coord[-2][0],
                              coord[-2][1], fill="blue")
            coord = []
            formes = []
        else:
            canva.create_line(coord[-1][0], coord[-1][1], coord[-2][0],
                              coord[-2][1], fill="red")
            coord = []
            formes = []


window = tk.Tk()
window.title("click")
canva = tk.Canvas(window, width=500, height=500, bg="black")
ligne = canva.create_line(250, 0, 250, 500, fill="white")

canva.bind("<Button-1>", carre)

canva.grid()
window.mainloop()
