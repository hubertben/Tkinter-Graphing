
def map(x, x1, x2, y1, y2):
    return y1 + (x - x1) * (y2 - y1) / ((x2 - x1) or 1)


def circle(canvas, x, y, r, fill = "black", outline = "black"):
    canvas.create_oval(x - r, y - r, x + r, y + r, fill = fill, outline = outline)

def square(canvas, x, y, r, fill = "black", outline = "black"):
    canvas.create_rectangle(x - r, y - r, x + r, y + r, fill = fill, outline = outline)

def rectangle(canvas, x, y, w, h, fill = "black", outline = "black"):
    canvas.create_rectangle(x, y, x + w, y + h, fill = fill, outline = outline)

def triangle(canvas, x, y, w, h, fill = "black", outline = "black"):
    canvas.create_polygon(x, y, x + w, y, x + w / 2, y + h, fill = fill, outline = outline)

def triangle(canvas, points, fill = "black", outline = "black"):
    canvas.create_polygon(points, fill = fill, outline = outline)

def polygon(canvas, points, fill = "black", outline = "black"):
    canvas.create_polygon(points, fill = fill, outline = outline)

def line(canvas, x1, y1, x2, y2, fill = "black", width = 1):
    canvas.create_line(x1, y1, x2, y2, fill = fill, width = width)

def textOnCanvas(canvas, x, y, text, fill = "black", font = "Arial", size = 12):
    canvas.create_text(x, y, text = text, fill = fill, font = str(font) + " " + str(size))
    

class Graph:

    def __init__(self, canvas, w, h, min_x = -1, max_x = 1, min_y = -1, max_y = 1, inc = 0.1):
        self.canvas = canvas
        self.w = w
        self.h = h
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.inc = inc

        self.total_steps = int((self.max_x - self.min_x) / self.inc)
        self.increment = self.w / self.total_steps

        self.points = []
        self.lines = []
        self.shapes = []

    def render(self):
        self.grid()
        for s in self.shapes:
            s.render()
        

    def grid(self):
        line(self.canvas, 0, self.h / 2, self.w, self.h / 2, fill = "gray", width = 3)
        line(self.canvas, self.w / 2, 0, self.w / 2, self.h, fill = "gray", width = 3)

        for i in range(self.total_steps):
            x = i * self.increment
            line(self.canvas, x, 0, x, self.h, fill = "gray", width = 1)
            line(self.canvas, 0, x, self.w, x, fill = "gray", width = 1)


    def function(self, func, connected = True, color = "black"):
        s = Set(self.canvas, self)
        s.params(connected=connected, color=color)

        for i in range(int((self.max_x - self.min_x) / self.inc) + 1):
            x = self.min_x + i * self.inc
            y = -func(x)
            s.add(x, y)

        self.shapes.append(s)

    def scalePoint(self, x, y):
        return map(x, self.min_x, self.max_x, 0, self.w), map(y, self.min_y, self.max_y, 0, self.h)
            

class Set:

    def __init__(self, canvas, graph):
        self.canvas = canvas
        self.graph = graph
        self.points = []
        self.params()

    def add(self, x, y):
        self.points.append((x, y))

    def params(self, connected = True, color = "black"):
        self.connected = connected
        self.color = color

    def render(self):

        c = 1 if self.connected else 0
        
        for i in range(len(self.points) - c):
            x, y = self.points[i]
            x, y = self.scalePoint(x, y)

            if (self.connected):
                x2, y2 = self.points[i + 1]
                x2, y2 = self.scalePoint(x2, y2)
                line(self.canvas, x, y, x2, y2, fill = self.color, width = 3)
                circle(self.canvas, x, y, 3, fill = self.color, outline = self.color)
            else:
                circle(self.canvas, x, y, 3, fill = self.color, outline = self.color)

    def scalePoint(self, x, y):
        return map(x, self.graph.min_x, self.graph.max_x, 0, self.graph.w), map(y, self.graph.min_y, self.graph.max_y, 0, self.graph.h)