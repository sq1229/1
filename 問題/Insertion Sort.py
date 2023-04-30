#Insertion Sort


def insertion_sort(n,A):
    """
    >>> InsertionSort(6,[5,2,4,6,1,3])
    [1, 2, 3, 4, 5, 6]
    >>> InsertionSort(3,[1,2,3])
    [1, 2, 3]
    """


    print('Insertion Sort')
    if n >100 or n<1:
        print('error')
        return
    #if the length is too large,stop the function

    #change the input into array
    for i in range(n):
        A[i] = int(A[i])
    #change the element in the array into int
    for i in range(n):
        key = A[i]
        j = i-1
        while j>=0 and A[j]>key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        print(*A)


if __name__ == '__main__':
    n = int(input('please input the length of the array'))
    A = input('please input the array')
    A = A.split(' ')
    insertion_sort(n, A)
"""
    import doctest
    doctest.testmod()
"""