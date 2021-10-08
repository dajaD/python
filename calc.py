# calculator programmed using python
from tkinter import*
import math
import parser
import tkinter.messagebox


#function
# clicking buttons on the calculator and showing them . contains global variable operator
#
def btnClick(numbers):
        global operator
        operator = operator + str(numbers)
        text_Input.set(operator)

def btnClearDisplay():
        global operator
        operator = ""
        text_Input.set("")

def btnEqalsInput():
        global operator
        operator=""
        sumup = str(eval(operator))
        text_Input.set("sumup")
        

# name of app
cal = Tk()
cal.title(" Scientific Calculator")
cal.configure(background = "#4b4f00")
cal.resizable(width=False, height=False)
cal.geometry("430x450+0+0")
##############################################################################

calc=Frame(cal)
calc.grid()
operator=""
text_Input = StringVar()

##############################################################################

def iExit():
        iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm you want to exit")
        if iExit > 0:
                cal.destroy()
                return
#different calculator tytpes, whether scientific or standard
def Scientific():
        cal.resizable(width=False, height=False)
        cal.geometry("944x568+0+0")
def Standard():
        cal.resizable(width=False, height=False)
        cal.geometry("450x430+0+0")

#menu has file, edit, and help options
menuBar = Menu(calc)

fileMenu = Menu(menuBar, tearoff = 0)
menuBar.add_cascade(label = "File", menu=fileMenu)
fileMenu.add_command(label = "Standard", command = Standard)
fileMenu.add_command(label = "Scientific", command = Scientific)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = iExit)

editMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label = "Edit", menu=editMenu)
editMenu.add_command(label = "Edit")
editMenu.add_command(label = "Copy")
editMenu.add_separator()
editMenu.add_command(label = "Paste")


helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label = "Help", menu=helpMenu)
helpMenu.add_command(label = "View Help")

cal.configure(menu = menuBar)

# define textbox and the actual display
txtDisplay = Entry(calc,font=('arial', 20, 'bold'),
                bd=30, insertwidth=4, bg="#4b4f00", width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")


numberPad = "789456123"
i = 0
btn = []
for j in range [2,5]:
        for k in range(3):
                btn.append(Button(calc, width=6, height =2, font=('arial', 20, 'bold'), bd=4, text = numberPad[i]))
                btn[i].grid(row = j, column = k, pady = 1)

                i += 1
#=======================================================================
btnClear = Button(calc, text=chr(67), width=6, height =2, font=('arial', 20, 'bold'), bd=4, bg="4b4f00").grid(row=1, column=1, pady = 1)
# # the numeric buttons for the calculator. numbers '7,8,9' and the addition function
# btn7=Button(cal,padx=10, bd=8, fg="black", font=('arial', 20, 'bold'),
#             text="7").grid(row=1,column=0, sticky="nsew")

# btn8=Button(cal,padx=10, bd=8, fg="black", font=('arial', 20, 'bold'),
#             text="8").grid(row=1,column=1, sticky="nsew")

# btn9=Button(cal,padx=10, bd=8, fg="black", font=('arial', 20, 'bold'),
#             text="9").grid(row=1,column=2, sticky="nsew")

# btnAdd = Button(cal,padx=10, bd=8, fg="black", font=('arial', 20, 'bold'),
#             text="+").grid(row=1,column=3, sticky="nsew")
# ###############################################################################
# # the numeric buttons for the calculator. numbers '4,5,6' and subtraction function
# btn4=Button(cal,padx=10, bd=8, fg="black", font=('arial', 20, 'bold'),
#             text="4").grid(row=2,column=0, sticky="nsew")
# btn5=Button(cal,padx=10, bd=8, fg="black", font=('arial', 20, 'bold'),
#             text="5").grid(row=2,column=1, sticky="nsew")
# btn6=Button(cal,padx=10, bd=8, fg="black", font=('arial', 20, 'bold'),
#             text="6").grid(row=2,column=2, sticky="nsew")
# btnSub= Button(cal,padx=10, bd=8, fg="black", font=('arial', 20, 'bold'),
#             text="-").grid(row=2,column=3, sticky="nsew")
# ################################################################################
# # the numeric buttons for the calculator. numbers '1,2,3' and multiplication function
# btn1=Button(cal,padx=10, bd=8, fg="black", font=('arial', 20, 'bold'),
#             text="1").grid(row=3,column=0, sticky="nsew")
# btn2=Button(cal,padx=10, bd=8, fg="black", font=('arial', 20, 'bold'),
#             text="2").grid(row=3,column=1, sticky="nsew")
# btn3=Button(cal,padx=10, bd=8, fg="black", font=('arial', 20, 'bold'),
#             text="3").grid(row=3,column=2, sticky="nsew")
# btnMulti= Button(cal,padx=10, bd=8, fg="black", font=('arial', 20, 'bold'),
#             text="*").grid(row=3,column=3, sticky="nsew")
# ###############################################################################

# # the numeric buttons for the calculator. numbers '0' and functions clear, equals, division
# btn0=Button(cal,padx=10, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
#             text="0").grid(row=4,column=0, sticky="nsew")
# btnClear=Button(cal,padx=10, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
#             text="C").grid(row=4,column=1, sticky="nsew")
# btnEquals=Button(cal,padx=10, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
#             text="=").grid(row=4,column=2, sticky="nsew")
# btnDiv= Button(cal,padx=10, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
#             text="/").grid(row=4,column=3, sticky="nsew")
# ###############################################################################
cal.mainloop()
