#Selection Sort

class AbstractSort:
    def sort(self):
        raise NotImplementedError


class SelectionSort(AbstractSort):
    def __init__(self, num, arr):
        self.num = num
        self.arr = arr
        
    def sort(self):
        n = self.num
        if n < 1 or n > 100:
            print('error')
            return
        A = self.arr
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
    n = 6
    Arr = [5, 6, 4, 2, 1, 3]
    _c = SelectionSort(n, Arr)
    _c.sort()

