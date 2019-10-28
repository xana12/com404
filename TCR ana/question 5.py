health=100
print("Your health is 100%. Escape is in progress...")

for count in range(0,5,1):
    print("...Oh dear. who is this?")
    user = str(input())


    if (user == "smileer bot"):
        health-health-20
        print("Time to jam out of here")

    elif (user == "hacker"):
        health=health+20
        print("Yap. Better follow this one")
    
    else:
        print("Phwew. just another emoji")

print("Esacped health is" + str(health))