firstnumber = int(input ("Please enter first number") )
secondnumber = int(input ("Please enter the second number"))
thirdnumber = int(input (" Please enter the thirdnumber"))
counteven=0
countodd=0

if firstnumber %2==0:
    counteven=counteven+1
else:
    countodd=countodd+1

if secondnumber %2==0:
    counteven=counteven+1
else:
    countodd=countodd+1
    
if thirdnumber %2==0:
    counteven=counteven+1
else:
    counteven=counteven+1
print("The number of even is " + str(counteven))
print("The number of odd us" + str(counteven))

    
  
  