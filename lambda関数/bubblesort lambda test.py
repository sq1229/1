#BubbleSort

def bubble_sort(n, A, comp_func):
    print('BubbleSort')

    if n < 1 or n > 100:
        print('error')
        return

    for i in range(n):
        A[i] = int(A[i])
    times = 0

    for i in range(n):
        for j in range(n-1, i, -1):
            #if comp_func(A[j],A[j-1]):
            if A[j] < A[j-1]:
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
                times += 1

    print(*A)
    print(times)
    B = sorted(A, key = comp_func)
    print(*B)
if __name__ == '__main__':
    n = 5
    A = [5, 3, 2, 4, 1]
    bubble_sort(n, A, comp_func=(lambda x: x%2))
    #bubble_sort(n, A, comp_func=(lambda x,y: x>y))
    # bubble_sort(n, A, comp_func=(lambda x,y: x<y))