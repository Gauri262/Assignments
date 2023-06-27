#for loop with else 
#break
for i in range(9):
    if i==5:
        break
    else:
        print(i)
else:
    print("Break in for")
print("-------")

#continue
for i in range(9):
    if i==5:
        continue
    else:
        print(i)
else:
    print("Continue in for")
print("-------")
#pass
for i in range(9):
    if i==5:
        pass
    else:
        print(i)
else:
    print("Pass in for")

#while loop with else

#break
i=1
while i<=10:
    if i==7:
        break
    else:
        print(i)
    i+=1
else:
    print("Break in while")
print("-------")

#continue
i=1
while i<=10:
    if i==7:
        continue
    else:
        print(i)
    i+=1
else:
    print("Continue in while")
print("------")

#pass
i=1
while i<=10:
    if i==7:
        pass
    else:
        print(i)
    i+=1
else:
    print("Pass in while")


            
