# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib
from matplotlib import style
style.use('ggplot')

#Importing pyplot
from matplotlib import pyplot as plt
data=np.loadtxt(r"C:\Users\HP\Desktop\data.txt",  delimiter='\t', skiprows=1)
#print(data)


#Plotting to our canvas
"""for i in range(1, 10):
    for j in range(i+1,11):

        #plt.plot(data[:,i],data[:,j])
        plt.scatter(data[:,i][data[:,0]==1], data[:,j][data[:,0]==1] , color='red',label='Label 1')#, align='center')
        plt.scatter(data[:,i][data[:,0]==2], data[:,j][data[:,0]==2] , color='blue',label='Label 2')#, align='center')
        plt.title('Feature '+str(i)+'vs'+str(j))
        plt.ylabel('feature'+ str(j))
        plt.xlabel('feature  '+str(i))
        plt.legend()
        plt.savefig('feature'+str(i)+'vs'+str(j)+'.png')
        plt.show()"""

        #the two features which classify the labels perfectly are feature 1 and 2 (the plots feature1vs2.png)
