import threading


gRet = 0


def print_str(st, n):
    global gRet
    for i in range(n):
        print(st)
    gRet = 1

t = threading.Thread(target=print_str, args=("Hello World", 2))
t.start()

print('Main thread printing')

t.join()

print('Done' + str(gRet))