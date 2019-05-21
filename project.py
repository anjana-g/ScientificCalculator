import os
import Tkinter
import random
import math
import tkMessageBox
from numpy import *
import matplotlib
matplotlib.use("TkAgg") # set the backend
import matplotlib.pyplot as plt

root = Tkinter.Tk()
#Tkinter.Tk().option_add('*Dialog.msg.font', 'Courier 12')

#Change the title
root.title("Graphing Calculator")

#Change window size
root.geometry("500x500")

     #ADD TO TEXTBOX
def yay ():
	tkMessageBox.showinfo("About the coder.",
	"""
	Made by Anjana Govindarajan (12)
	2016.
	""")
def one ():
	txtbox.insert("end", 1)
def two ():
	txtbox.insert("end", 2)
def three ():
	txtbox.insert("end", 3)
def four ():
	txtbox.insert("end", 4)
def five ():
	txtbox.insert("end", 5)
def six ():
	txtbox.insert("end", 6)
def seven ():
	txtbox.insert("end", 7)
def eight ():
	txtbox.insert("end", 8)
def nine ():
	txtbox.insert("end", 9)
def zero ():
	txtbox.insert("end", 0)
def decimal():
	txtbox.insert("end", ".")
def add():
	txtbox.insert("end", "+")
def subtract():
	txtbox.insert("end", "-")
def multiply():
	txtbox.insert("end", "*")
def divide():
	txtbox.insert("end", "/")
def delete():
	txtbox.delete(0, "end")
def pi():
	txtbox.insert("end", math.pi)
     #ADD TO TEXTBOX

	#PERFORM FUNCTIONS

def do_sqrt():
	os.system("clear")
	text = float(txtbox.get())
	#if text is negative
	if (text < 0):
		lbl_display = Tkinter.Label(root, text="Error", bg="white")
		lbl_display.grid(row=1,column=6)
	ans = math.sqrt(text)
	txtbox.delete(0, "end")
	txtbox.insert(0, ans)
	#

def perform_calc():
	os.system("clear")
	text = str(txtbox.get())
	ans = eval(text)
	txtbox.delete(0, "end")
	txtbox.insert(0, ans)

def perform_log():
	os.system("clear")
	text = float(txtbox.get())
	if (text <= 0):
		lbl_display = Tkinter.Label(root, text="Error", bg="white")
		lbl_display.grid(row=1,column=6)
	ans = log10(text)
	txtbox.delete(0, "end")
	txtbox.insert(0, ans)

def do_sin():
	os.system("clear")
	text = float(txtbox.get())
	ans = math.sin(text)
	txtbox.delete(0, "end")
	txtbox.insert(0, ans)

def do_cos():
	os.system("clear")
	text = float(txtbox.get())
	ans = math.cos(text)
	txtbox.delete(0, "end")
	txtbox.insert(0, ans)

def do_tan():
	os.system("clear")
	text = float(txtbox.get())
	ans = math.tan(text)
	txtbox.delete(0, "end")
	txtbox.insert(0, ans)

def do_arctan():
	os.system("clear")
	text = float(txtbox.get())
	ans = math.atan(text)
	txtbox.delete(0, "end")
	txtbox.insert(0, ans)

def do_arcsin():
	os.system("clear")
	text = float(txtbox.get())
	ans = math.asin(text)
	txtbox.delete(0, "end")
	txtbox.insert(0, ans)

def do_arccos():
	os.system("clear")
	text = float(txtbox.get())
	ans = math.acos(text)
	txtbox.delete(0, "end")
	txtbox.insert(0, ans)

def do_ln():
	os.system("clear")
	text = float(txtbox.get())
	if (text <= 0):
		lbl_display = Tkinter.Label(root, text="Error", bg="white")
		lbl_display.grid(row=1,column=6)
	ans = math.log(text)
	txtbox.delete(0, "end")
	txtbox.insert(0, ans)

