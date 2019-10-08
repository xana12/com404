print("How many numbers should I sum up?")
numbers=int(input())
count=0
total=0
while(count<numbers):
    numbersadd=int(input())
    total+=numbersadd
    count+=1
print(str(total))

