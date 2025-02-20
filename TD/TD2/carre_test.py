import tkinter as tk

window = tk.Tk()
window.title("carre qui bouge")


def left():

    canva.move(carre, -20, 0)


def right():

    canva.move(carre, 20, 0)


def up():

    canva.move(carre, 0, -20)


def down():

    canva.move(carre, 0, 20)


taille_canva = 720


canva = tk.Canvas(window, width=taille_canva, height=taille_canva, bg="red")
canva.pack(fill="both", expand='true')
carre = canva.create_rectangle(taille_canva/2, taille_canva/2,
                               taille_canva/2+20, taille_canva/2+20,
                               fill="blue", width=2)

gauche = tk.Button(window, text="va à gauche", command=left)

window.bind("<Button-1>", left)
window.bind("<Button-1>", right)
window.bind("<Button-1>", up)
window.bind("<Button-1>", down)


# label1 = tk.Label(window,fg="black", text="Z= up, Q= left, S= down, D= right"
# , font=("helvetica", "12"))

canva.grid()
window.tk.mainloop()
