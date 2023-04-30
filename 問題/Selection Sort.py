#Selection Sort

def selection_sort():
    n = int(input('please input the amount of the numbers'))
    if n < 1 or n > 100:
        print('error')
        return
    A = input('please input the array')
    A = A.split(' ')
    for i in range(n):
        A[i] = int(A[i])
    times = 0
    for j in range(n):
        mini = j
        for k in range(j, n):
            if A[k] < A[mini]:
                mini = k
        if mini != j:
            times += 1
        temp = A[mini]
        A[mini] = A[j]
        A[j] = temp
    print(*A)
    print(times)


if __name__ == '__main__':
    selection_sort()
