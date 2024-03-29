import tkinter as tk

def SetValue(var):
    tk.Label(f1, textvariable= var, height = 3).grid()

def Click(num):

    #deal with 0 +-x/ with other number
    op = ['+', '-', '*', '/']
    if var.get() == '0' and num in op:
        var.set('0' + num)

    # user keep click 0 -> only 0 remain in expression
    # if divide by 0 -> expression display error
    elif var.get() == '0' or var.get() == 'Error':
        var.set(num)

    # otherwise, concatenate the click character with expression
    else:
        print(var.get())
        var.set(var.get() + num)

# When user click 'C' -> expression = '0'
def Clear():
    var.set('0')

# When user click '=' -> evaluate the expression
def Calculate():
    expression = var.get()

    # find out what is the first / second number
    # and get the operation
    for i in range(1, len(expression)):
        if expression[i] in ['-', '*', '+', '/']:
            operation = expression[i]
            a = int(expression[:i])
            b = int(expression[i+1:])
            break

    #switch case to calculate the result
    match operation:
        case '+':
            var.set(a + b)
        case '-':
            var.set(a - b)
        case '*':
            var.set(a * b)
        case '/':
            if b == 0:
                var.set('Error')
            else:
                var.set(a // b)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Lab4")

    f1 = tk.Frame(window)
    f2 = tk.Frame(window)
    f1.pack()
    f2.pack()

    var = tk.StringVar()
    var.set('0')
    SetValue(var)

    # button layout with grid
    btn7 =          tk.Button(f2, text = '7', borderwidth = 5, width = 6, height = 2, command = lambda: Click('7')).grid(row = 0, column = 0)
    btn8 =          tk.Button(f2, text = '8', borderwidth = 5, width = 6, height = 2, command = lambda: Click('8')).grid(row = 0, column = 1)
    btn9 =          tk.Button(f2, text = '9', borderwidth = 5, width = 6, height = 2, command = lambda: Click('9')).grid(row = 0, column = 2)
    btn_times =     tk.Button(f2, text = 'x', borderwidth = 5, width = 6, height = 2, command = lambda: Click('*')).grid(row = 0, column = 3)
    btn4 =          tk.Button(f2, text = '4', borderwidth = 5, width = 6, height = 2, command = lambda: Click('4')).grid(row = 1, column = 0)
    btn5 =          tk.Button(f2, text = '5', borderwidth = 5, width = 6, height = 2, command = lambda: Click('5')).grid(row = 1, column = 1)
    btn6 =          tk.Button(f2, text = '6', borderwidth = 5, width = 6, height = 2, command = lambda: Click('6')).grid(row = 1, column = 2)
    btn_minus =     tk.Button(f2, text = '-', borderwidth = 5, width = 6, height = 2, command = lambda: Click('-')).grid(row = 1, column = 3)
    btn1 =          tk.Button(f2, text = '1', borderwidth = 5, width = 6, height = 2, command = lambda: Click('1')).grid(row = 2, column = 0)
    btn2 =          tk.Button(f2, text = '2', borderwidth = 5, width = 6, height = 2, command = lambda: Click('2')).grid(row = 2, column = 1)
    btn3 =          tk.Button(f2, text = '3', borderwidth = 5, width = 6, height = 2, command = lambda: Click('3')).grid(row = 2, column = 2)
    btn_plus =      tk.Button(f2, text = '+', borderwidth = 5, width = 6, height = 2, command = lambda: Click('+')).grid(row = 2, column = 3)
    btn0 =          tk.Button(f2, text = '0', borderwidth = 5, width = 6, height = 2, command = lambda: Click('0')).grid(row = 3, column = 0)
    btnC =          tk.Button(f2, text = 'C', borderwidth = 5, width = 6, height = 2, command = lambda: Clear()).grid(row = 3, column = 1)
    btn_equal =     tk.Button(f2, text = '=', borderwidth = 5, width = 6, height = 2, command = lambda: Calculate()).grid(row = 3, column = 2)
    btn_divide =    tk.Button(f2, text = '/', borderwidth = 5, width = 6, height = 2, command = lambda: Click('/')).grid(row = 3, column = 3)

    window.mainloop()