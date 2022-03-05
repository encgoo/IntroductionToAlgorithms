# Create a heap that can handle both max and min

from heapq import heappop
from heapq import heappush

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

    def get_lst(self):
        ret = []
        while self.lst:
            ret.append(self.heappop())
        return ret

if __name__ =='__main__':
    h = Heap()
    h.heappush(1)
    h.heappush(100)
    h.heappush(-20)
    print(h.get_lst())

    h1 = Heap(reverse=True)
    h1.heappush(1)
    h1.heappush(0)
    h1.heappush(100)
    h1.heappush(-20)
    print(h1.get_lst())