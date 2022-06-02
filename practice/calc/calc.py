import tkinter as t

window = t.Tk()


f_entry = t.Entry(window)
c_entry = t.Entry(window)


def change_temp():
    c = c_entry.get()
    f = f_entry.get()
    if f == '' and c != '':
        try:
            c = float(c)
        except ValueError:
            return

        f_entry.insert(0, str(c * 9 / 5 + 32))
    elif f != '' and c == '':
        try:
            f = float(f)
        except ValueError:
            return

        c_entry.insert(0, str((f - 32) * 5 / 9))


def clear_entry():
    f_entry.delete(0, len(f_entry.get()))
    c_entry.delete(0, len(c_entry.get()))


f_label = t.Label(window, text="화씨")
c_label = t.Label(window, text="섭씨")

change_button = t.Button(window, text="섭씨 <-> 화씨", command=change_temp)

clear_button = t.Button(window, text="Clear!", command=clear_entry)

f_label.grid(column=0, row=1)
f_entry.grid(column=1, row=1)
c_label.grid(column=0, row=0)
c_entry.grid(column=1, row=0)

change_button.grid(column=0, row=2)
clear_button.grid(column=1, row=2)

window.mainloop()
