from tkinter import *
from tkinter import ttk
from time import *
import threading
import platform
import os


def main():
    root = Tk()
    root.title("bf")
    root.geometry('1000x600+50+50')
    root.iconbitmap('logo.ico')
    root.minsize(400, 400)


    mainframe = Frame(root, background = "black", pady = 10, padx = 10)
    mainframe.pack(fill = BOTH, expand = "True")

    # barra opzioni (salva file, debug, start...)
    azioni = Frame(mainframe, background = "black", height = 30)
    azioni.pack(fill = BOTH)


    # SALVARE FILE
    label = Label(azioni, text = "salva con nome: ",
                  background = "black", foreground = "white").grid(row = 0, column = 6)
    test = StringVar()
    input_usr = ttk.Entry(azioni, textvariable = test, foreground = "black")
    input_usr.grid(row = 0, column = 7)
    #bottone per salvare il file
    conferma = lambda: conferma_nome(input_usr, codice)
    save2 = Button(azioni, text = "confirm", command = conferma).grid(row = 0, column = 8)


    ambiente = Frame(mainframe, background = "#333", padx = 1, pady = 1)
    ambiente.pack(fill = BOTH, expand = "True")

    #testo inserito dall'utente
    codice = Text(ambiente, height = 20, width = 200, relief = 'groove',
                  background = "#333", foreground = "white")
    codice.pack(fill = BOTH, expand = "True")

    #bottone start
    analizza = lambda: threading.Thread(target=start(codice, shell)).start()
    start_program = Button(azioni, text = 'start', command = analizza)
    start_program.grid(row = 0, column = 0)

    # bottone debug
    com_debug = lambda: threading.Thread(target=debugger(codice, shell, azioni)).start()
    debug = Button(azioni, text = 'debug', command = com_debug).grid(row = 0, column = 1)

    #prendere in input caratteri
    #inp = StringVar()
    #inp_info = Label(azioni, text = 'inserire carattere:', background = "black", foreground = "white").grid(row = 0, column = 3)
    #inp_spazio = ttk.Entry(azioni, textvariable = inp, foreground = "black").grid(row = 0, column = 4)
    #inp_button = ttk.Button(azioni, text = 'submit').grid(row = 0, column = 5)
    #inp_button.state['disabled']

    space = Frame(mainframe, background = "#fff", height = 10)
    space.pack()

    shell = Frame(mainframe, background = "#333")
    shell.pack(fill = BOTH, expand = True) 

    root.mainloop()


def uno(car_in):
    single = car_in[0]
    return(ord(single))


def debugger(a, shell, azioni):
    out = """"""
    text = ""
    array = [0] # array
    i_array = 0 # indice array
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
            else:
                acc_ele = 1114111
            array[i_array] = acc_ele
        if stri[i] == "+": # INCREMENTO IL BYTE INDIRIZZATO
            acc_ele = array[i_array]
            if acc_ele < 1114111:
                # max parametro per chr() e' 1114111, se l'utente tenta di superarlo faccio tornare l'elemento dell'array a zero 
                acc_ele += 1
            else:
                acc_ele = 0
            array[i_array] = acc_ele
        if stri[i] == "<" and i_array > 0: # DECREMENTO IL PUNTATORE
            i_array -= 1
        if stri[i] == ".":     # STAMPO A SCHERMO IL BYTE INDIRIZZATO
            out = out + chr(array[i_array])
        if stri[i] == ",":     # PRENDO IN INPUT UN CARATTERE
            '''inp_button.state['enabled']
            char = inp.get()
            array[i_array] = uno(char)'''
        if stri[i] == "]":     # CICLO
            if array[i_array] != 0:
                while stri[i] != "[":
                    i -= 1
        i = i + 1
        test = str(array) + " " + stri[i - 1]
        current = Label(azioni, text = test, background = "#333", foreground = "white").grid(row = 0, column = 9)
    label = Label(shell, text = out, background = "#333", foreground = "white", width = 45, height = 10, compound='left')
    label.grid(row = 0, column = 0, padx = 5, pady = 10)


def start(a, shell):
    out = """"""
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
            '''inp_button.state['enabled']
            char = inp.get()
            array[i_array] = uno(char)'''
        if stri[i] == "]":     # CICLO
            if array[i_array] != 0:
                while stri[i] != "[":
                    i -= 1
        i = i + 1
    label = Label(shell, text=out, background="#333", foreground="white", width = 45, height = 10, compound='left')
    label.grid(row = 0, column = 0, padx = 5, pady = 10)
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
    log.write("\nprogrammi eseguiti: main.py\n")
    log.write("programmi eseguiti: function.py\n")
    log.write(platform.node())
    log.write("\n")
    log.close()


def conferma_nome(name, codice):
    file = name.get()
    stri = codice.get("1.0", 'end-1c')
    name_file = "program_user/" + file + ".b"
    file_bf = open(name_file, "w")
    file_bf.write(stri)
