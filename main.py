"""
A module that contains the code to run the project
"""

import pandas
import matplotlib
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import project_part_1 as proj1
import project_part_2 as proj2

matplotlib.use('TkAgg')

########
# Part 1
########
root = Tk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
# Displays the window in full screen

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

canvas = None

# Buttons:

button_of_agriculture = Button(frame, text="Agriculture",
                               command=lambda: display("Agriculture"), padx=25)
button_of_agriculture.grid(row=0, column=0)     # Placing the buttons on the screen

button_of_FFMQOG = Button(frame, text="FFMQOG",
                          command=lambda: display("Forestry, fishing, mining, quarrying, oil and gas"), padx=25)
button_of_FFMQOG.grid(row=0, column=1)

button_of_construction = Button(frame, text="Construction",
                                command=lambda: display("Construction"), padx=25)
button_of_construction.grid(row=0, column=2)

button_of_wholesale = Button(frame, text="Wholesale and retail trade",
                             command=lambda: display("Wholesale and retail trade"), padx=25)
button_of_wholesale.grid(row=0, column=3)

button_of_transportation_and_warehousing = Button(frame, text="Transportation and warehousing",
                                                  command=lambda: display("Transportation and warehousing"), padx=25)
button_of_transportation_and_warehousing.grid(row=0, column=4)

button_of_edicational_services = Button(frame, text="Education",
                                        command=lambda: display("Educational services"), padx=25)
button_of_edicational_services.grid(row=0, column=5)

button_of_health_care = Button(frame, text="Health care and social assistance",
                               command=lambda: display("Health care and social assistance"), padx=25)
button_of_health_care.grid(row=0, column=6)

button_of_accomodation_and_food = Button(frame, text="Accomodation and food services",
                                         command=lambda: display("Accommodation and food services"), padx=25)
button_of_accomodation_and_food.grid(row=0, column=7)

button_of_public_administration = Button(frame, text="Public administration",
                                         command=lambda: display("Public administration"), padx=25)
button_of_public_administration.grid(row=0, column=8)

quit_button = Button(frame, text="Close the program", command=root.destroy)  # The quit button
quit_button.grid(row=10, column=4)


def display(industry: str) -> None:    
    """
    Display the graph of the industry on the user panel.
    """
    global canvas, bottomframe

    if canvas:        # Removing the existing graph (if there is any)
        bottomframe.destroy()
        bottomframe = Frame(root)
        bottomframe.pack(side=BOTTOM)

    # Generating the figure and a canvas to display it
    figure = proj1.plotting_the_graph(industry)   
    canvas = FigureCanvasTkAgg(figure, master=bottomframe)

    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)  # Displaying the figure

root.mainloop()

########
# Part 2
########


