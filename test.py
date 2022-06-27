from tkinter import *
from graph import *

import math

root = Tk()
root.title("Graph")

w = 1000
h = 1000

cavnas = Canvas(root, width = w, height = h)
cavnas.pack()

g = Graph(cavnas, w, h, -2, 2, -2, 2, .1)

g.function(lambda x: (x ** 2), color="green")
g.function(lambda x: (math.sin(x)), color="red")
g.function(lambda x: (math.cos(x)), color="blue")
g.function(lambda x: ((-1 * x) - 1), color="orange")

g.render()

root.mainloop()