##simple calculator with exception handling

import tkinter as tk
from tkinter import messagebox

mainWindow=tk.Tk()
mainWindow.title("  Basic Calculator  ")

label=tk.Label(mainWindow,text="enter first number",
                       pady=(10),padx=(20))
label.pack()

name_field_1=tk.Entry(mainWindow)
name_field_1.pack()

label=tk.Label(mainWindow,text="enter second number",
                       pady=(10),padx=(20))
label.pack()

name_field_2=tk.Entry(mainWindow)
name_field_2.pack()

label=tk.Label(mainWindow,text="operations")
label.pack()

add_button=tk.Button(mainWindow,text="+",command=lambda: addition())
add_button.pack()

sub_button_1=tk.Button(mainWindow,text="-",command=lambda: subtraction())
sub_button_1.pack()

mul_button_2=tk.Button(mainWindow,text="*",command=lambda: multiplication())
mul_button_2.pack()

div_button_3=tk.Button(mainWindow,text="/",command=lambda: divison())
div_button_3.pack()

result_label=tk.Label(mainWindow,text="operation result is :")
result_label.pack()

def addition():
    first=int(name_field_1.get())
    second=int(name_field_2.get())
    result=first+second
    # print(" result is ",result)
    result_label.config(text="operation result is : " + str(result))

def subtraction():
    first =int(name_field_1.get())
    second=int(name_field_2.get())
    result = first-second
    # print("result is ",result)
    result_label.config(text="operation result is" + str(result))

def multiplication():
    first = int(name_field_1.get())
    second = int(name_field_2.get())
    result = first * second
    # print("result is ",result)
    result_label.config(text="operation result is" + str(result))
def divison():
        first=name_field_1.get()
        second=name_field_2.get()
        try:
            first=int(first)
            second=int(second)
            result=first/second
            #print("result is ",result)
            result_label.config(text="operation result is : " +str(result))
        except ZeroDivisionError:
            messagebox.showerror(ZeroDivisionError,"divison by zero is not possible")
mainWindow.mainloop()
