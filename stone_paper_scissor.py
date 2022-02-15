import random
a=input("type st for stone sc for scissor and type pa for paper - ")
op = ["st","sc","pa"]
b= random.choice(op)

score=0
for i in range(1000):
    if("st" in a and "pa" in b):
        score=score-1
        print("you chose stone and computer chose paper \n computer won")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)
        
    elif("sc" in a and "pa" in b):
        score=score+1
        print("you chose scissor and computer chose paper \n you won")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)
        
    elif("pa" in a and "pa" in b):
        print("you chose paper and computer chose paper \n Draw")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)
        
    elif("pa" in a and "sc" in b):
        score=score-1
        print("you chose paper and computer chose sissor \n computer won")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)
        
    elif("pa" in a and "st" in b):
        score=score+1
        print("you chose paper and computer chose stone \n you won")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)
    elif("st" in a and "sc" in b):
        score=score+1
        print("you chose stone and computer chose scissor \n you won")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)
    elif("st" in a and "st" in b):
        print("you chose stone and computer chose stone \n draw")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)
        
    elif("sc" in a and "st" in b):
        score=score-1
        print("you chose scissor and computer chose stone \n computer won")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)
        
    elif("sc" in a and "sc" in b):
        print("you chose scissor and computer chose scissor \n draw")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)
        