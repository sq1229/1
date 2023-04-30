import math


class AbstractSort:
    def sort(self):
        raise NotImplementedError


class PrimeNumbers(AbstractSort):
    def __init__(self, n, num):
        self.n = n
        self.num = num

    def sort(self):
        n = self.n
        nums = self.num
        primenums = 0
        for i in range(n):
            num = nums[i]
            if num < 2 or num > 10**8:
                print('error')
                return
            if num == 2 or num == 3:
                primenums += 1
            else:
                temp = int(math.sqrt(num))
                for j in range(2, temp+1):
                    if num % j == 0:
                        primenums -= 1
                        break
                primenums += 1
        print(primenums)


if __name__ == '__main__':
    a = 5
    b = [2, 3, 4, 5, 6]

    _c = PrimeNumbers(a, b)
    _c.sort()
