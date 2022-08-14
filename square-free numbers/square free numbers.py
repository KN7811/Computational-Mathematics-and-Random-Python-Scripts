import numpy as np
from matplotlib import pyplot as plt

b = np.array([])

for k in range(0,100):
    def isSquareFree(n): 
          
        if n % 2 == 0: 
            n = n / 2
      
        if n % 2 == 0: 
            return False
      
        for i in range(3, int(np.sqrt(n) + 1)):         
            if n % i == 0: 
                n = n / i  
            if n % i == 0: 
                return False
        return True
      

    ##n = int(input("Enter a number"))
    ##if isSquareFree(n): 
    ##    print ("Yes") 
    ##else: 
    ##    print ("No")


    a = np.random.randint(1000, size = 10000)

    count = 0
    for i in range(0, len(a)):
        if isSquareFree(a[i]) == True:
            count = count + 1

    x = count/len(a)
    b = np.append(b,x)


print(a)
print(len(a))
print(b)
print(np.mean(b))
print(len(b))
##plt.plot(b)
##plt.axis([0,100, 0,1])
##plt.xlabel('Iteration')
##plt.ylabel('Probability')
##plt.suptitle('Probability of choosing a square-free number')
##plt.show()

