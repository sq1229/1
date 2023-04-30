#BubbleSort

def bubble_sort():
    print('BubbleSort')
    n = int(input('please input the amount of the numbers'))
    if n < 1 or n > 100:
        print('error')
        return
    A = input('please input the array')
    A = A.split(' ')
    for i in range(n):
        A[i] = int(A[i])
    times = 0

    for i in range(n):
        for j in range(n-1, i, -1):
            if A[j] < A[j-1]:
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
                times += 1

    print(*A)
    print(times)


if __name__ == '__main__':
    bubble_sort()
