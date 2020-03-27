import logging


def do_math(x):
    y = x ^ x
    return x + x ^ 2 + y


FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
mylog = logging.getLogger('log')
mylog.setLevel(1)
x = []
for i in range(6000):
    mylog.debug(f"THis is log line {i}")
    x.append(do_math(i))

print("hello")
print(x)
