from tkinter import *
root = Tk() 
root.geometry("800x600") 
root.title("PATTERN SEARCHING") 
Tops = Frame(root, width = 1600, relief = SUNKEN) 
Tops.pack(side = TOP)

f1 = Frame(root, width =1600, height = 100, relief = SUNKEN) 
f1.pack(side = LEFT)

lblInfo = Label(Tops, font = ('helvetica', 30, 'bold'),text="PATTERN SEARCHING", fg = "Black", bd = 10, anchor='w') 
lblInfo.grid(row = 0, column = 0)

str_ip = StringVar() 
pattern_ip = StringVar() 
index_op = StringVar()

def qExit(): 
	root.destroy() 
def Reset():
    str_ip.set("")
    pattern_ip.set("")
    index_op.set("")

lblReference = Label(f1, font = ('arial', 18, 'bold'), text = "Enter the string", bd = 16, anchor = "w") 
lblReference.grid(row = 1, column = 0) 
txtReference = Entry(f1, font = ('arial', 18, 'bold'), textvariable = str_ip, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right') 
txtReference.grid(row = 1, column = 1)

lbldestin = Label(f1, font = ('arial', 18, 'bold'), text = "Enter pattern to find", bd = 16, anchor = "w") 
lbldestin.grid(row = 3, column = 0) 
txtdestin = Entry(f1, font = ('arial', 18, 'bold'),textvariable = pattern_ip, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right') 
txtdestin.grid(row = 3, column = 1) 

lblkey = Label(f1, font = ('arial', 18, 'bold'), text = "Pattern found at index position", bd = 16, anchor = "w") 
lblkey.grid(row = 5, column = 0) 
txtkey = Entry(f1, font = ('arial', 18, 'bold'), textvariable = index_op, bd = 10, insertwidth = 4,bg = "powder blue", justify = 'right') 
txtkey.grid(row = 5, column = 1) 

def search(pat, txt):
    M = len(pat)
    N = len(txt)
    op_list = list()
    # A loop to slide pat[] one by one */ 
    for i in range(N - M + 1):
        j = 0
		# For current index i, check
        # for pattern match */
        while(j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1
        if (j == M):
            op_list.append(i)
    return op_list
 
def Ref():
    if(len(str_ip.get()) == 0):
        index_op.set("Please enter string!")
        return
    elif(len(pattern_ip.get()) == 0):
        index_op.set("Please enter pattern!")
        return
    lst = search(pattern_ip.get(), str_ip.get())
    if(len(lst) == 0):
        index_op.set("No pattern found!")
        return
    index_op.set(str(lst))
		
btnTotal = Button(f1, padx = 16, pady = 8, bd = 8, fg = "black", font = ('arial', 24, 'bold'), 
    width = 10, text = "GO", bg = "powder blue", command = Ref).grid(row = 7, column = 1) 
btnReset = Button(f1, padx = 16, pady = 8, bd = 8, fg = "white", font = ('arial', 16, 'bold'),
    width = 10, text = "Reset", bg = "green", command = Reset).grid(row = 8, column = 0) 
btnExit = Button(f1, padx = 16, pady = 8, bd = 8,fg = "white", font = ('arial', 16, 'bold'),
    width = 10, text = "Exit", bg = "red",command = qExit).grid(row = 8, column = 1) 
root.mainloop()
