from heapq import heappush
from heapq import heappop



class LNode:
    def __init__(self, v):
        self.v = v

# if you want to use heap to sort obj, like LNode above, put it into a
# tuple. The first one is the val you want to use to sort. But
# be careful, if the first is the same, heapq will use the second one
# if __lt__ is not defined for the obj class, then it will error out.

# one trick is to use the second one for tie break. Put the obj in third
# make sure the tie break can always break the tie, then the comparision
# of the objs is not needed.

heap = []
heappush(heap, (1,2, LNode(1)))
heappush(heap, (1,3, LNode(2)))

print('Done')