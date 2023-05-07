import random
z=True
while(z):
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
    boole=True
    print(" This is a ",len(input_string),"word"," and your no of attempts is ",attempts," and the anagram word is ",ana_string)
    print("Your game starts now")
    numbers=[]
    for i in range(1,len(input_string)):
        numbers.append(i)
    while(boole):
        if(d==attempts):
            print("You lost the game")
            print("The actual word is", input_string)
            break
        d+=1
        ana_string=input("ENTER THE ANA STRING: ")
        
        if(ana_string!=input_string):
            print("Your guess is wrong :")
            if(d!=attempts):
                print("I am going to give you a clue :")
                x=len(input_string)
                index=random.choice(numbers)
                print(" The ",index," value is ",a[index-1])
        else:
            boole=False
            print("You are right")
            break

    
    x=input("Do you want to play the game again [Y/N]: ")
    if(x=='N'):
        z=False
    elif(x=='Y'):
        z=True
    else:
        print("You have written something wrong.Please write the required character ")
        x=input("Do you want to play the game again [Y/N]: ")
        if(x=='N'):
            z=False
        elif(x=='Y'):
            z=True
