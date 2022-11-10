import sys
import tkinter


def error(x="There's an error!!"):
    print(x)
    sys.exit()


def create_null_matrix(r, c):
    m1 = {}
    l = []
    for i in range(0, c):
        l += [0]
    for i in range(0, r):
        m1[i] = list(l)
    return m1


def create_matrix(l):
    # l is the dictionary of tkinter entries
    r = len(l.keys())
    c = len(l[0])
    m1 = create_null_matrix(r, c)
    o = find_order(m1)
    for i in range(0, o[0]):
        for j in range(0, o[1]):
            m1[i][j] = l[i][j].get()
    return m1


def create_matrix_from_input(r, c):
    m1 = {}
    l = []
    for i in range(0, c):
        l += [0]
    for i in range(0, r):
        m1[i] = list(l)
    for i in range(0, r):
        for j in range(0, c):
            txt = "Enter row:" + str(i + 1) + ", column" + str(j + 1) + ':'
            while True:
                vv = input(txt)
                if vv == '':
                    vv = '0'
                elif not vv.isdigit():
                    txt = '!!' + txt
                    continue
                try:
                    m1[i][j] = int(vv)
                    break
                except:
                    txt = '!!' + txt
    return m1


def check_if_ok(m1):
    x = type({1: ''})
    if type(m1) != x:
        error()
    c = len(m1)
    r_prev = len(m1[list(m1.keys())[0]])
    for i in m1.keys():
        if type(m1[i]) != type([]):
            error()
        r_now = len(m1[i])
        if r_now != r_prev:
            error()
        else:
            r_prev = r_now


def find_order(m1):
    check_if_ok(m1)
    r = len(m1.keys())
    c = len(m1[list(m1.keys())[0]])
    return [r, c]


def transpose(m):
    l = find_order(m)
    m1 = create_null_matrix(l[1], l[0])
    for i in m.keys():
        for j in range(0, len(m[i])):
            m1[j][i] = m[i][j]
    return m1

"""def find_determinant(m):
    find_order(a)
    for i in range(0,len(m.keys()[0]):"""
        

def add_matrices(m1,m2):
    o1=find_order(m1)
    o2=find_order(m2)
    if o1[0]==o2[0] and o1[1]==o2[1]:
        m=create_null_matrix(o1[0],o1[1])
        for i in range(0,o1[0]):
            for j in range(0,o1[1]):
                m[i][j]=m1[i][j]+m2[i][j]
    else:
        error("Please provide feasible matrices for addition.")
    return m
        
def multiply_matrices(m1, m2_):
    m2 = transpose(m2_)
    o1 = find_order(m1)
    o2_ = find_order(m2_)
    o2 = find_order(m2)
    if o1[1] != o2_[0]:
        error("Please provide feasible matrices for mutiplication.")
    mf = {}  # this is the result matrix
    l = []
    for j in range(0, o2_[1]):
        l += [0]
    for i in range(0, o1[0]):
        mf[i] = list(l)
    del l
    el = 0
    for i in range(0, o1[0]):
        for a in range(0, o2_[1]):
            for b in range(0, o2_[0]):
                el += m1[i][b] * m2[a][b]
            mf[i][a] = el
            el = 0
    return mf
