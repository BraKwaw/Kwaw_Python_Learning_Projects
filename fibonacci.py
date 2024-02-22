""" this program outputs any of the first given number of terms in the fibonacci sequence the user requests"""
import numpy as np
import matplotlib.pyplot as plt
#importing libraries

fib_seq_terms=int(input("How many items in the sequence do you want? : ")) # asks user to input the number of terms required
fbs=[ ]            #initialize an empty list
first_i=0
second_i=1
                  #initialize first and second values
xlist=np.linspace(0,100,num=fib_seq_terms)    #list of x values
for index in range(fib_seq_terms):
    if index==0:
        fbs.append(first_i)
    if index==1:
        fbs.append(second_i)
    if index>1:
        x=fbs[-1]  #current value
        y=fbs[-2]  #previous value
        z=y+x      #new value
        fbs.append(z)
print(fbs)
plt.plot(xlist,fbs)
plt.show() #displays plot


