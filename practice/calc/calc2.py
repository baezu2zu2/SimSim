import tkinter as t

window = t.Tk()
window.title('계산기!!')

result = 0
PLUS = 1
MINUS = 2
MULTIPLY = 3
DIVIDE = 4

operation = 0

float_point_bool = False

display_num = t.StringVar()


def set_operation(str):
    dict = {'+': PLUS, '-': MINUS, '*': MULTIPLY, '/': DIVIDE}

    if str not in dict.keys() or not float_point_bool:
        return False

    global operation, display_num
    operation = dict[str]

    display_num.set(display_num.get()+str)

    return True


def num_operation(num):
    global result, operation, float_point_bool

    if float_point_bool:
        if type(result) == int:
            result *= 10
            result += num
            result /= 10
        elif type(result) == float:
            float_part = result - int(result)

            divide_num = 10 ** (len(str(float_part))-1)
            result *= divide_num
            result += num
            result /= divide_num

        float_point_bool = False

    else:
        result *= 10
        result += num

    display_num.set(str(result))
    operation = 0


def float_point():
    if operation != 0:
        return False

    global float_point_bool

    float_point_bool = True

    return True


display = t.Label(window, width=33, bg='yellow', textvariable=display_num)
display.grid(row=0, column=0, columnspan=5)
button_text_list = [['7', '8', '9', '/', 'C'],
                   ['4', '5', '6', '*',  ''],
                   ['1', '2', '3', '-',  ''],
                   ['',  '0', '.', '+',  '']]

display_num.set(str(result))
for i in range(len(button_text_list)):
    for j in range(len(button_text_list[i])):
        if button_text_list[i][j].isdigit():
            t.Button(window, text=button_text_list[i][j], width=5
                     , command=lambda arg=button_text_list[i][j]: num_operation(int(arg))).grid(row=i+1, column=j)

        elif button_text_list[i][j] == '.':
            t.Button(window, text=button_text_list[i][j], width=5
                     , command=float_point).grid(row=i + 1, column=j)

        elif button_text_list[i][j] == '=':
            pass

        elif button_text_list[i][j] == 'C':
            pass
        else:
            t.Button(window, text=button_text_list[i][j], width=5
                     , command=lambda arg=button_text_list[i][j]: set_operation(arg)).grid(row=i + 1, column=j)


window.mainloop()
