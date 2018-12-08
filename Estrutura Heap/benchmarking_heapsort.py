from heap import Heap
from random import shuffle
from time import time


gerada = list(range(1000))
shuffle(gerada)

heap = Heap(gerada)

before = time()
heap.heapsort()
after = time()

total = (after - before) * 1000
print(f'The HeapSot took {total} ms to order {len(heap)} elements')
