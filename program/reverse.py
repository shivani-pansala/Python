a = [50,40,30,20,10]

i=0
j=4
while i<=j:
     temp=a[i]
     a[i]=a[j]
     a[j]=temp
     i+=1
     j-=1

for i in a:
     print(i,end=" ")