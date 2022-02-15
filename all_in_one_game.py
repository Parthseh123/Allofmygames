a=["Guess the word","Guess the number","quistionaire","secret diary","stone paper scissor","quistionaire 2",
"Odd Even"]
print(a)
game=input("Enter the name of the game that you want to play - ")

if("Guess the word" in game):
    import Guesstheword
if("Guess the number" in game):
    import Guessthenumber
if("quistionaire" in game):
    import quistionaire
if("secret diary" in game):
    import secretdiary
if("stone paper scissor" in game):
    import stone_paper_scissor
if("quistionaire 2" in game):
    import quistionaire2
if("Odd Even" in game):
    import oddeven
