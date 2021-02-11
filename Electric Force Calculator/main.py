# Has some bugs (sizing)

import tkinter as tk
from tkinter import Canvas, Label, Frame, Entry, Button, PhotoImage, Scale

# ventana   
root = tk.Tk()
root.title('Ley de Coulomb')

# canva
canvas = Canvas(root, height=460, width=800, bg='#DCDADA')
canvas.pack()
frame = Frame()
frame.place(relx=0.1, rely=0.1)

# Charge 1
label = Label(frame, text='Carga 1')
label.grid(row=0,column=1)

label = Label(frame, text='microCoulombs')
label.grid(row=1, column=0)

chargedefault1 = tk.StringVar()
entry_charge = Entry(frame, width=10, textvariable=chargedefault1)
entry_charge.grid(row=1, column=1)
chargedefault1.set(4)

# Charge 2
label = Label(frame, text='Carga 2')
label.grid(row=0,column=2)

chargedefault2 = tk.StringVar()
entry_charge = Entry(frame, width=10, textvariable=chargedefault2)
entry_charge.grid(row=1, column=2)
chargedefault2.set(4)

# Distance
distanceLab = Label(frame, text='Distancia en metros:')
distanceLab.grid(row=3, column=0)

distance = tk.StringVar()

entry_distance = Entry(frame, width=10, textvariable=distance)
entry_distance.grid(row=3, column=1)
distance.set(0.04)

# Force
Result = tk.StringVar()

force = Label(frame, text='La fuerza es: ')
force.grid(row=5, column=1)

entry_force = Entry(frame, width=10, textvariable=Result)
entry_force.grid(row=5, column=2)

# Force Result
def result():
    q1 = float(chargedefault1.get())
    q2 = float(chargedefault2.get())
    d = float(distance.get())
    k_e = 9*(10**9)
    if d == 0:
        Result.set(0)
        error_distance = Label(frame, text='Error, la distancia no puede ser 0')
        error_distance.grid(row=6, column=0)
    else:
        resultdef = "{:.2e}".format((k_e*abs(q1*10**-6)*abs(q1*10**-6))/(d**2))
        Result.set(resultdef)


# Button
play = Button(frame, text='Calcular',command=result)
play.grid(row=4, column=1)

# Slider for distance
slider = Scale(root, from_=0, to=10, orient='horizontal')
slider.set(4)
slider.pack()

# Graphics
positive = PhotoImage(file="/home/mariovlv/Documentos/4to-semestre/electromagnetismo/positive.png")
myimg = canvas.create_image(int(slider.get())*50+320, 250, image=positive)
negative = PhotoImage(file="/home/mariovlv/Documentos/4to-semestre/electromagnetismo/negative.png")
myimg2 = canvas.create_image(290, 250,image=negative)
barra = PhotoImage(file="/home/mariovlv/Documentos/4to-semestre/electromagnetismo/barra.png")
myimgBarra = canvas.create_image(420, 340, image=barra)

# mainloop
root.mainloop()
