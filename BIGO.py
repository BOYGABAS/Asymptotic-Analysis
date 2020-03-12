'''
Isaiah Andre Pabillon
BSCS-2
2018-5769

Algorithm:

    1) Create an empty list to be filled with random elements

    2) Generate random number at particular iterations and append them to the empty list                            #2) Set a random range from 0 to 25 and add it to the ASCII equivalent of
                                                                                                                    "A" to produce random letters from "A" to "Z" and append it to the empty list
    3) Perform both sorting algorithms
                                                                                                                    #3) Repeat step #2 at your leisure
    4) Go back to step #2 but for every iteration, multiply the iterations of generating random numbers by 10
                                                                                                                    #4) Ask user to select which sorting algorithm to perform

                                                                                                                    #4.1) If user inputs "1" then perform insertion sort

                                                                                                                    #4.2) If user inputs "2" or any string if the user is bored, then perform merge sort

        Insertion sort:

            1) Create a new empty list

            2) Scan through the elements of the scrambled list

                2.1) If the new list is empty then simply append element

                2.2) Else compare them to the elements of the new list and declare a variable
                    for the index that will start iterating

                    2.2.1) If the current element in the scrambled list is greater than the
                          element of the new list, then move to the next element via incrementing
                          the index variable

                    2.2.2) Else add/insert the element from the scrambled list to the new list
                           at the index[variable]

            3) Display the new list

        Merge sort:

            1) Allocate three lists which are left,right and final

            2) Browse through the scrambled list and append them to the new lists accordingly

                2.1) If the element's index is at the lower half of the list then assign to left list

                2.2) Else assign it to the right list

            3) With the left and right lists, do step #1

            4) If the list came to a point where there is only 1 element, return as a list

            5) Sort the elements of the two lists by scanning their elements and appending the lesset one
              to the final list and the list with the lesser element will select the next element in its list

            6) If one side of the lists are already finished, append the remaining elements of the other list
              to the final list as they are already the later/bigger items since they are already sorted

            7) Repeat until sorted and print output



'''
import random
import time
import math
import matplotlib.pyplot


print("PATIENCE IS A VIRTUE")
n=0
xaxis=[]
yaxisO1=[]
yaxisOlogn=[]
yaxisOnlogn=[]
yaxisOn=[]
yaxisOn2=[]
yaxisOn3=[]
yaxisO2n=[]
scrambledlist=[]
sortlist=[]
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
matplotlib.pyplot.plot(xaxis, yaxisO1)
matplotlib.pyplot.plot(xaxis, yaxisOlogn)
matplotlib.pyplot.plot(xaxis, yaxisOnlogn)
matplotlib.pyplot.plot(xaxis, yaxisOn)
matplotlib.pyplot.plot(xaxis, yaxisOn2)
matplotlib.pyplot.plot(xaxis, yaxisOn3)
matplotlib.pyplot.plot(xaxis, yaxisO2n)
matplotlib.pyplot.xlabel('number of entries')
matplotlib.pyplot.ylabel('time')
matplotlib.pyplot.title('Difference between merge and insertion sorting')
matplotlib.pyplot.show()
