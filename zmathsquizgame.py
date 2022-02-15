anwserdic= {
    "a1":2,
    "a2":144,
    "a3":-5,
    "a4":9425,
    "a5":64,
    "a6":20736,
    "a7":4/10,
    "a8":2,
    "a9":2,
    "a10":2,
}

print("maths quiz")

points=0
q1= int(input("what is 2+2-2*2/2 - "))

for i in range(100):
    if(anwserdic["a1"]== q1):
        points=points+1
        print("Wright anwser you got 1 point")
        print("score:",points)       
        q2= int(input("find square of 12 - "))
        for i in range(100):
            if(anwserdic["a2"]== q2):
                points=points+1
                print("Wright anwser you got 1 point")
                print("score:",points)       
                q3= int(input("-8 + 9 - 6 = "))
                for i in range(100):
                    if(anwserdic["a3"]== q3):
                        points=points+1
                        print("Wright anwser you got 1 point")
                        print("score:",points)       
                        q4= int(input("what is 29 x 325 - "))
                        for i in range(100):
                            if(anwserdic["a4"]== q4):
                                points=points+1
                                print("Wright anwser you got 1 point")
                                print("score:",points)       
                                q5= int(input("what is the perimeter of a square with a side of 16 - "))
                                for i in range(100):
                                    if(anwserdic["a5"]== q5):
                                        points=points+1
                                        print("Wright anwser you got 1 point")
                                        print("score:",points)       
                                        q6= int(input("what is the area of a square with a side of 144 -"))
                                        for i in range(100):
                                            if(anwserdic["a6"]== q6):
                                                points=points+1
                                                print("Wright anwser you got 1 point")
                                                print("score:",points)       
                                                q7= int(input("what is 29 x 325 - "))
                                                for i in range(100):
                                                    if(anwserdic["a7"]== q7):
                                                        points=points+1
                                                        print("Wright anwser you got 1 point")
                                                        print("score:",points)       
                                                        q8= int(input("2/10 + 1/5 - "))
                                                        for i in range(100):
                                                            if(anwserdic["a8"]== q8):
                                                                points=points+1
                                                                print("Wright anwser you got 1 point")
                                                                print("score:",points)       
                                                                q9= int(input("what is 29 x 325 - "))

                                                            else:
                                                                print("wrong anwser try again")
                                                                print("score:",points)
                                                                q8= int(input("2/10 + 1/5 - "))

                                                    else:
                                                        print("wrong anwser try again")
                                                        print("score:",points)
                                                        q7= int(input("what is 29 x 325 - "))

                                            else:
                                                print("wrong anwser try again")
                                                print("score:",points)
                                                q6= int(input("6÷2(1+2) = "))

                                    else:
                                        print("wrong anwser try again")
                                        print("score:",points)
                                        q5= int(input("what is 29 x 325 - "))

                            else:
                                print("wrong anwser try again")
                                print("score:",points)
                                q4= int(input("what is 29 x 325 - "))
                    else:
                        print("wrong anwser try again")
                        print("score:",points)
                        q3= int(input("-8 + 9 - 6 = "))
        
                        
            else:
                print("wrong anwser try again")
                print("score:",points)
                q2= int(input("find square of 12 - "))
        
    else:
        print("wrong anwser try again")
        print("score:",points)
        q1= int(input("what is 2+2-2*2/2 - "))