def show_equations():
	tkMessageBox.showinfo("List of Common Functions",
	"""
	y= x

	y=x^2  : y = pow(x,2) : y= (x)**2

	y = sqrt(x)

	y= log(x) --> natural logarithm

	y= sin(x) , y=arcsin(x)

	y= cos(x) , y=arccos(x)

	y= tan(x) , y=arctan(x)
	""")

	#PERFORM FUNCTIONS
	#graph function
def graph():
	if txtbox.get() == "Giraffe":
		tkMessageBox.showinfo("Giraffe",
"""


Q.Why did the giraffe leave work early?
A.To avoid the giraffic jam.
                                      ._ o o
                                       \_'-)|_
                                    '""       \
                                  '"  ## |  0 0 .
                                '" ##   '-\__    `.
                              '"       /     `--._;)
                            '"     ## /
                          '"   ##    /
	""")

	elif txtbox.get() == "Money":
		tkMessageBox.showinfo("$$$$$",
"""
Money money money, You're so funny.


                      $$$$
                      $$$$
           $$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$$$
     $$$$$$$       $$$$    $$$$$$$$
   $$$$$$          $$$$        $$$$$$$
  $$$$$$           $$$$          $$$$$$
  $$$$$$           $$$$
  $$$$$$           $$$$
   $$$$$$          $$$$
    $$$$$$$$      $$$$
      $$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$
                 $$$$$$$$$$$$$$$$
                      $$$$ $$$$$$$$$$
                      $$$$       $$$$$$$
                     $$$$          $$$$$$
                      $$$$           $$$$$$
$$$$$$$            $$$$          $$$$$$$
 $$$$$$            $$$$          $$$$$$$
  $$$$$$$          $$$$        $$$$$$$$
   $$$$$$$$       $$$$      $$$$$$$$
      $$$$$$$$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$$
                  $$$$$$$$
                      $$$$
                      $$$$
	""")

	else:
		x = linspace(-10, 10, 100)
		y = eval(txtbox.get()) #textbox should not have y=
		plt.figure()
		plt.axhline(y=0, color='Black')
		plt.axvline(x=0, color='Black')
		plt.title(txtbox.get())
		plt.xlabel('x')
		plt.ylabel('y')
		plt.plot(x,y, color = 'Green')
		plt.show(block=False)
		plt.get_current_fig_manager().window.wm_geometry("+600+200")
	#graph function

			#add widgets
lbl_title = Tkinter.Label(root, text= "Calculator", bg="green")
lbl_title.grid(row=0,column=2)

txtbox = Tkinter.Entry(root, width=40)
txtbox.grid(row=1,column=1, columnspan = 5)
str_textbox = str(txtbox)

            #BUTTONS FROM 1-9
btn_1 = Tkinter.Button(root, text="1", fg="black", bg="white",command=one)
btn_1.grid(row=4,column=3)

btn_2 = Tkinter.Button(root, text="2", fg="black", bg="white",command=two)
btn_2.grid(row=4,column=4)

btn_3 = Tkinter.Button(root, text="3", fg="black", bg="white",command=three)
btn_3.grid(row=4,column=5)

btn_4 = Tkinter.Button(root, text="4", fg="black", bg="white",command=four)
btn_4.grid(row=3,column=3)

btn_5 = Tkinter.Button(root, text="5", fg="black", bg="white",command=five)
btn_5.grid(row=3,column=4)

btn_6 = Tkinter.Button(root, text="6", fg="black", bg="white",command=six)
btn_6.grid(row=3,column=5)

btn_7 = Tkinter.Button(root, text="7", fg="black", bg="white",command=seven)
btn_7.grid(row=2,column=3)

btn_8 = Tkinter.Button(root, text="8", fg="black", bg="white",command=eight)
btn_8.grid(row=2,column=4)

btn_9 = Tkinter.Button(root, text="9", fg="black", bg="white",command=nine)
btn_9.grid(row=2,column=5)

