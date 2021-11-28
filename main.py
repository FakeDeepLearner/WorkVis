import pandas
import matplotlib
from tkinter import *
import project_part_1
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import project_part_1 as proj1
import project_part_2 as proj2

root = Tk()

text_box = Entry(root, width= 60, fg= "black",bg= "cyan")
text_box.pack()

my_button = Button(root, text= "Execute", command= proj1.plotting_the_graph(text_box.get()))
my_button.pack()


root.mainloop()
    
