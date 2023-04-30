#Maximum Profit

def maximum_profit():
    n = int(input('please input how many time points do you have:'))
    if n > 200000 or n < 2:
        print('error')
        return
    Rt = []
    Dv = []
    for i in range(n):
        Rtemp = int(input())
        if Rtemp < 0 or Rtemp > 10**9:
            print('error')
            return
        Rt.append(Rtemp)
    for j in range(n):
        for k in range(j+1, n):
            Dv.append(Rt[k] - Rt[j])
    print(max(Dv))


if __name__ == '__main__':
    maximum_profit()

