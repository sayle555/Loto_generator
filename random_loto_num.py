import random
from random import randint, choice
from tkinter import *
import string

def loto_generator():
    loto_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
    #loto_list2=[i for i in range(1,50)]
    number=random.sample(loto_list, 5)
    nums_entry.delete(0, END)
    nums_entry.insert(0, number)
    """l=[]
    r= random.randint(1,50)
    if r not in l:
        l.append(r)"""


def stars_generator():
    stars_list = [1,2,3,4,5,6,7,8,9,10]
    number=random.sample(stars_list, 1)
    stars_entry.delete(0, END)
    stars_entry.insert(0, number)

#creer la fenetre
window=Tk()
window.title("Générateur de numero du LOTO")
window.geometry("720x480")
window.iconbitmap("logo_loto(ico).ico")
window.config(background="white")

#creer une frame principale
frame=Frame(window, bg="white")

#creation dimage
width=300
height=250
image=PhotoImage(file="logo_loto.png").zoom(10).subsample(30)
canvas=Canvas(frame, width=width, height=height, bg="white", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)


#creer un sous boite
right_frame=Frame(frame, bg="white")

# creer un titre
label_title=Label(right_frame, text="Numeros du LOTO:", font=("helvetica", 20), bg="white", fg="black")
label_title.pack()

#creer un champ/entrée/input
nums_entry=Entry(right_frame, text="saisie", font=("helvetica", 20), bg="white", fg="black")
nums_entry.pack()

# creer un boutton
generate_password_button=Button(right_frame, text="generer", font=("helvetica", 20), bg="#41B77F", fg="black", command=loto_generator)
generate_password_button.pack(fill=X)

# creer un titre
label_title2=Label(right_frame, text="Étoile:", font=("helvetica", 20), bg="white", fg="black")
label_title2.pack()

#creer un champ/entrée/input
stars_entry=Entry(right_frame, text="a remplir", font=("helvetica", 20), bg="white", fg="black")
stars_entry.pack()

# creer un boutton
generate_stars_button=Button(right_frame, text="generer", font=("helvetica", 20), bg="#41B77F", fg="black", command=stars_generator)
generate_stars_button.pack(fill=X)

#on place la sous boite a droite de la frame principale
right_frame.grid(row=0, column=1, sticky=SW)

#afficher la frame
frame.pack(expand=YES)

#afficher la fenetre
window.mainloop()
