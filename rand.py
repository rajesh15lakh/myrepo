#import random
from random import  random,randint,uniform as u,randrange,choice as c   #as is alice name
import  time
#for i in range(7)
for i in range(1):
    for j in range(1):
        print(random())  #o to 1 but 1 is not inclusive
        print(randint(1,100))  #within specified range but last no. in the range is inclusive
        print(u(11,20))  #float numbers
        print(randrange(1,15,2)) # 2 is a step,default step is 1... generate random int within 1 to 15
        print(randrange(1,9),randrange(1,9),randrange(1,9),randrange(1,9),randrange(1,9),sep="")
        #print(randint(1,9),end="")
    print()
    time.sleep(2)

#only list and tuple we can take..cant take elements in set and dict
p=(1,2,3,4,5,6,7,8,9)
r=['1','v','r','i','99','y','x']
for i in range(5):
    print(c(p)) #take random elements in r
    print(c(r))
    time.sleep(2)

