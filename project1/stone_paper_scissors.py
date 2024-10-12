import random

def game(b,r):
        if ((r==b=="s") or (b==r== "p") or (b==r=="sc")):
            return None
        elif ((b=="s" and r=="sc") or (b=="p" and r=="r") or (b=="sc" and r=="p")):
            return True
        elif ((b=="s" and r=="p") or (b=="p" and r=="sc") or (b=="sc" and r=="r")):
            return False

you = input("Player's Trun: Stone(s) Paper(p) Scissors(sc)? \n")

r= random.randrange(1,4)
if r== 1:
    comp = "s"
elif r ==2:
    comp = "p"
elif r ==3:
    comp= "sc"

a = game(you,comp)
if a== True:
     print("You win")
elif a== False:
     print("Comp win")
elif a== None :
     print("Its a draw")