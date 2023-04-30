import abc


class method():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calculate(self):
        pass


class BubbleSort(method):
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


class SelectionSort(method):
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


class InsertionSort(method):
    def __init__(self, num, arr):
        self.num = num
        self.arr = arr

    def sort(self):
        print('Insertion Sort')
#change the element in the array into int
        nums = self.num
        for i in range(nums):
            A = self.arr
            key = A[i]
            j = i-1
            while j >= 0 and A[j] > key:
                A[j+1] = A[j]
                j -= 1
            A[j+1] = key
            print(*A)


class MethodFactory:

    def creat_method(self, method):
        if method == 'bubblesort':
            return BubbleSort(n,Arr)
        elif method == 'selectionsort':
            return SelectionSort(n,Arr)
        elif method == 'insertionsort':
            return InsertionSort(n,Arr)
        else:
            print('error')


if __name__ == '__main__':
    n = 6
    Arr = [5, 6, 4, 2, 1, 3]
    c = MethodFactory()
    #_c = c.creat_method('bubblesort')
    #_c.sort()
    _c = c.creat_method('insertionsort')
    _c.sort()
    #_c = c.creat_method('selectionsort')
    #_c.sort()

