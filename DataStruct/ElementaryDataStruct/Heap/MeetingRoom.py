from heapq import heappush
from heapq import heappop


def meeting_room(intrs):
    # sort intervals according to start time
    intrs = sorted(intrs, key=lambda x:x[0])

    endtime = []
    for intr in intrs:
        if len(endtime) > 0:
            if endtime[0] <= intr[0]:
                heappop(endtime)

        heappush(endtime, intr[1])

    return len(endtime)


if __name__ == '__main__':
    intrs = [(2, 15), (36, 45), (9, 29), (16, 23), (4,9)]

    print(meeting_room(intrs))