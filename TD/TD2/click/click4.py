import tkinter as tk

click = 0

color = "red"


def carre(event):

    global carre, click

    if click % 2 == 0:
        canva.itemconfig(carrer, fill="white")
    else:
        canva.itemconfig(carrer, fill="")

    click += 1
    if click == 10:
        window.destroy()


window = tk.Tk()
window.title("click")
canva = tk.Canvas(window, width=500, height=500, bg="black")
carrer = canva.create_rectangle(200, 200, 300, 300, fill="",
                                outline="white", width=2)

canva.bind("<Button-1>", carre)

canva.grid()
window.mainloop()
