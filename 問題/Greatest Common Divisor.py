#Greatest Common Divisor

def greatest_common_divisor():
    A = input('please input the numbers')
    A = A.split(' ')
    a = int(A[0])
    b = int(A[1])
    if a < b:
        temp = a
        a = b
        b = temp
    elif a % b == 0:
        print(b)
        return
    while a % b != 0:
        rem = a % b
        a = b
        b = rem
    print(b)


if __name__ == '__main__':
    greatest_common_divisor()