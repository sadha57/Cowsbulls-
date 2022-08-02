import tkinter as tk
import random as r
import string
from functools import partial  
from tkinter.messagebox import *
def enterName(s1):
	global k
	k=str(s1.get())
	s=len(k)
	if(s<3 or k.isdigit()):
		showinfo(title="Player Name",message="Please enter valid Name")
		return
	
root = tk.Tk()
root.geometry('700x1300')
f1 = tk.Frame(root)
f2 = tk.Frame(root)
f3=tk.Frame(root)
def free(l6,l7,label_result):
	label_result.config(text="")
	l6.config(text="")
	l7.config(text="")
def call_name(label_result, n1):
	global system
	global c
	global b
	global t1
	global g
	t1 = str(n1.get())
	if(g>0):
		cowsbulls()	
		label_result.config(text=label_result.cget("text")+"\n"+t1+'\t\t'+str(c)+'\t\t'+str(b),fg='blue')

#to switch b/w frames
def raise_frame(frame):
	frame.tkraise()

for frame in (f1, f2,f3):
    frame.grid(row=0, column=0, sticky='news')


raise_frame(f1)
#select type of game
def easy():
	global n
	global system
	n=3
	L=['0','1','2','3','4','5','6','7','8','9']
	system=""
	enterName()
	for i in range(n):
		a=r.choice(L)
		L.remove(a)
		system+=a
	return 
def medium():
	global n
	global system
	n=4
	L=['0','1','2','3','4','5','6','7','8','9']
	system=""
	enterName()
	for i in range(n):
		a=r.choice(L)
		L.remove(a)
		system+=a
	return 
def hard():
    global n
    global system
    n=5
    L=['0','1','2','3','4','5','6','7','8','9']
    system=""
    enterName()
    for i in range(n):
    	a=r.choice(L)
    	L.remove(a)
    	system+=a
    return 
   
def five():
    global g
    g=5
    return
def ten():
    global g
    g=10
    return
def fifteen():
    global g
    g=15
    return 
# Contents of frame 1
r5=tk.Button(f1,text='i',font='Times 7 bold',bg='yellow',command=lambda:raise_frame(f3)).grid(column=0,row=0)
stxt=tk.StringVar()
cb=tk.Label(f1,text="COWS BULLS",fg='red',font='Times 15 bold',pady=40).grid(column=1,row=0)
l1=tk.Label(f1,font='arial 10',text="Your Name:",fg='blue').grid(column=0,row=1)
E1= tk.Entry(f1,textvariable=stxt).grid(row=1, column=1)  
l2=tk.Label(f1,font='arial 10',text="Select Type:",fg='blue').grid(column=0,row=2 )
l3=tk.Label(f1,font='arial 10',text="Chances:",fg='blue').grid( column=0,row=5)
enterName = partial(enterName, stxt)  
b1=tk.Button(f1, width='10',text='START',fg='white',bg='purple',font='Times 15',command=lambda:raise_frame(f2)).grid(row=10,column=1,pady=30)

easy1=tk.Button(f1,width=8,font='arial 10',fg='white',bg='black',text="Easy",command=easy).grid( column=1,row=2,pady=5 )
medium2=tk.Button(f1,width=8,font='arial 10',fg='white',bg='black',text="Medium",command=medium).grid(column=1,row=3,pady=5)
hard3=tk.Button(f1,text="Hard",width=8,font='arial 10',fg='white',bg='black',command=hard).grid(column=1,row=4,pady=5)

chance5=tk.Button(f1,text="5",width=5,font='arial 10',fg='red',bg='white',command=five).grid(column=1,row=5,pady=5)
chance10=tk.Button(f1,text="10",width=5,font='arial 10',fg='red',bg='white',command=ten).grid( column=1,row=6,pady=5 )
chance15=tk.Button(f1,text="15",width=5,font='arial 10',fg='red',bg='white',command=fifteen).grid(column=1,row=7,pady=5)

def cowsbulls():
	global c
	global b
	global g
	
	b=c=0
	g=g-1
	mine=str(t1)
	for i in range(n):
		if(system[i]==mine[i]):
			c+=1
		if(mine[i] in system):
			b+=1
	if(c==n):
		l6.config(text="Congratulations..!   %s\nU R D CHAMP \nAnswer is:%s"%(k,system),fg='green',font='arial 10 bold ')
		b2=tk.Button(f2, bg='cyan',text='Play Again',command=lambda:[free(l6,l7,label_result),raise_frame(f1)]).grid(column=0,row=11)
		return
	else:
		b-=c
		l7.config(text="Chances Left:%d"%g)
	
	if(g==0):
		l6.config(text='U LOST.. '+k+'\nAnswer is:%s'%system,fg='red',font='arial 10 bold ')
		b2=tk.Button(f2,bg='cyan',font='arial 10 bold',text='Play Again',command=lambda:[free(l6,l7,label_result),raise_frame(f1)]).grid(column=0,row=11)
		return
#contents of frame 2
text1 = tk.StringVar()  
text1.set=""
cb=tk.Label(f2,text="COWS BULLS",fg='red',font='Times 15 bold').grid(column=0,row=0,pady=30)
l5=tk.Label(f2,text='Take a Guess:',fg='black',font='arial 10 bold').grid(column=0,row=1,pady=5) 
entryNum1 = tk.Entry(f2,width=5,textvariable=text1).grid(row=2, column=0,pady=15)

swtch1=tk.Button(f2,text='←',font='arial 8 bold',fg='black',bg='white',command=lambda:raise_frame(f1)).grid(column=1,row=10)

listOfGuesses=tk.Label(f2,text='Number\t\tCows\t\tBulls',font='arial 8 bold' ).grid(column=0,row=5)
label_result = tk.Label(f2)  
label_result.grid(row=6, column=0) 
l6=tk.Label(f2)
l6.grid(column=0,row=7)
l7=tk.Label(f2)
l7.grid(column=0,row=10) 

call_name = partial(call_name, label_result, text1)  
buttonCal = tk.Button(f2, text="Check", command=call_name,fg='white',bg='black').grid(row=3, column=0,pady=50)  

#frame3 for rules 
cb=tk.Label(f3,text="COWS BULLS",fg='red',font='Times 15 bold').grid(column=0,row=0,pady=30)

rules=tk.Label(f3,text=">>>Instructions to play The Game....\n",fg='blue',font='Times 10 bold').grid()
r1=tk.Label(f3,text=">>The device sets a Number\n that do not repeat..\n>>You have to GUESS that number \nBy using some clues\n\n>>Now device will check\n corresponding Numbers \n are they placed Correctly or not\n\n>>Here \nCows=No.of digits which are exactly placed \n Bulls=No. of digits at different position\n\n>> if u place them correctly YOU WIN..!!\n",font='arial 8 bold').grid()

r2=tk.Label(f3,text='>>Selection of game type:\nEasy->with 3 digits\nMedium->with 4 digits\nHard->with 5 digits\n\n >>Selecting Chances:\n How many chances you need \nto accomplish the game in 5,10 and 15',font='arial 8 bold').grid()
startNow=tk.Button(f3,text='Click to Play',command=lambda:raise_frame(f1),bg='pink').grid()
f1.grid()
f2.grid()
f3.grid()
root.mainloop()
