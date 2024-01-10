#
# ROCK, PAPER, SCISSORS - Iterācija 2
# 
# 4. Pārkopēt šeit iepriekšējo failu, modificēt spēli no iepriekšēja faila, lai ir pieci raundi un beigas rādas cik sanāca vinnēt (izmantot for loop, https://www.w3schools.com/python/python_for_loops.asp)
# 5. [Bonus Level] Izmantot ne vairāk par trīs if/else rezultāta skaitīšanai (var izmantot ciparu starpību)
# 6. [UNSTOPPABLE] Pievieno papildus ieročus Rock-Paper-Scissors-Spock-Lizard (https://en.wikipedia.org/wiki/Rock_paper_scissors#Additional_weapons)
# 
import random
#
# ROCK, PAPER, SCISSORS - Iterācija 1
# 
# 1. Spēle prasa ievadīt ciparu no 1 līdz 3 (izmanto input, https://www.w3schools.com/python/python_user_input.asp)
# 2. Dators iedomājas ciparu no 1 līdz 3  (izmanto random, https://www.w3schools.com/python/ref_random_randint.asp)
# 3. Atkarībā no ievadītajiem cipariem un datora, izdrukā paziņojumu par zaudējumu, uzvaru, vai neizšķirtu (izmanto if, else https://www.w3schools.com/python/python_conditions.asp)
#
neizskirti=0
uzvaras=0
PM=0
OM=0
dators=" "
print("Izvēlies Akmens, Sķēres vai Papīrs")

def game():
    variants = input("Tavs variants: ")
    global PM
    global OM
    global dators
    global uzvaras
    global neizskirti
    if variants == "Akmens":
        OM=1
    elif variants == "Šķēres":
        OM=2
    elif variants == "Papīrs":
        OM=3
    else:
        print("Ievadītais variants neeksistē vai tika ievadīts nepareizi")
    PM=random.randint(1,3)
    if PM == 1:
        dators="Akmeni"
    elif PM == 2:
        dators="ŠĶēres"
    elif PM == 3:
        dators="Papīru"
    if PM == OM:
        print("Neizšķirts , pretinieks izvēlējās: " , dators)
        neizskirti=neizskirti+1
    elif PM == 1 and OM == 2:
        print("Tu zaudēji, pretinieks izvēlējās: " , dators)
    elif PM == 2 and OM == 3:
        print("Tu zaudēji, pretinieks izvēlējās: " , dators)
    elif PM == 3 and OM == 1:
        print("Tu zaudēji, pretinieks izvēlējās: " , dators)
    elif PM == 1 and OM == 3:
        print("Tu Uzvarēji, pretinieks izvēlējās: " , dators)
        uzvaras=uzvaras+1
    elif PM == 3 and OM == 2:
        print("Tu Uzvarēji, pretinieks izvēlējās: " , dators)
        uzvaras=uzvaras+1
    elif PM == 2 and OM == 1:
        print("Tu Uzvarēji, pretinieks izvēlējās: " , dators)
        uzvaras=uzvaras+1
    else:
        print("Kļūda")
for x in range(5):
    game()
if uzvaras==1:
    print("Tu uzvarēji: " , uzvaras , """ reizi!! 
Pretinieks Uzvarēja: """ , 5-uzvaras-neizskirti , " reizes")
else:
    print("Tu uzvarēji: " , uzvaras , """ reizes!! 
Pretinieks Uzvarēja: """ , 5-uzvaras-neizskirti , " reizes")