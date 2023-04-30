#BubbleSort


class AbstractSort:
    def sort(self):
        raise NotImplementedError


class BubbleSort(AbstractSort):
    def __init__(self, num, arr):
        self.num = num
        self.arr = arr
        
    def sort(self):
        print('BubbleSort')
        n = self.num
        if n < 1 or n > 100:
            print('error')
            return
        A = self.arr
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
    n = 5
    Arr = [5, 3, 2, 4, 1]
    _c = BubbleSort(n, Arr)
    _c.sort()

