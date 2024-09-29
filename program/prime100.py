for i in range(1,100+1):
     if(i>1):
          flag = False
          for j in range(2,i):
                if(i%j==0):
                   flag = True
                   break
          if(flag==False):
               print(i,end=" ")
     