import sys
import tkinter as tk
from modules import *

o1 = []
o2 = []
m1 = create_null_matrix(9, 5)
m2 = create_null_matrix(9, 5)
mf={}

def set_():
    global ent_x, ent_y, o1, o2, l_e_1, l_e_2, m1, m2
    s = ent_x.get()
    ok = False
    for k in s:
        if k not in "1234567890xX, ":
            ok = False
        else:
            ok = True
    if ok:
        for i in "xX, ":
            o = s.split(i)
            f = 0
            for j in o:
                if j.isnumeric():
                    ok = True
                else:
                    ok = False
                    f += 1
            if f == 0:
                break
    if not ok:
        error()
    o1 = [int(o[0]), int(o[1])]
    print("o1=", o)

    del s, ok, f, o

    s = ent_y.get()
    ok = False
    for k in s:
        if k not in "1234567890xX, ":
            ok = False
        else:
            ok = True
    if ok:
        for i in "xX, ":
            o = s.split(i)
            f = 0
            for j in o:
                if j.isnumeric():
                    ok = True
                else:
                    ok = False
                    f += 1
            if f == 0:
                break
    if not ok:
        error()
    o2 = [int(o[0]), int(o[1])]
    print("o2=", o)

    for i in range(0, 5):
        for j in range(0, 5):
            if i >= o1[0] or j >= o1[1]:
                try:
                    l_e_1[i][j].delete(0,len(l_e_1[i][j].get()))
                    l_e_1[i][j].config(state="disabled")
                except:
                    pass
            else:
                try:
                    l_e_1[i][j].config(state="normal")
                except:
                    pass
    for i in range(0, 5):
        for j in range(0, 5):
            if i >= o2[0] or j >= o2[1]:
                try:
                    l_e_2[i][j].delete(0,len(l_e_2[i][j].get()))
                    l_e_2[i][j].config(state="disabled")
                except:
                    pass
            else:
                try:
                    l_e_2[i][j].config(state="normal")
                except:
                    pass
    m1 = create_null_matrix(o1[0], o1[1])
    m2 = create_null_matrix(o2[0], o2[1])

def find():
    global o1, o2, l_e_1, l_e_2, m1, m2 , mf
    for j in range(0, o1[0]):
        for i in range(0, o1[1]):
            s1 = l_e_1[j][i].get()
            if s1 == "":
                s1 = '0'
            s = int(s1)
            m1[j][i] = s
    for j in range(0, o2[0]):
        for i in range(0, o2[1]):
            s1 = l_e_2[j][i].get()
            if s1 == "":
                s1 = '0'
            s = int(s1)
            m2[j][i] = s
    mf = multiply_matrices(m1, m2)
    o = find_order(mf)
    win = tk.Tk()
    win.geometry('720x500')
    win.title("..::Result Matrices::..")
    win.minsize(width=720, height=500)
    print (mf)
    for i in range(0,o[1]):
        for j in range(0,o[0]):
            print(i,",",j)
            print(str(mf[j][i]))
            exec("lbl"+str(i)+str(j)+" = tk.Label(win, text="+str(mf[j][i])+", fg='DeepSkyBlue4', bg='light sky blue', font=('Arial Black', 15))")
            exec("lbl"+str(i)+str(j)+".place(relx="+str(0.05+i*0.18)+", rely="+str(0.05+j*0.18)+", relheight=0.17, relwidth=0.17)")


# -----------------------main window----------------------------------------------------------------

win = tk.Tk()
win.geometry('1280x720')
win.title("..::Set Matrices::..")
win.minsize(width=1280, height=720)

bck_grd = tk.Label(win, text="", fg="DeepSkyBlue4", bg="light sky blue", font=("Arial Black", 15))
lbl = tk.Label(win, text="", fg="DeepSkyBlue4", bg="DeepSkyBlue4", font=("Arial Black", 15))
lbl1 = tk.Label(win, text="Matrix 1:", fg="DeepSkyBlue4", bg="light sky blue", font=("Arial Black", 15))
lbl2 = tk.Label(win, text="Matrix 2:", fg="DeepSkyBlue4", bg="light sky blue", font=("Arial Black", 15))
ent_x = tk.Entry(win, fg="steel blue", bg="light cyan", font=("Arial Bold", 20), justify='center')
ent_y = tk.Entry(win, fg="steel blue", bg="light cyan", font=("Arial Bold", 20), justify='center')
ent_x.insert(0, "5x5")
ent_y.insert(0, "5x5")
bttn0 = tk.Button(win, text="SET", fg="sky blue", bg="DeepSkyBlue4", font=("Arial Bold", 20), command=set_)
bttn = tk.Button(win, text="OK", fg="sky blue", bg="DeepSkyBlue4", font=("Arial Bold", 20), command=find)

bck_grd.place(relx=0, rely=0, relheight=1, relwidth=1)
lbl.place(relx=0.49, rely=0, relheight=1, relwidth=0.01)
lbl1.place(relx=0, rely=0.01, relheight=0.06, relwidth=0.2)
lbl2.place(relx=0.5, rely=0.01, relheight=0.06, relwidth=0.195)
ent_x.place(relx=0.1875, rely=0.01, relheight=0.06, relwidth=0.25)
ent_y.place(relx=0.7, rely=0.01, relheight=0.06, relwidth=0.25)
bttn0.place(relx=0.45, rely=0, relheight=0.08, relwidth=0.1)
bttn.place(relx=0, rely=0.91, relheight=0.09, relwidth=1)

l_e_1 = {}
l_e_2 = {}

for j in range(0, 5):
    l_e_1[j] = []
    l_e_2[j] = []
    for i in range(0, 5):
        l_e_1[j].append(0)
        l_e_2[j].append(0)

for j in range(0, 5):
    for i in range(0, 5):
        s1 = "ent_1_" + str(j) + "_" + str(
            i) + "=tk.Entry(win,fg = 'steel blue',bg = 'light cyan',font=('Arial', 18),justify='center')"
        s2 = "ent_1_" + str(j) + "_" + str(i) + ".place(relx=" + str(0.0125 + i * 0.09) + ",rely=" + str(
            0.15 + j * 0.15) + ", relheight=0.09, relwidth=0.085)"
        exec(s1)
        exec(s2)
        exec("l_e_1[" + str(j) + "][" + str(i) + "]=(ent_1_" + str(j) + "_" + str(i) + ")")

for j in range(0, 5):
    for i in range(0, 5):
        s1 = "ent_2_" + str(j) + "_" + str(
            i) + "=tk.Entry(win,fg = 'steel blue',bg = 'light cyan',font=('Arial', 18),justify='center')"
        s2 = "ent_2_" + str(j) + "_" + str(i) + ".place(relx=" + str(0.5235 + i * 0.09) + ",rely=" + str(
            0.15 + j * 0.15) + ", relheight=0.09, relwidth=0.085)"
        exec(s1)
        exec(s2)
        exec("l_e_2[" + str(j) + "][" + str(i) + "]=(ent_2_" + str(j) + "_" + str(i) + ")")

win.mainloop()
