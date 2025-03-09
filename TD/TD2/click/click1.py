import tkinter as tk


def carre(event):

    canva.create_rectangle(event.x, event.y, event.x+2,
                           event.y+2, fill="red", width=0)


window = tk.Tk()
window.title("click")
canva = tk.Canvas(window, width=500, height=500, bg="black")

canva.bind("<Button-1>", carre)

canva.grid()
window.mainloop()
