from tkinter import *



root = Tk()


def my_click():
    pass
    
    

my_button = Button(root, text = "Agriculture", command= my_click, padx= 40, pady=1)
my_button.grid(row = 0, column= 0)

my_button1 = Button(root, text = "FFMQOG", command= my_click, padx= 40, pady=1)
my_button1.grid(row = 0, column= 1)

my_button2 = Button(root, text = "Construction", command= my_click, padx= 40, pady=1)
my_button2.grid(row = 0, column= 2)

my_button3 = Button(root, text = "Wholesale and retail", command= my_click, padx= 40, pady=1)
my_button3.grid(row = 0, column= 3)

my_button4 = Button(root, text = "Transportation", command= my_click, padx= 40, pady=1)
my_button4.grid(row = 0, column= 4)

my_button5 = Button(root, text = "Education", command= my_click, padx= 40, pady=1)
my_button5.grid(row = 0, column= 5)

my_button6 = Button(root, text = "HC & SA", command= my_click, padx= 40, pady=1)
my_button6.grid(row = 0, column= 6)

my_button7 = Button(root, text = "A & Food Services", command= my_click, padx= 40, pady=1)
my_button7.grid(row = 0, column= 7)

my_button8 = Button(root, text = "Public administration", command= my_click, padx= 40, pady=1)
my_button8.grid(row = 0, column= 8)


    


root.mainloop()                                