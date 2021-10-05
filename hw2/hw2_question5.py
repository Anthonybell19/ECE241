
"""
UMass ECE 241 - Advanced Programming
Homework #2     Fall 2021
question5.py - 3 way merge sort

"""


## This is an example of code to merge two lists in a descending order
## You can directly call this function or write your own one

# The two lists "lefthalf" and "righthalf" are start from i and j
# The destination list "alist" start from the given position "pos"
# The function returns the number of comparisons during merge
def merge2List(alist, lefthalf, righthalf, i, j, pos):

    comparison = 0 # initial the comparison number as 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            alist[pos] = righthalf[j]
            j += 1
        else:
            alist[pos] = lefthalf[i]
            i += 1
        comparison += 1
        pos += 1

    while i < len(lefthalf): # add the remained numbers in the lefthalf to alist
        alist[pos] = lefthalf[i]
        i = i + 1
        pos += 1

    while j < len(righthalf): # add the remained numbers in the righthalf to alist
        alist[pos]=righthalf[j]
        j=j+1
        pos += 1

    return comparison



## Implement 3 way merge sorting algorithm
## It takes a given list "alist" and return the number of comparison used
def mergeSort_3_way(alist):

    comparison = 0

    if len(alist)>1:
        firstThird = int(len(alist)/3)
        secondThird = int(len(alist)*2/3)

        leftThird =  alist[:firstThird]
        middleThird = alist[firstThird:secondThird] # split list into three thirds
        rightThird = alist[secondThird:]


        mergeSort_3_way(leftThird)
        mergeSort_3_way(middleThird)    #recursive calls on the merge function
        mergeSort_3_way(rightThird)



        i=0
        j=0     # 4 instantiated variables for sorting the lists
        q=0
        k=0

        while i < len(leftThird) and j < len(middleThird) and q < len(rightThird):
            if leftThird[i] >= middleThird[j]:
                if leftThird[i] >= rightThird[q]:
                    alist[k] = leftThird[i]
                    i = i + 1
                else:
                    alist[k] = rightThird[q]
                    q = q + 1
            else:
                if middleThird[j] >= rightThird[q]:
                    alist[k] = middleThird[j]
                    j = j + 1
                else:
                    alist[k] = rightThird[q]
                    q = q + 1
            comparison+=1
            k += 1

        while i < len(leftThird) and j < len(middleThird):
            if leftThird[i] >= middleThird[j]:
                alist[k] = leftThird[i]
                i = i + 1
            else:
                alist[k] = middleThird[j]
                j = j + 1
            comparison +=1
            k = k + 1

        while i < len(leftThird) and q < len(rightThird):
            if leftThird[i] >= rightThird[q]:
                alist[k] = leftThird[i]
                i = i + 1
            else:
                alist[k] = rightThird[q]
                q = q + 1
            comparison += 1
            k = k + 1

        while j < len(middleThird) and q < len(rightThird):
            if middleThird[j] >= rightThird[q]:
                alist[k] = middleThird[j]
                j = j + 1
            else:
                alist[k] = rightThird[q]
                q = q + 1
            comparison += 1
            k = k + 1

        while i < len(leftThird):
            alist[k] = leftThird[i]
            i = i + 1
            comparison += 1
            k += 1
        while j < len(middleThird):
            alist[k] = middleThird[j]
            j = j + 1
            comparison += 1
            k += 1
        while q < len(rightThird):
            alist[k] = rightThird[q]
            q = q + 1
            comparison += 1
            k += 1


        return comparison


alist = [54,26,93,17,77,31,44,55,20]
print(mergeSort_3_way(alist))