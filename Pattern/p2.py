n=6
for i in range(1,n):
     for s in range(n-i):
          print(end=" ")
     for j in range(1,i+1):
        print("* ",end="")
     print("")
