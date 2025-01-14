a=(int(input("enter no:")))
c=0
for i in range(2, a):
    if(a%i==0):
        c=c+1
        break
if(c==0):
     print(a,"is a prime number")
else:
     print(a,"is not a prime number")
       