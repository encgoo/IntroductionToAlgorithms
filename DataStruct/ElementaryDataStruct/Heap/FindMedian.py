from heapq import heappush
from heapq import heappop

# use two heaps
from heapq import heappush
from heapq import heappop

class Heap:
    def __init__(self, reverse=False):
        self.lst = []
        self.coef = 1
        if reverse:
            self.coef = -1

    def heappush(self, n):
        heappush(self.lst, n*self.coef)

    def heappop(self):
        return self.coef*heappop(self.lst)

    def size(self):
        return len(self.lst)

    def get_lst(self):
        ret = []
        while self.lst:
            ret.append(self.heappop())
        return ret

    def get_first(self):
        return self.coef*self.lst[0]

class MedianFinder:
    def __init__(self):
        self.min = Heap()
        self.max = Heap(reverse=True)

    def add_num(self, n):
        # put into min first
        self.min.heappush(n)

        self.max.heappush(self.min.heappop())
        if self.max.size() > self.min.size():
            self.min.heappush(self.max.heappop())

    def get_median(self):
        if self.min.size() > self.max.size():
            return self.min.get_first()
        else:
            return (self.min.get_first()+self.max.get_first())/2

if __name__ == '__main__':
    md = MedianFinder()
    #md.add_num(5)
    #md.add_num(1)
    #md.add_num(4)
    md.add_num(1)
    md.add_num(2)
    print(md.get_median())
    md.add_num(3)
    print(md.get_median())