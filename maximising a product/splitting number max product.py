#not restricted to splitting by integers
N = int(input("Enter N"))
array=[]
for k in range(1,N+1):
    array.append((N/k)**k)

print(array)
print("")

print("Maximum:", max(array))

x=array.index(max(array))+1

print("")
print("for sum: ",max(array)**(1/x),"*",N/(max(array)**(1/x)),"=",N)
print("for product: ",max(array)**(1/x),"^",N/(max(array)**(1/x)),"=",max(array))
