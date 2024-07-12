#1.0
from tkinter import *

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operator = operator_var.get()

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2!= 0:
            result = num1 / num2
        else:
            result = "除数不能为 0"

    result_label.config(text=f"结果: {result}")

root = Tk()
root.title("图形化计算器")

Label(root, text="第一个数:").grid(row=0, column=0)
entry1 = Entry(root)
entry1.grid(row=0, column=1)

Label(root, text="第二个数:").grid(row=1, column=0)
entry2 = Entry(root)
entry2.grid(row=1, column=1)

operator_var = StringVar()
operator_var.set('+')

operators = ['+', '-', '*', '/']
operator_menu = OptionMenu(root, operator_var, *operators)
operator_menu.grid(row=2, column=0)

Button(root, text="计算", command=calculate).grid(row=2, column=1)

result_label = Label(root, text="结果: ")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()