btn_0 = Tkinter.Button(root, text="0", fg="black", bg="white",command=zero)
btn_0.grid(row=5,column=4)

btn_pi = Tkinter.Button(root, text="pi", fg="black", bg="white",command=pi)
btn_pi.grid(row=6,column=5)

btn_dec = Tkinter.Button(root, text=".", fg="black", bg="white",command=decimal)
btn_dec.grid(row=5,column=3)

btn_equ = Tkinter.Button(root, text="=", fg="black", bg="white",command=perform_calc)
btn_equ.grid(row=5,column=5)
        #BUTTONS FROM 1-9

        #OTHER CALC FUNCTION BUTTONS
btn_sqrt = Tkinter.Button(root, text="sqrt", fg="black", bg="white",command=do_sqrt)
btn_sqrt.grid(row=5,column=1)

btn_log = Tkinter.Button(root, text="log", fg="black", bg="white",command=perform_log)
btn_log.grid(row=5,column=2)

btn_ln = Tkinter.Button(root, text="ln", fg="black", bg="white",command=do_ln)
btn_ln.grid(row=6,column=1)

btn_sin = Tkinter.Button(root, text="sin", fg="black", bg="white",command= do_sin)
btn_sin.grid(row=2,column=2)

btn_cos = Tkinter.Button(root, text="cos", fg="black", bg="white",command=do_cos)
btn_cos.grid(row=3,column=2)

btn_tan = Tkinter.Button(root, text="tan", fg="black", bg="white",command=do_tan)
btn_tan.grid(row=4,column=2)

btn_degsin = Tkinter.Button(root, text="arcsin", fg="black", bg="white",command=do_arcsin)
btn_degsin.grid(row=2,column=1)

btn_degcos = Tkinter.Button(root, text="arccos", fg="black", bg="white",command=do_arccos)
btn_degcos.grid(row=3,column=1)

btn_degtan = Tkinter.Button(root, text="arctan", fg="black", bg="white",command=do_arctan)
btn_degtan.grid(row=4,column=1)
        #OTHER CALC FUNCTION BUTTONS

         #ADD, SUBTRACT, MULTIPLY, DIVIDE
btn_add = Tkinter.Button(root, text="+", fg="black", bg="white",command=add)
btn_add.grid(row=2,column=6)

btn_sub = Tkinter.Button(root, text="-", fg="black", bg="white",command=subtract)
btn_sub.grid(row=3,column=6)

btn_mult = Tkinter.Button(root, text="*", fg="black", bg="white",command=multiply)
btn_mult.grid(row=4,column=6)

btn_div = Tkinter.Button(root, text="/", fg="black", bg="white",command=divide)
btn_div.grid(row=5,column=6)

btn_deletee = Tkinter.Button(root, text="del", fg="black", bg="white",command=delete)
btn_deletee.grid(row=6,column=6)

btn_showequ = Tkinter.Button(root, text="Show Common Equations", fg="black", bg="white",command=show_equations)
btn_showequ.grid(row=6,column=2, columnspan = 3)

btn_graph = Tkinter.Button(root, text="graph function", fg="black", bg="white",command=graph)
btn_graph.grid(row=7,column=1)

quit = Tkinter.Button(root, text="exit", fg="black", bg="white",command=exit)
quit.grid(row=7,column=6)

btn_yay = Tkinter.Button(root, text=" ", fg="black", bg="white",command=yay)
btn_yay.grid(row=7,column=5)
         #ADD, SUBTRACT, MULTIPLY, DIVIDE
#Splash Screen
"""splash_image = Tkinter.PhotoImage(file="circ.gif") #https://media.giphy.com/media/3oEdvdAGaxHPqzNxMQ/giphy.gif
splash_label = Tkinter.Label(root, image=splash_image)
splash_label.place(x=0,y=0, relwidth=1, relheight=1)
root.after(2000,splash_label.destroy)"""

#Start the main loop
root.mainloop()
