#Greatest Common Divisor


class AbstractSort:
    def sort(self):
        raise NotImplementedError


class GreatestCommonDivisor(AbstractSort):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sort(self):
        A = self.num1
        B = self.num2
        if A < B:
            temp = A
            A = B
            B = temp
        elif A % B == 0:
            print(B)
            return
        while A % B != 0:
            rem = A % B
            A = B
            B = rem
        print(B)


if __name__ == '__main__':
    a = 54
    b = 20
    _c = GreatestCommonDivisor(a, b)
    _c.sort()
