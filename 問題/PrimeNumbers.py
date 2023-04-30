#Prime Numbers
import math


def prime_numbers():
    n = int(input('please input how many numbers do you want:'))
    if n > 10000 or n < 1:
        print('error')
        return
    primenums = 0
    for i in range(n):
        num = int(input())
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
    prime_numbers()



