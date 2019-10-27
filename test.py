print("Whats happen when last petal falls?")
response=input
print("My dear  Bella Whenthe last petal falls", response)



print("Have you fear your heart?")
response=input
if response == "yes":
    print("Fear is the path to the dark side")
 else:
     print("The force is strong in you. You may be a Jedi apprentice."")   



print("How many zones must I cross?")
zones=int(input)
print("Crossing zones")
while zones>0:
    print(Crossed zone, + str(zones))
    zones = zones-1

print(Crossed all zones. Jump!)



def visit(ghost):
    if ghost == "Ghost of Christmas Past":
        print("Humbug! I care not for these days of past celebration.")
    elif ghost =="Ghost of Christmas Present" :
        print("Humbug! I care not for their suffering.")
    else:
        print("Please no more. I will change my ways.")

visit("Ghost of Christmas Past") 
visit(“Ghost of Christmas Present") 
visit("Ghost of Christmas Future")




