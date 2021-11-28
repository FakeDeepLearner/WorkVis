import pandas
import matplotlib
from tkinter import *
import project_part_1 as proj1
import project_part_2 as proj2


########
#Part 1
########

def Display(industry: str) -> None:
    """
    Display the graph of the industry on the user panel.
    """
    proj1.plotting_the_graph(industry)
    
    
root = Tk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

button_of_agriculture = Button(root, text = "Agriculture", command= lambda: Display("Agriculture"), padx= 25)
button_of_agriculture.grid(row=0 , column= 0)

button_of_FFMQOG = Button(root, text = "FFMQOG", command= lambda: Display("Forestry, fishing, mining, quarrying, oil and gas"), padx= 25)
button_of_FFMQOG.grid(row=0 , column= 1)

button_of_construction = Button(root, text = "Construction", command= lambda: Display("Construction"), padx= 25)
button_of_construction.grid(row=0 , column= 2)

button_of_wholesale = Button(root, text = "Wholesale and retail trade", command= lambda: Display("Wholesale and retail trade"), padx= 25)
button_of_wholesale.grid(row=0 , column= 3)

button_of_transportation_and_warehousing = Button(root, text = "Transportation and warehousing", command= lambda: Display("Transportation and warehousing"), padx= 25)
button_of_transportation_and_warehousing.grid(row=0 , column= 4)

button_of_edicational_services = Button(root, text = "Education", command= lambda: Display("Educational services"), padx= 25)
button_of_edicational_services.grid(row=0 , column= 5)

button_of_health_care = Button(root, text = "Health care and social assistance", command= lambda: Display("Health care and social assistance"), padx= 25)
button_of_health_care.grid(row=0 , column= 6)

button_of_accomodation_and_food = Button(root, text = "Accomodation and food services", command= lambda: Display("Accommodation and food services"), padx= 25)
button_of_accomodation_and_food.grid(row=0 , column= 7)

button_of_public_administration = Button(root, text = "Public administration", command= lambda: Display("Public administration"), padx= 25)
button_of_public_administration.grid(row=0 , column= 8)

quit_button = Button(root, text = "Close the program", command= root.destroy)
quit_button.grid(row= 10, column= 4)

root.mainloop()
