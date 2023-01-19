from tkinter import *
from tkinter import ttk
from time import *
import platform
import os


def main():
    out = ''
    root = Tk()
    root.title("bf")
    root.geometry('1000x600')
    root.iconbitmap('logo.ico')
    root.minsize(400, 400)

    mainframe = Frame(root, background = "black", pady = 10, padx = 10)
    mainframe.pack(fill = BOTH, expand = "True")

    azioni = Frame(mainframe, background = "black", height = 30)
    azioni.pack(fill = BOTH)

    ambiente = Frame(mainframe, background = "#333", padx = 1, pady = 1)
    ambiente.pack(fill = BOTH, expand = "True")

    codice = Text(ambiente, height = 20, width = 200, relief = 'groove',
                  background = "#333", foreground = "white")
    codice.pack(fill = BOTH, expand = "True")

    analizza = lambda: start(codice, shell, out)
    start_program = Button(azioni, text = 'start', command = analizza)
    start_program.pack(side = LEFT)
    
    com_debug = lambda: debugger(codice, shell, out)
    debug = Button(azioni, text = 'debug', command = com_debug).pack(side = LEFT)

    save_f = lambda: savefile(codice, shell, out)
    save = Button(azioni, text = 'save', command = save_f).pack(side = LEFT)
    
    space = Frame(mainframe, background = "#fff", height = 10)
    space.pack()

    shell = Frame(mainframe, background = "#333")
    shell.pack(fill = BOTH, expand = True) 

    root.mainloop()


def uno(car_in):
    single = car_in[0]
    return(ord(single))


def debugger(a, shell, out):
    array = [0] #array
    i_array = 0 #indice array
    stri = a.get("1.0", 'end-1c')
    i = 0
    while i < len(stri):
        if stri[i] == ">":  # INCREMENTO IL PUNTATORE
            if i_array + 1 == len(array):
                array.append(0)
            i_array += 1
        if stri[i] == "-":  # DECREMENTO IL BYTE INDIRIZZATO
            acc_ele = array[i_array]
            if acc_ele > 0: 
                acc_ele -= 1
                array[i_array] = acc_ele
            else:
                acc_ele = 255
                array[i_array] = acc_ele
        if stri[i] == "+":  # INCREMENTO IL BYTE INDIRIZZATO
            acc_ele = array[i_array]
            if array[i_array] <= 255:
                acc_ele += 1
                array[i_array] = acc_ele
            else:
                acc_ele = 0
                array[i_array] = acc_ele
        else:
            array[i_array] = 0
        if stri[i] == "<" and i_array > 0: # DECREMENTO IL PUNTATORE
            i_array -= 1
        if stri[i] == ".":     # STAMPO A SCHERMO IL BYTE INDIRIZZATO
            out = out + chr(array[i_array])
        if stri[i] == ",":     # PRENDO IN INPUT UN CARATTERE
            car_in = str(input("inserire carattere: "))
            array[i_array] = uno(car_in)
        if stri[i] == "]":     # CICLO
            if array[i_array] != 0:
                while stri[i] != "[":
                    i -= 1
        i = i + 1
        print(array, '\n', stri[i - 1])
        sleep(0)
    label = Label(shell, text = out, background = "#333", foreground = "white")
    label.grid(row = 0, padx = 5, pady = 5)


def start(a, shell, out):
    array = [0] #array
    i_array = 0 #indice array
    stri = a.get("1.0", 'end-1c')
    i = 0
    while i < len(stri):
        if stri[i] == ">":  # INCREMENTO IL PUNTATORE
            if i_array + 1 == len(array):
                array.append(0)
            i_array += 1
        if stri[i] == "-":  # DECREMENTO IL BYTE INDIRIZZATO
            acc_ele = array[i_array]
            if acc_ele > 0: 
                acc_ele -= 1
                array[i_array] = acc_ele
        if stri[i] == "+": # INCREMENTO IL BYTE INDIRIZZATO
            acc_ele = array[i_array]
            acc_ele += 1
            array[i_array] = acc_ele
        if stri[i] == "<" and i_array > 0: # DECREMENTO IL PUNTATORE
            i_array -= 1
        if stri[i] == ".":     # STAMPO A SCHERMO IL BYTE INDIRIZZATO
            out = out + chr(array[i_array])
        if stri[i] == ",":     # PRENDO IN INPUT UN CARATTERE
            car_in = str(input("inserire carattere: "))
            array[i_array] = uno(car_in)
        if stri[i] == "]":     # CICLO
            if array[i_array] != 0:
                while stri[i] != "[":
                    i -= 1
        i = i + 1
    label = Label(shell, text=out, background="#333", foreground="white")
    label.grid(row = 0, padx = 5, pady = 5)
    print(array)
    print(out)


def log():
    user = os.environ['USERNAME']
    log = open("../logmgnt/log/trace.log", "a")
    ltuple = localtime()
    time_string = strftime("\n%m/%d/%Y, %H:%M:%S", ltuple)
    log.write(str(time_string))
    log.write("\n")
    log.write(str(time()))
    log.write("\nuser:")
    log.write(user)
    log.write("\nprogrammi eseguiti: brainfuck.py\n")
    log.write("programmi eseguiti: function.py\n")
    log.write(platform.node())
    log.write("\n")
    log.close()


def savefile(codice, shell, out):
    label = Label(shell, text = "come vuoi salvare il file? >>>",
                  background = "#333", foreground = "white")
    label.grid(row = 0, column = 0, padx = 5, pady = 5)

    test = StringVar()
    input_usr = ttk.Entry(shell, textvariable = test, foreground = "black")
    input_usr.grid(row = 0, column = 1)

    conferma = lambda: conferma_nome(input_usr, codice, label)
    save2 = Button(shell, text = "confirm", command = conferma).grid(row = 0, column = 2)


def conferma_nome(name, codice):
    file = name.get()
    stri = codice.get("1.0", 'end-1c')
    name_file = "program_user/" + file + ".b"
    file_bf = open(name_file, "w")
    file_bf.write(stri)
