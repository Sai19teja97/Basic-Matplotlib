# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:59:13 2019

@author: sai teja
"""

#_MATPLOTLIB TUTORIAL

#import libraries
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline ##with out using plt.show()in jupiter note book

#simple example scatter plot
a=np.arange(0,10)
b=np.arange(11,21)

c=np.arange(40,50)
d=np.arange(50,60)
plt.scatter(a,b,c='g')
plt.title('graph in 2d')
plt.xlabel('x_axis')
plt.ylabel('y_axis')

y=a*b
##plt plot
plt.plot(a,y,'r--')
plt.plot(a,y,'r*-')
plt.plot(a,y,'ro--')
plt.plot(a,y,'ro',linestyle='dashed',linewidth=3,markersize=10)
plt.title('plt plot')
plt.xlabel('x axis')
plt.ylabel('y axis')


##creating a subplot
plt.subplot(2,2,1)
plt.plot(a,y,'r--')
plt.subplot(2,2,2)
plt.plot(a,y,'y*-')
plt.subplot(2,2,3)
plt.plot(a,y,'bo-')
plt.subplot(2,2,4)
plt.plot(a,y,'g')
plt.show()

x=np.arange(1,11)
y=3*x+5
plt.plot(x,y,'r*-')
plt.title('matplotdemo')
plt.xlabel('x axis')
plt.ylabel('y axis')

##compute the x and y coordinates for point on a sine curve
np.pi

x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)
plt.title('sine wave')
plt.plot(x,y)
plt.show()

x=np.arange(0,4*np.pi,0.1)
y_sin=np.sin(x)
y_cos=np.cos(x)

plt.subplot(2,1,1)
plt.plot(x,y_sin,'b-')
plt.title('sine')

plt.subplot(2,1,2)
plt.plot(x,y_cos,'g--')
plt.plot('y_cos')

##barplot
x=[1,2,3]
y=[5,6,8]

s=[10,12,11]
t=[20,22,21]
plt.bar(x,y,align='center')
plt.bar(s,t,color='g')
plt.title('bar graph')
plt.show()

##histogram
a=np.array([22,87,5,43,56,13,55,54,11,20,51,5,79,31,27])
plt.hist(a)
plt.title("histogram")
plt.show()

##boxplot
data=[np.random.normal(0,std,100)for std in range(1,4)]
plt.boxplot(data,vert=True,patch_artist=True);

###pie chart
labels='python','r','c++','java'
sizes=[215,130,245,210]
colors=['gold','yellowgreen','red','lightskyblue']
exploded=(0.1,0,0,0)

plt.pie(sizes,explode=exploded,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True)

plt.axis('equal')
plt.show()


   
