        # importing tkinter library
from tkinter import *
from tkinter import ttk

# colors
color1 = "#1e1f1e" #Black Color
color2 = "#feffff" #White Color
color3 = "#38576b" #Blue
color4 = "#ECEFF1" #Grey
color5 = "#FFAB40" #Orange

# screen 
screen =Tk()
screen.title("Calculadora")
screen.geometry("235x310")
screen.config(bg=color1)

# frames
frame_screen = Frame(screen,width=235, height=50, bg=color3)
frame_screen.grid(row=0, column=0)

frame_body = Frame(screen,width=235, height=268)
frame_body.grid(row=1, column=0)

# variable all values

all_values = ''

# functions
def value_input(event):

    global all_values
    all_values = all_values + str(event)
    text_result.set(all_values)

def calculate():
    global all_values
    result= eval(all_values)
    all_values=str(result)
    text_result.set(result)

def clearscreen():
    global all_values
    all_values =""
    text_result.set("")
    


# button labels
text_result = StringVar()

app_label = Label(frame_screen, textvariable=text_result, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=color3, fg=color2)
app_label.place(x=0, y=0)

# buttons
# layer 1
b_1 = Button(frame_body, command=clearscreen, text="C", width=11, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_body, command = lambda: value_input('%'), text="%", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_body, command = lambda: value_input('/'), text="/", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

# layer 2
b_4 = Button(frame_body, command = lambda: value_input('7'), text="7", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5 = Button(frame_body, command = lambda: value_input('8'), text="8", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)

b_6 = Button(frame_body, command = lambda: value_input('9'), text="9", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7 = Button(frame_body, command = lambda: value_input('*'), text="*", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

# layer 3
b_8 = Button(frame_body, command = lambda: value_input('4'), text="4", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)

b_9 = Button(frame_body, command = lambda: value_input('5'), text="5", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)

b_10 = Button(frame_body, command = lambda: value_input('6'), text="6", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)

b_11 = Button(frame_body, command = lambda: value_input('-'), text="-", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

# layer 4
b_12 = Button(frame_body, command = lambda: value_input('1'), text="1", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)

b_13 = Button(frame_body, command = lambda: value_input('2'), text="2", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)

b_14 = Button(frame_body, command = lambda: value_input('3'), text="3", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)

b_15 = Button(frame_body, command = lambda: value_input('+'), text="+", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

# layer 5
b_16 = Button(frame_body, command = lambda: value_input('0'), text="0", width=11, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)

b_17 = Button(frame_body, command = lambda: value_input('.'), text=".", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)

b_18 = Button(frame_body, command = calculate, text="=", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)

screen.mainloop()
