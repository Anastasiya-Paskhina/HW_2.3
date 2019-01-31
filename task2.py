import hashlib
from task1 import dec_log


@dec_log('C:\\Users\\Александр\\PycharmProjects\\HW 2.3\\')
def generate(path):
    with open(path) as f:
        for line in f:
            h = hashlib.md5(line.encode('utf-8'))
            yield h.hexdigest()


for item in generate('result2.txt'):
    print(item)