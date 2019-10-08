print("Please enter a number")
factorial=int(input())
count=factorial-1
while count>0:
    factorial = factorial * (count)
    count = count -1

print(str(factorial))
