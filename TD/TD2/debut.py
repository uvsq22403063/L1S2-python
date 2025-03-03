import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

root = tk.Tk()

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

# Début de votre code
x = CANVAS_WIDTH / 2
y0 = 100
y1 = CANVAS_HEIGHT - 100
canvas.create_line(x, y0, x, y1)
canvas.create_oval(x - 25, y0 - 25, x + 25, y0 + 25)
canvas.create_oval(x - 25, y1 - 25, x + 25, y1 + 25)
canvas.create_oval(x + 25, (y0 + y1) / 2 - 25, x - 25, (y0 + y1) / 2 + 25)
# Fin de votre code

canvas.grid()
root.mainloop()
