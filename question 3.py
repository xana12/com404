print("How many miles must I travel before I reach the secret base?")
miles = int(input())

print("I will count the miles...")
while miles > 0:
    print("I have... miles to go before I reach the base" + str(miles))
    miles = miles-1 

print("I have arrived at the secret headquarters of the MIB!")
print("It is time to sneak in.")