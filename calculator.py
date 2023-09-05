import math
import tkinter as tk

def add():
    a = float(num1.get())
    b = float(num2.get())
    result = a + b
    result_label.config(text="Result: " + str(round(result, 2)))

def substract():
    a = float(num1.get())
    b = float(num2.get())
    result = a - b
    result_label.config(text="Result: " + str(round(result, 2)))

def multiply():
    a = float(num1.get())
    b = float(num2.get())
    result = a * b
    result_label.config(text="Result: " + str(round(result, 2)))

def divide():
    a = float(num1.get())
    b = float(num2.get())
    if b == 0:
        result_label.config(text="Cannot divide by zero")
    else:
     result = a / b
     result_label.config(text="Result: " + str(round(result, 2)))

def square():
    a = float(num1.get())
    result = a ** 2
    result_label.config(text="Result: " + str(round(result, 2)))

def factorial():
    a = int(num1.get())
    factorial = 1
    if a < 0:
        result_label.config(text="Factorial does not exist for negative numbers ")
    elif a == 0:
        result_label.config(text="Factorial of zero is 1 ")
    else:
        for i in range(1, a + 1):
            factorial = factorial * i
        result = factorial
    result_label.config(text="Result: " + str(round(result, 2)))
    
def cube():
    a = float(num1.get())
    result = a ** 3
    result_label.config(text="Result: " + str(round(result, 2)))

window = tk.Tk()
window.title("Basic Calculator ")

label = tk.Label(window, text="Enter only First Number for single operand operations such as square, cube and factorial ")
label.pack()

label = tk.Label(window, text="ONLY USE INTEGERS AND FLOAT VALUES AS INPUTS ")
label.pack()

instruction_label1 = tk.Label(window, text="First Number :")
instruction_label1.pack()

num1 = tk.Entry(window)
num1.pack()

instruction_label2 = tk.Label(window, text="Second Number :")
instruction_label2.pack()
num2 = tk.Entry(window)
num2.pack()

add_button = tk.Button(window, text=" ADD ", command=add)
add_button.pack()

substract_button = tk.Button(window, text=" SUBSTRACT ", command=substract)
substract_button.pack()

multiply_button = tk.Button(window, text=" MULTIPLY ", command=multiply)
multiply_button.pack()

divide_button = tk.Button(window, text=" DIVIDE ", command=divide)
divide_button.pack()

square_button = tk.Button(window, text=" FIND SQUARE ", command=square)
square_button.pack()

cube_button = tk.Button(window, text=" FIND CUBE ", command=cube)
cube_button.pack()

factorial_button = tk.Button(window, text=" FIND FACTORIAL ", command=factorial)
factorial_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()


