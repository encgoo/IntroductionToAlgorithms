# https://www.programcreek.com/2013/03/leetcode-lru-cache-java/
# almost like a queue. But need random access/edit. So use a double linked list
from collections import defaultdict


def def_val():
    return None


class LNode:
    def __init__(self, key=0, val=0, p=None, n=None):
        self.key = key
        self.val = val
        self.p = p
        self.n = n

    @staticmethod
    def print_lst(rt):
        nd = rt
        while nd:
            print('key: ' + str(nd.key) + ', val: ' + str(nd.val))
            nd = nd.n


class LRUCache:
    def __init__(self, sz):
        self.dict_ = defaultdict(def_val)
        self.sz = sz
        self.head = None
        self.tail = None

    def get(self, key):
        if not self.dict_[key]:
            return -1

        node = self.dict_[key]

        self.del_node(node)
        self.offer_node(node)

        return node.val

    def put(self, key, value):
        if self.dict_[key]:
            node = self.dict_[key]
            node.val = value

            # move to tail
            self.del_node(node)
            self.app_node(node)
        else:
            if len(self.dict_.keys()) > self.sz:
                self.dict_.pop(self.head.key, None)
                self.del_node(self.head)

            node = LNode(key, value)
            self.app_node(node)
            self.dict_[key] = node

    def del_node(self, nd):
        if nd.p:
            nd.p.n = nd.n
        else:
            self.head = nd.n

        if nd.n:
            nd.n.p = nd.p
        else:
            self.tail = nd.p

    def app_node(self, nd):
        if self.tail:
            self.tail.n = nd

        nd.p = self.tail
        nd.n = None
        self.tail = nd

        if not self.head:
            self.head = self.tail

    def print_cache(self):
        LNode.print_lst(self.head)


if __name__ == '__main__':
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 1)
    cache.put(3, 1)
    cache.put(2, 1)
    cache.put(6, 1)
    cache.put(8, 1)
    cache.print_cache()






