import random
import tkinter as tk
from tkinter import *
parent=tk.Tk()
parent.title("WELCOME EVERYBODY TO THE ANAGRAMS GAME")
w=Label(parent,text="LET'S PLAY THE GAME",font=("Arial", 40))
w.pack(pady=100)
parent.geometry("800x600")
parent.configure(bg="lightblue")
w.configure(bg="lightblue")
def new():
    f=open('game1.txt','r')
    S=random.choice(f.readlines())
    input_string=""
    for i in S:
        if(i!='\n'):
            input_string+=i
    f.close()
    attempts=(len(input_string))//2
    if(attempts%2!=0):
        attempts+=1
    a=list(input_string)
    q=list(input_string)
    random.shuffle(q)
    ana_string=""
    for i in q:
        if(i!='\n'):
            ana_string+=i
    d=0
    numbers=[]
    for i in range(1,len(input_string)+1):
           numbers.append(i)
    result1=[]
    result1=random.sample(numbers,attempts-1)
    result2=""
    for i in range(0,len(result1)):
        result2+=f"{result1[i]} "
    dis.config(text=f"{ana_string.upper()}",foreground="red",font=("Times New Roman", 20),bg="lightblue")
    #dis.place(x=850,y=200)
    guess.config(text=f"{d}")
    attempts1.config(text=f"{attempts}")
    Instructions.config(text=f"INSTRUCTIONS:\n1.The above given sequence of letters are jumbled from a meaningful word.\n2.Number of attempts to guess the word are {attempts}\n3.After every wrong attempt you wiil get the position of a specific letter.\nThat's all..Enjoy The Game!!!")
    input_string1.config(text=f"{input_string}")
    a1.config(text=f"{a}")
    prev.config(text="0")
    result.config(text=f"{result2}")
    input.config(state=NORMAL)
    out.config(text="")
    out1.config(text="")
def value(index):
    x=index%10
    if(x==1):
        return f'{index}st'
    elif(x==2):
        return f'{index}nd'
    elif(x==3):
        return f'{index}rd'
    else:
        return f'{index}th'
def clue(input_string,index):
    a=list(input_string)
    out1.config(text=f"The {value(index)} word is {a[index-1]}")
def play():
    users_input=input.get()
    d=int(guess["text"])
    d=d+1
    input_string=input_string1["text"]
    attempts=int(attempts1["text"])
    guess.config(text=str(d))
    index=int(prev["text"])
    prev.config(text=str(index+1))
    result2=(result["text"])
    z=result2.split(" ")
    if(users_input.upper()==input_string.upper()): 
        out.config(text="")
        out.config(text="You Guessed it right.Congratulations")
        out1.config(text="")   
        dis.config(text="")
    elif(users_input.upper()!=input_string.upper()):
        out.config(text="")
        input.delete(0,tk.END)
        if(d!=attempts):
            out.config(text="Your guess is wrong!\n.I am going to give you a clue :")
            clue(input_string,int(z[index]))
        else:
            out.config(text=f"You lost the game\n.The actual word is {input_string.upper()}") 
            out1.config(text="")
            input.config(state=DISABLED)
dis=Label(text="")
dis.pack()
input_string1=Label(text="")
input=Entry(parent,font=("Times New Roman", 30),textvariable="Enter the word")
input.pack()
guess=Label(text="")
attempts1=Label(text="")
prev=Label(text="")
a1=Label(text="")
result=Label(text="")
but=Button(parent,text="Submit",font = ("Times New Roman",15),command=play)
but.pack(pady=10)
but=Button(parent,text="new game",font = ("Times New Roman",15),command=new)
but.pack(pady=10)
out=Label(text="",background="lightblue")
out.pack()
out1=Label(text="",background="lightblue")
out1.pack()
Instructions=Label(parent,background="lightblue",font=("Times New Roman",20),border=0,foreground="green")
Instructions.pack()
#Instructions.place(x=350,y=550)
new()
parent.mainloop()