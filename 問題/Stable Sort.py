#Stable Sort
import re
import numpy as np


def comparepre(n, NUM, TYP):
    NumDuplicates = list(set([i for i in NUM if NUM.count(i) > 1]))

    length1 = len(NumDuplicates)
    NUM1 = np.array(NUM)
    TYPtemp = []

    for i in range(length1):
        dup = NumDuplicates[i]
        WH = np.where(NUM1 == dup)[0].tolist()
        length2 = len(WH)
        for j in range(length2):
            whtemp = WH[j]
            TYPtemp.append(TYP[whtemp])
    return TYPtemp


def bubble_sort(n, A, B, TYPtemp):

    for i in range(n):
        A[i] = int(A[i])

    for i in range(n):
        for j in range(n-1, i, -1):
            if A[j] < A[j-1]:
                temp1 = A[j]
                A[j] = A[j-1]
                A[j-1] = temp1
                temp2 = B[j]
                B[j] = B[j-1]
                B[j-1] = temp2

    for num in range(n):
        print('{}{}'.format(B[num], A[num]), end=' ')
    print()
    TYPori = TYPtemp
    TYPcur = comparepre(n, A, B)
    if TYPori == TYPcur:
        print('Stable')
    else:
        print('Not stable')
    return None


def selection_sort(n, A1, B1, TYPtemp):

    for i in range(n):
        A1[i] = int(A1[i])

    for j in range(n):
        mini = j
        for k in range(j, n):
            if A1[k] < A1[mini]:
                mini = k
        temp1 = A1[mini]
        A1[mini] = A1[j]
        A1[j] = temp1
        temp2 = B1[mini]
        B1[mini] = B1[j]
        B1[j] = temp2


    for num in range(n):
        print('{}{}'.format(B1[num], A1[num]), end=' ')
    print()

    TYPori = TYPtemp
    TYPcur = comparepre(n, A1, B1)
    if TYPori == TYPcur:
        print('Stable')
    else:
        print('Not stable')


def stable_sort():
    n = int(input('please input the number of the cards'))
    if n > 36 or n < 1:
        print('error')
        return
    NUM = []
    TYP = []
    TYPS = ['S', 'H', 'C', 'D']
    A = input('please input the array')
    for i in range(n):
        num = int(re.findall('\d+', A)[i])
        if num < 1 or num > 9:
            print('error')
            return
        NUM.append(num)
    A = ''.join([i for i in A if not i.isdigit()])
    for i in range(n):
        typ = (re.findall('\S', A)[i])
        if typ in TYPS:
            TYP.append(typ)
        else:
            print('error')
            return
    NUM1 = NUM.copy()
    TYP1 = TYP.copy()
    TYPtemp = comparepre(n, NUM, TYP)
    bubble_sort(n, NUM, TYP, TYPtemp)
    selection_sort(n, NUM1, TYP1, TYPtemp)


if __name__ == '__main__':
    stable_sort()