#Insertion Sort

class AbstractSort:
    def sort(self):
        raise NotImplementedError


class InsertionSort(AbstractSort):
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


if __name__ == '__main__':
    n = 6
    Arr = [5, 2, 4, 6, 1, 3]
    _c = InsertionSort(n, Arr)
    _c.sort()
