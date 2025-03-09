import tkinter as tk


def carre(event):

    color = "red"

    if event.x <= 250:
        color = "blue"
    else:
        color = "red"

    canva.create_oval(event.x-25, event.y-25, event.x+25,
                      event.y+25, fill=color, width=0)


window = tk.Tk()
window.title("click")
canva = tk.Canvas(window, width=500, height=500, bg="black")
ligne = canva.create_line(250, 0, 250, 500, fill="white")

canva.bind("<Button-1>", carre)

canva.grid()
window.mainloop()
