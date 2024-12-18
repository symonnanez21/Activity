for s in range(7,0,-1):
    for y in range(1,s+1):
        print(" ",end=" ")
    for m in range(6,s,-1):
        print("*",end=" ")
    for o in range(7,s,-1):
        print("*",end=" ")
    print()
for n in range(1,6):
    for a in range(0,n + 1):
        print(" ",end=" ")
    for b in range(5,n,-1):
        print("*",end=" ")
    for c in range(6,n,-1):
        print("*",end=" ")
    print()
