import random
import time
import math
import matplotlib.pyplot as mat


print("PATIENCE IS A VIRTUE")
n=1
xaxis=[]
yaxisO1=[]
yaxisOlogn=[]
yaxisOnlogn=[]
yaxisOn=[]
yaxisOn2=[]
yaxisOn3=[]
yaxisO2n=[]
while n<25:
    xaxis.append(n)
    yaxisO1.append(1)
    yaxisOlogn.append(math.log(n,10))
    yaxisOnlogn.append(n*math.log(n,10))
    yaxisOn.append(n)
    yaxisOn2.append(n^2)
    yaxisOn3.append(n^3)
    yaxisO2n.append(2^n)
    n+=1
mat.plot(xaxis, yaxisO1)
mat.plot(xaxis, yaxisOlogn)
mat.plot(xaxis, yaxisOnlogn)
mat.plot(xaxis, yaxisOn)
mat.plot(xaxis, yaxisOn2)
mat.plot(xaxis, yaxisOn3)
mat.plot(xaxis, yaxisO2n)
mat.xlabel('N')
mat.ylabel('F(N)')
mat.title('Difference between merge and insertion sorting')
mat.show()
