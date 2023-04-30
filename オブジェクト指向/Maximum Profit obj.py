#Maximum Profit


class AbstractSort:
    def sort(self):
        raise NotImplementedError


class MaximumProfit(AbstractSort):
    def __init__(self, n, num):
        self.n = n
        self.num = num

    def sort(self):
        Rt = []
        Dv = []
        for i in range(self.n):
            Rtemp = self.num[i]
            Rt.append(Rtemp)
        for j in range(self.n):
            for k in range(j+1, self.n):
                Dv.append(Rt[k] - Rt[j])
        print(max(Dv))


if __name__ == '__main__':
    times = 6
    nums = [5, 3, 1, 3, 4, 3]
    _c = MaximumProfit(times, nums)
    _c.sort()
