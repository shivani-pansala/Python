for i in range(1,6):
          for j in range(1,1+i):
                if ((i==5 or i==j) or (j==1 or  j==5)):
                   print(" *",end=" ")
                else:
                     print("  ",end=" ")  
          print()